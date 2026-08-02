import numpy as np
import scipy.linalg as la
import sympy as sp
from typing import Dict, Any, List, Optional
from services.validation_service import (
    sanitize_and_parse_matrix,
    validate_square_matrix,
    validate_addition_dimensions,
    validate_multiplication_dimensions,
    validate_invertible_matrix
)

def format_number(val: float) -> str:
    """Format float cleanly, omitting trailing zeroes or converting near-ints."""
    if abs(val - round(val)) < 1e-9:
        return str(int(round(val)))
    return f"{val:.4f}"

def matrix_to_latex(mat: np.ndarray) -> str:
    """Convert NumPy matrix to LaTeX pmatrix string."""
    rows = []
    for row in mat:
        row_str = " & ".join([format_number(x) for x in row])
        rows.append(row_str)
    return "\\begin{pmatrix} " + " \\\\ ".join(rows) + " \\end{pmatrix}"

def matrix_to_list(mat: np.ndarray) -> List[List[float]]:
    """Convert matrix to rounded python float list."""
    return [[round(float(x), 4) for x in row] for row in mat]


def matrix_addition(mat_a: np.ndarray, mat_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    err = validate_addition_dimensions(mat_a, mat_b)
    if err:
        return {"success": False, "error": err}

    res = mat_a + mat_b
    r, c = mat_a.shape

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Element-wise Addition:")
        steps.append(f"Dimensions of Matrix A and B are both ${r} \\times {c}$. Element-wise formula: $C_{{ij}} = A_{{ij}} + B_{{ij}}$")
        
        elem_steps = []
        for i in range(r):
            for j in range(c):
                val_a = mat_a[i, j]
                val_b = mat_b[i, j]
                val_c = res[i, j]
                elem_steps.append(f"$C_{{{i+1}{j+1}}} = A_{{{i+1}{j+1}}} + B_{{{i+1}{j+1}}} = {format_number(val_a)} + ({format_number(val_b)}) = {format_number(val_c)}$")
        steps.extend(elem_steps)

    latex_eq = f"C = A + B = {matrix_to_latex(mat_a)} + {matrix_to_latex(mat_b)} = {matrix_to_latex(res)}"

    return {
        "success": True,
        "operation": "Matrix Addition",
        "input_a": matrix_to_list(mat_a),
        "input_b": matrix_to_list(mat_b),
        "result": matrix_to_list(res),
        "latex_result": latex_eq,
        "steps": steps,
        "explanation": "Matrix addition is an element-wise operation defined for matrices of identical dimensions.",
        "time_complexity": f"O({r} \\times {c})"
    }


def matrix_subtraction(mat_a: np.ndarray, mat_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    err = validate_addition_dimensions(mat_a, mat_b)
    if err:
        return {"success": False, "error": err}

    res = mat_a - mat_b
    r, c = mat_a.shape

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Element-wise Subtraction:")
        steps.append(f"Dimensions of Matrix A and B are both ${r} \\times {c}$. Element-wise formula: $C_{{ij}} = A_{{ij}} - B_{{ij}}$")
        
        elem_steps = []
        for i in range(r):
            for j in range(c):
                val_a = mat_a[i, j]
                val_b = mat_b[i, j]
                val_c = res[i, j]
                elem_steps.append(f"$C_{{{i+1}{j+1}}} = A_{{{i+1}{j+1}}} - B_{{{i+1}{j+1}}} = {format_number(val_a)} - ({format_number(val_b)}) = {format_number(val_c)}$")
        steps.extend(elem_steps)

    latex_eq = f"C = A - B = {matrix_to_latex(mat_a)} - {matrix_to_latex(mat_b)} = {matrix_to_latex(res)}"

    return {
        "success": True,
        "operation": "Matrix Subtraction",
        "input_a": matrix_to_list(mat_a),
        "input_b": matrix_to_list(mat_b),
        "result": matrix_to_list(res),
        "latex_result": latex_eq,
        "steps": steps,
        "explanation": "Matrix subtraction subtracts corresponding elements of Matrix B from Matrix A.",
        "time_complexity": f"O({r} \\times {c})"
    }


def matrix_multiplication(mat_a: np.ndarray, mat_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    err = validate_multiplication_dimensions(mat_a, mat_b)
    if err:
        return {"success": False, "error": err}

    res = np.matmul(mat_a, mat_b)
    r1, c1 = mat_a.shape
    r2, c2 = mat_b.shape

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Matrix Multiplication:")
        steps.append(f"Matrix A is ${r1} \\times {c1}$ and Matrix B is ${r2} \\times {c2}$. Columns of A ({c1}) equals Rows of B ({r2}). Result C is ${r1} \\times {c2}$.")
        steps.append("Formula: $C_{ij} = \\sum_{k=1}^{n} A_{ik} B_{kj}$")

        for i in range(r1):
            for j in range(c2):
                terms = [f"({format_number(mat_a[i, k])} \\times {format_number(mat_b[k, j])})" for k in range(c1)]
                terms_sum = " + ".join(terms)
                steps.append(f"$C_{{{i+1}{j+1}}} = {terms_sum} = {format_number(res[i, j])}$")

    latex_eq = f"C = A \\times B = {matrix_to_latex(mat_a)} \\times {matrix_to_latex(mat_b)} = {matrix_to_latex(res)}"

    return {
        "success": True,
        "operation": "Matrix Multiplication",
        "input_a": matrix_to_list(mat_a),
        "input_b": matrix_to_list(mat_b),
        "result": matrix_to_list(res),
        "latex_result": latex_eq,
        "steps": steps,
        "explanation": "Matrix multiplication computes dot products of rows of Matrix A with columns of Matrix B.",
        "time_complexity": f"O({r1} \\times {c1} \\times {c2})"
    }


def scalar_multiplication(mat_a: np.ndarray, scalar: float, show_steps: bool = True) -> Dict[str, Any]:
    res = scalar * mat_a
    r, c = mat_a.shape

    steps = []
    if show_steps:
        steps.append(f"#### Step-by-Step Scalar Multiplication by $c = {format_number(scalar)}$:")
        steps.append("Formula: $C_{ij} = c \\cdot A_{ij}$")
        for i in range(r):
            for j in range(c):
                val_a = mat_a[i, j]
                val_c = res[i, j]
                steps.append(f"$C_{{{i+1}{j+1}}} = {format_number(scalar)} \\times ({format_number(val_a)}) = {format_number(val_c)}$")

    latex_eq = f"{format_number(scalar)} \\cdot A = {format_number(scalar)} \\cdot {matrix_to_latex(mat_a)} = {matrix_to_latex(res)}"

    return {
        "success": True,
        "operation": "Scalar Multiplication",
        "input_a": matrix_to_list(mat_a),
        "scalar": scalar,
        "result": matrix_to_list(res),
        "latex_result": latex_eq,
        "steps": steps,
        "explanation": "Scalar multiplication multiplies every single element of the matrix by the scalar constant.",
        "time_complexity": f"O({r} \\times {c})"
    }


def matrix_transpose(mat_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    res = mat_a.T
    r, c = mat_a.shape

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Transposition:")
        steps.append(f"Original dimension: ${r} \\times {c}$. Transposed dimension: ${c} \\times {r}$.")
        steps.append("Row $i$ of Matrix A becomes Column $i$ of Matrix $A^T$ ($A^T_{ij} = A_{ji}$).")

    latex_eq = f"A^T = {matrix_to_latex(mat_a)}^T = {matrix_to_latex(res)}"

    return {
        "success": True,
        "operation": "Matrix Transpose",
        "input_a": matrix_to_list(mat_a),
        "result": matrix_to_list(res),
        "latex_result": latex_eq,
        "steps": steps,
        "explanation": "Transposition flips a matrix over its diagonal, switching row and column indices.",
        "time_complexity": f"O({r} \\times {c})"
    }


def matrix_trace(mat_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    err = validate_square_matrix(mat_a)
    if err:
        return {"success": False, "error": err}

    n = mat_a.shape[0]
    diag_elements = [mat_a[i, i] for i in range(n)]
    trace_val = float(np.trace(mat_a))

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Trace Calculation:")
        steps.append(f"Matrix is square (${n} \\times {n}$). Trace is the sum of main diagonal elements: $a_{{11}} + a_{{22}} + \\dots + a_{{{n}{n}}}$")
        diag_str = " + ".join([f"({format_number(x)})" for x in diag_elements])
        steps.append(f"$\\text{{Trace}}(A) = {diag_str} = {format_number(trace_val)}$")

    return {
        "success": True,
        "operation": "Matrix Trace",
        "input_a": matrix_to_list(mat_a),
        "result": round(trace_val, 4),
        "diagonal_elements": [round(float(x), 4) for x in diag_elements],
        "latex_result": f"\\text{{Trace}}(A) = {format_number(trace_val)}",
        "steps": steps,
        "explanation": "The trace of a square matrix is the sum of elements along its main diagonal.",
        "time_complexity": f"O({n})"
    }


def matrix_rank(mat_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    r, c = mat_a.shape
    rank_val = int(np.linalg.matrix_rank(mat_a))

    # SymPy Row Echelon Form to explain dependency
    sp_mat = sp.Matrix(mat_a)
    rref_mat, pivot_cols = sp_mat.rref()

    steps = []
    reasoning = ""
    if show_steps:
        steps.append("#### Step-by-Step Rank Analysis:")
        steps.append(f"Matrix dimensions: ${r} \\times {c}$. Maximum possible rank is $\\min({r}, {c}) = {min(r, c)}$.")
        steps.append(f"Row Reduction to Echelon Form yields {len(pivot_cols)} non-zero pivot columns at indices: {list(pivot_cols)}.")
        steps.append(f"$$\\text{{RREF}}(A) = {sp.latex(rref_mat)}$$")

    if rank_val == min(r, c):
        reasoning = f"The matrix has full rank ({rank_val}) because all rows and columns are linearly independent."
    else:
        dependent_count = min(r, c) - rank_val
        reasoning = f"Rank = {rank_val}. {dependent_count} row(s)/column(s) are linearly dependent on other rows."

    return {
        "success": True,
        "operation": "Matrix Rank",
        "input_a": matrix_to_list(mat_a),
        "result": rank_val,
        "reasoning": reasoning,
        "latex_result": f"\\text{{Rank}}(A) = {rank_val}",
        "steps": steps,
        "explanation": f"The rank of a matrix is the maximum number of linearly independent row or column vectors. {reasoning}",
        "time_complexity": f"O({r} \\times {c}^2)"
    }


def matrix_determinant(mat_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    err = validate_square_matrix(mat_a)
    if err:
        return {"success": False, "error": err}

    n = mat_a.shape[0]
    det_val = float(np.linalg.det(mat_a))

    steps = []
    if show_steps:
        steps.append(f"#### Step-by-Step Determinant Expansion ({n}x{n}):")
        if n == 2:
            a, b = mat_a[0, 0], mat_a[0, 1]
            c, d = mat_a[1, 0], mat_a[1, 1]
            steps.append(f"Formula for $2 \\times 2$: $\\det = ad - bc$")
            steps.append(f"$\\det(A) = ({format_number(a)} \\times {format_number(d)}) - ({format_number(b)} \\times {format_number(c)}) = {format_number(det_val)}$")
        elif n == 3:
            steps.append("Cofactor expansion along Row 1:")
            a11, a12, a13 = mat_a[0, 0], mat_a[0, 1], mat_a[0, 2]
            m11 = mat_a[1:, [1, 2]]
            m12 = mat_a[1:, [0, 2]]
            m13 = mat_a[1:, [0, 1]]

            det11 = float(np.linalg.det(m11))
            det12 = float(np.linalg.det(m12))
            det13 = float(np.linalg.det(m13))

            steps.append(f"$\\det(A) = ({format_number(a11)}) \\det{matrix_to_latex(m11)} - ({format_number(a12)}) \\det{matrix_to_latex(m12)} + ({format_number(a13)}) \\det{matrix_to_latex(m13)}$")
            steps.append(f"$\\det(A) = ({format_number(a11)})({format_number(det11)}) - ({format_number(a12)})({format_number(det12)}) + ({format_number(a13)})({format_number(det13)}) = {format_number(det_val)}$")
        else:
            steps.append(f"Evaluated using LU/Gaussian Pivot Reduction for size ${n} \\times {n}$.")
            steps.append(f"$$\\det(A) = {format_number(det_val)}$$")

    return {
        "success": True,
        "operation": "Matrix Determinant",
        "input_a": matrix_to_list(mat_a),
        "result": round(det_val, 4),
        "latex_result": f"\\det(A) = {format_number(det_val)}",
        "steps": steps,
        "explanation": f"The determinant scaling factor of volume under matrix linear transformation. Here det(A) = {format_number(det_val)}.",
        "time_complexity": f"O({n}^3)"
    }


def matrix_inverse(mat_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    is_inv, det_val, err = validate_invertible_matrix(mat_a)
    if not is_inv:
        return {"success": False, "error": err, "explanation": "Matrix is singular (det = 0) and has no inverse."}

    inv_mat = np.linalg.inv(mat_a)
    n = mat_a.shape[0]

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Matrix Inversion:")
        steps.append(f"1. Check determinant: $\\det(A) = {format_number(det_val)} \\neq 0$. Matrix is non-singular and invertible.")
        steps.append("2. Compute Adjugate Matrix and divide by determinant: $A^{-1} = \\frac{1}{\\det(A)} \\text{adj}(A)$")
        sp_mat = sp.Matrix(mat_a)
        adj_mat = sp_mat.adjugate()
        steps.append(f"$$\\text{{adj}}(A) = {sp.latex(adj_mat)}$$")
        steps.append(f"$$A^{{-1}} = {matrix_to_latex(inv_mat)}$$")

    latex_eq = f"A^{{-1}} = {matrix_to_latex(inv_mat)}"

    return {
        "success": True,
        "operation": "Matrix Inverse",
        "input_a": matrix_to_list(mat_a),
        "result": matrix_to_list(inv_mat),
        "determinant": round(det_val, 4),
        "latex_result": latex_eq,
        "steps": steps,
        "explanation": "The matrix inverse satisfy A * A^(-1) = I. Exists only for square non-singular matrices.",
        "time_complexity": f"O({n}^3)"
    }
