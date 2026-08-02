import numpy as np
import sympy as sp
from typing import Dict, Any
from services.validation_service import validate_square_matrix, validate_non_zero_vector
from services.matrix_service import format_number, matrix_to_latex, matrix_to_list

def compute_gf2_operations(mat_a: np.ndarray, vec_b: Optional[np.ndarray] = None, operation: str = "rank", show_steps: bool = True) -> Dict[str, Any]:
    # Modulo 2 integer conversion
    mat_mod2 = (np.round(mat_a).astype(int) % 2)
    r, c = mat_mod2.shape

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step GF(2) Galois Field Operations:")
        steps.append("GF(2) consists of elements {0, 1} where Addition is XOR ($1+1=0$) and Multiplication is AND.")
        steps.append(f"Matrix A in GF(2): $$A_{{\\text{{GF(2)}}}} = {matrix_to_latex(mat_mod2)}$$")

    if operation == "power":
        if r != c:
            return {"success": False, "error": f"Matrix power in GF(2) requires square matrix. Got {r}x{c}."}
        res = (mat_mod2 @ mat_mod2) % 2
        if show_steps:
            steps.append(f"Compute $A^2 \\pmod 2$: $$A^2 = {matrix_to_latex(res)}$$")
        return {
            "success": True,
            "operation": "GF(2) Matrix Power (A^2)",
            "result": res.tolist(),
            "latex_result": f"A^2 \\pmod 2 = {matrix_to_latex(res)}",
            "steps": steps,
            "explanation": "GF(2) matrix multiplication performs binary vector dot products modulo 2.",
            "time_complexity": f"O({r}^3)"
        }

    elif operation == "rank":
        sp_mat = sp.Matrix(mat_mod2)
        rank_val = sp_mat.rank()
        if show_steps:
            steps.append(f"Row echelon reduction over GF(2) yields Rank = {rank_val}.")
        return {
            "success": True,
            "operation": "GF(2) Matrix Rank",
            "rank": rank_val,
            "latex_result": f"\\text{{Rank}}_{{\\text{{GF(2)}}}}(A) = {rank_val}",
            "steps": steps,
            "explanation": "GF(2) rank measures binary linear independence of row vectors.",
            "time_complexity": f"O({r} \\times {c}^2)"
        }

    elif operation == "solve":
        if vec_b is None:
            return {"success": False, "error": "Vector b is required to solve Ax = b in GF(2)."}
        vec_mod2 = (np.round(vec_b).astype(int) % 2)
        aug = np.hstack([mat_mod2, vec_mod2.reshape(-1, 1)])
        sp_aug = sp.Matrix(aug)
        rref_mat, pivots = sp_aug.rref()
        rref_mod2 = np.array([[elem % 2 for elem in row] for row in rref_mat.tolist()])

        if show_steps:
            steps.append(f"Augmented Matrix $[A \\mid b]_{{\\text{{GF(2)}}}} = {matrix_to_latex(aug)}$")
            steps.append(f"$$\\text{{RREF}}([A \\mid b]) \\pmod 2 = {matrix_to_latex(rref_mod2)}$$")

        return {
            "success": True,
            "operation": "Solve Ax = b in GF(2)",
            "result": rref_mod2.tolist(),
            "latex_result": f"\\text{{RREF}}([A \\mid b]) = {matrix_to_latex(rref_mod2)}",
            "steps": steps,
            "explanation": "Solves binary linear equations over Galois Field 2.",
            "time_complexity": f"O({r}^3)"
        }

    return {"success": False, "error": f"Unknown GF(2) operation '{operation}'."}


