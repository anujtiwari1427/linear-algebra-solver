import numpy as np
import scipy.linalg as la
import sympy as sp
from typing import Dict, Any, List, Optional
from services.validation_service import sanitize_and_parse_matrix, sanitize_and_parse_vector
from services.matrix_service import format_number, matrix_to_latex, matrix_to_list

def solve_gaussian_elimination(mat_a: np.ndarray, vec_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    r, c = mat_a.shape
    if r != c:
        return {"success": False, "error": f"Gaussian elimination requires a square coefficient matrix A. Got {r}x{c}."}

    n = r
    # Create augmented matrix [A | b]
    aug = np.hstack([mat_a.copy().astype(float), vec_b.copy().reshape(-1, 1).astype(float)])

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Gaussian Elimination (Forward Elimination):")
        steps.append(f"Initial Augmented Matrix $[A \\mid b]$:")
        steps.append(f"$$[A \\mid b] = {matrix_to_latex(aug)}$$")

    # Forward elimination
    for i in range(n):
        # Partial pivoting
        pivot_row = i + np.argmax(np.abs(aug[i:, i]))
        if abs(aug[pivot_row, i]) < 1e-12:
            continue

        if pivot_row != i:
            aug[[i, pivot_row]] = aug[[pivot_row, i]]
            if show_steps:
                steps.append(f"Swap Row ${i+1}$ and Row ${pivot_row+1}$ for numerical stability:")
                steps.append(f"$$[A \\mid b] \\to {matrix_to_latex(aug)}$$")

        # Eliminate entries below pivot
        for j in range(i + 1, n):
            factor = aug[j, i] / aug[i, i]
            if abs(factor) > 1e-12:
                aug[j, i:] -= factor * aug[i, i:]
                if show_steps:
                    steps.append(f"Row operation: $R_{{{j+1}}} \\leftarrow R_{{{j+1}}} - ({format_number(factor)}) R_{{{i+1}}}$")
                    steps.append(f"$$[A \\mid b] \\to {matrix_to_latex(aug)}$$")

    # Rank check for consistency
    coeff_mat = aug[:, :n]
    const_vec = aug[:, n]

    rank_a = int(np.linalg.matrix_rank(coeff_mat))
    rank_aug = int(np.linalg.matrix_rank(aug))

    if rank_a < rank_aug:
        return {
            "success": True,
            "solution_type": "No Solution",
            "explanation": f"System is inconsistent (Rank(A) = {rank_a} < Rank([A|b]) = {rank_aug}). Parallel planes/lines do not intersect.",
            "steps": steps,
            "latex_result": "\\text{No Solution (Inconsistent System)}"
        }

    if rank_a < n:
        return {
            "success": True,
            "solution_type": "Infinitely Many Solutions",
            "explanation": f"System has infinitely many solutions (Rank = {rank_a} < n = {n}). Free parameters exist.",
            "steps": steps,
            "latex_result": f"\\text{{Infinitely Many Solutions (Rank = {rank_a} < {n})}}"
        }

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (aug[i, n] - np.dot(aug[i, i + 1:n], x[i + 1:n])) / aug[i, i]

    if show_steps:
        steps.append("#### Back Substitution Phase:")
        for i in range(n - 1, -1, -1):
            knowns = " + ".join([f"({format_number(aug[i, k])})({format_number(x[k])})" for k in range(i + 1, n)])
            rhs = f"{format_number(aug[i, n])}"
            if knowns:
                steps.append(f"$x_{{{i+1}}} = \\frac{{{rhs} - ({knowns})}}{{{format_number(aug[i, i])}}} = {format_number(x[i])}$")
            else:
                steps.append(f"$x_{{{i+1}}} = \\frac{{{rhs}}}{{{format_number(aug[i, i])}}} = {format_number(x[i])}$")

    sol_vars = [f"x_{{{i+1}}} = {format_number(val)}" for i, val in enumerate(x)]
    latex_sol = ", \\quad ".join(sol_vars)

    return {
        "success": True,
        "operation": "Gaussian Elimination",
        "solution_type": "Unique Solution",
        "solution": [round(float(val), 4) for val in x],
        "latex_result": latex_sol,
        "steps": steps,
        "explanation": "Gaussian elimination reduces the augmented matrix to Upper Triangular form before performing back-substitution.",
        "time_complexity": f"O({n}^3)"
    }


def solve_gauss_jordan(mat_a: np.ndarray, vec_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    r, c = mat_a.shape
    if r != c:
        return {"success": False, "error": f"Gauss-Jordan elimination requires square coefficient matrix. Got {r}x{c}."}

    n = r
    aug = np.hstack([mat_a.copy().astype(float), vec_b.copy().reshape(-1, 1).astype(float)])
    sp_aug = sp.Matrix(aug)
    rref_mat, pivot_cols = sp_aug.rref()

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Gauss-Jordan Reduction to RREF:")
        steps.append("Unlike standard Gaussian elimination, Gauss-Jordan eliminates entries both above and below each pivot, reducing $A$ directly to the Identity Matrix $I$.")
        steps.append(f"Initial $[A \\mid b] = {matrix_to_latex(aug)}$")
        steps.append(f"$$\\text{{RREF}}([A \\mid b]) = {sp.latex(rref_mat)}$$")

    rank_a = int(np.linalg.matrix_rank(mat_a))
    aug_arr = np.array(rref_mat, dtype=float)
    rank_aug = int(np.linalg.matrix_rank(np.hstack([mat_a, vec_b.reshape(-1, 1)])))

    if rank_a < rank_aug:
        return {
            "success": True,
            "solution_type": "No Solution",
            "explanation": "System is inconsistent. Rank(A) < Rank([A|b]).",
            "steps": steps,
            "latex_result": "\\text{No Solution}"
        }

    if rank_a < n:
        return {
            "success": True,
            "solution_type": "Infinitely Many Solutions",
            "explanation": f"System has infinitely many solutions (Rank = {rank_a} < n = {n}).",
            "steps": steps,
            "latex_result": f"\\text{{Infinitely Many Solutions (Rank = {rank_a})}}"
        }

    solution = [float(rref_mat[i, -1]) for i in range(n)]
    sol_vars = [f"x_{{{i+1}}} = {format_number(val)}" for i, val in enumerate(solution)]
    latex_sol = ", \\quad ".join(sol_vars)

    return {
        "success": True,
        "operation": "Gauss-Jordan Elimination",
        "solution_type": "Unique Solution",
        "solution": [round(val, 4) for val in solution],
        "latex_result": latex_sol,
        "steps": steps,
        "explanation": "Gauss-Jordan elimination reduces [A | b] directly into Reduced Row Echelon Form [I | x].",
        "time_complexity": f"O({n}^3)"
    }


def solve_lu_method(mat_a: np.ndarray, vec_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    r, c = mat_a.shape
    if r != c:
        return {"success": False, "error": f"LU Method requires square matrix A. Got {r}x{c}."}

    n = r
    det_a = float(np.linalg.det(mat_a))
    if abs(det_a) < 1e-9:
        return {"success": False, "error": "Matrix A is singular (det = 0). LU decomposition cannot solve singular system uniquely."}

    P, L, U = la.lu(mat_a)

    # Solve P L U x = b => L y = P^T b, U x = y
    pb = P.T @ vec_b
    y = la.solve_triangular(L, pb, lower=True)
    x = la.solve_triangular(U, y, lower=False)

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step LU Decomposition System Solution:")
        steps.append("1. Factorize matrix $A = P \\cdot L \\cdot U$:")
        steps.append(f"$$P = {matrix_to_latex(P)}, \\quad L = {matrix_to_latex(L)}, \\quad U = {matrix_to_latex(U)}$$")
        steps.append("2. Forward substitution solve $L y = P^T b$:")
        steps.append(f"$$y = {matrix_to_latex(y.reshape(-1, 1))}$$")
        steps.append("3. Back substitution solve $U x = y$:")
        steps.append(f"$$x = {matrix_to_latex(x.reshape(-1, 1))}$$")

    sol_vars = [f"x_{{{i+1}}} = {format_number(val)}" for i, val in enumerate(x)]
    latex_sol = ", \\quad ".join(sol_vars)

    return {
        "success": True,
        "operation": "LU Method Solution",
        "solution_type": "Unique Solution",
        "solution": [round(float(val), 4) for val in x],
        "latex_result": latex_sol,
        "steps": steps,
        "explanation": "LU decomposition breaks down Ax=b into forward (Ly=b) and backward (Ux=y) triangular system solves.",
        "time_complexity": f"O({n}^3) \\text{{ factorize + }} O({n}^2) \\text{{ solve}}"
    }


def solve_cramers_rule(mat_a: np.ndarray, vec_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    r, c = mat_a.shape
    if r != c:
        return {"success": False, "error": f"Cramer's rule requires a square coefficient matrix A. Got {r}x{c}."}

    n = r
    det_a = float(np.linalg.det(mat_a))

    if abs(det_a) < 1e-9:
        return {"success": False, "error": f"Cramer's rule is only applicable when \\det(A) \\neq 0. Got \\det(A) = {format_number(det_a)}."}

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Cramer's Rule:")
        steps.append(f"1. Compute main matrix determinant $\\det(A) = {format_number(det_a)}$")

    sols = []
    latex_steps = []
    for i in range(n):
        mat_ai = mat_a.copy()
        mat_ai[:, i] = vec_b
        det_ai = float(np.linalg.det(mat_ai))
        xi = det_ai / det_a
        sols.append(xi)
        if show_steps:
            steps.append(f"Replace Column ${i+1}$ of A with constant vector b to get $A_{{{i+1}}}$:")
            steps.append(f"$$A_{{{i+1}}} = {matrix_to_latex(mat_ai)}, \\quad \\det(A_{{{i+1}}}) = {format_number(det_ai)}$$")
            steps.append(f"$$x_{{{i+1}}} = \\frac{{\\det(A_{{{i+1}}})}}{{\\det(A)}} = \\frac{{{format_number(det_ai)}}}{{{format_number(det_a)}}} = {format_number(xi)}$$")

    sol_vars = [f"x_{{{i+1}}} = {format_number(val)}" for i, val in enumerate(sols)]
    latex_sol = ", \\quad ".join(sol_vars)

    return {
        "success": True,
        "operation": "Cramer's Rule",
        "solution_type": "Unique Solution",
        "solution": [round(val, 4) for val in sols],
        "latex_result": latex_sol,
        "steps": steps,
        "explanation": "Cramer's rule calculates solution variables via ratio of matrix determinants det(A_i)/det(A).",
        "time_complexity": f"O(({n}+1) \\times {n}^3) = O({n}^4)"
    }