def compute_change_of_basis(mat_b: np.ndarray, mat_b_prime: np.ndarray, mat_t_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    err_b = validate_square_matrix(mat_b)
    if err_b:
        return {"success": False, "error": f"Old basis B: {err_b}"}

    err_bp = validate_square_matrix(mat_b_prime)
    if err_bp:
        return {"success": False, "error": f"New basis B': {err_bp}"}

    det_b = float(np.linalg.det(mat_b))
    det_bp = float(np.linalg.det(mat_b_prime))

    if abs(det_b) < 1e-7 or abs(det_bp) < 1e-7:
        return {"success": False, "error": "Bases B and B' must consist of linearly independent vectors (det != 0)."}

    # Transition matrix P_{B -> B'} = (B')^{-1} * B
    P_mat = np.linalg.inv(mat_b_prime) @ mat_b
    P_inv = np.linalg.inv(P_mat)
    mat_t_b_prime = P_inv @ mat_t_b @ P_mat

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Change of Basis Transformation:")
        steps.append("1. Transition matrix formula: $P_{B \\to B'} = (B')^{-1} B$")
        steps.append(f"$$P_{{B \\to B'}} = {matrix_to_latex(P_mat)}$$")
        steps.append("2. Similar Transformation Matrix Formula: $[T]_{B'} = P^{-1} [T]_B P$")
        steps.append(f"$$[T]_{{B'}} = {matrix_to_latex(mat_t_b_prime)}$$")

    return {
        "success": True,
        "operation": "Change of Basis",
        "transition_matrix_P": matrix_to_list(P_mat),
        "transformed_matrix_T_prime": matrix_to_list(mat_t_b_prime),
        "latex_result": f"[T]_{{B'}} = {matrix_to_latex(mat_t_b_prime)}",
        "steps": steps,
        "explanation": "Change of basis maps linear transformations between different coordinate bases while preserving eigenvalues.",
        "time_complexity": f"O({mat_b.shape[0]}^3)"
    }


def compute_weighted_inner_product(vec_u: np.ndarray, vec_v: np.ndarray, mat_w: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    if vec_u.size != vec_v.size:
        return {"success": False, "error": f"Vector dimension mismatch ({vec_u.size} vs {vec_v.size})."}

    n = vec_u.size
    err_w = validate_square_matrix(mat_w)
    if err_w or mat_w.shape[0] != n:
        return {"success": False, "error": f"Weight matrix W must be a square {n}x{n} matrix."}

    if not np.allclose(mat_w, mat_w.T) or np.any(np.linalg.eigvals(mat_w) <= 0):
        return {"success": False, "error": "Weight matrix W must be Symmetric Positive Definite for a valid inner product!"}

    inner_uv = float(vec_u.T @ mat_w @ vec_v)
    norm_u_w = float(np.sqrt(vec_u.T @ mat_w @ vec_u))
    norm_v_w = float(np.sqrt(vec_v.T @ mat_w @ vec_v))

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Weighted Inner Product Calculation:")
        steps.append("Formula: $\\langle \\vec{u}, \\vec{v} \\rangle_W = \\vec{u}^T W \\vec{v}$")
        steps.append(f"1. Weighted Inner Product $\\langle \\vec{{u}}, \\vec{{v}} \\rangle_W = {format_number(inner_uv)}$")
        steps.append(f"2. Weighted Norm $\\|\\vec{{u}}\\|_W = \\sqrt{{\\vec{{u}}^T W \\vec{{u}}}} = {format_number(norm_u_w)}$")
        steps.append(f"3. Weighted Norm $\\|\\vec{{v}}\\|_W = \\sqrt{{\\vec{{v}}^T W \\vec{{v}}}} = {format_number(norm_v_w)}$")

    return {
        "success": True,
        "operation": "Weighted Inner Product",
        "inner_product": round(inner_uv, 4),
        "norm_u_w": round(norm_u_w, 4),
        "norm_v_w": round(norm_v_w, 4),
        "latex_result": f"\\langle \\vec{{u}}, \\vec{{v}} \\rangle_W = {format_number(inner_uv)}",
        "steps": steps,
        "explanation": "General inner products generalize dot products using symmetric positive-definite metric weighting matrices W.",
        "time_complexity": f"O({n}^2)"
    }
