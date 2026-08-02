import numpy as np
import scipy.linalg as la
from typing import Dict, Any
from services.validation_service import validate_square_matrix
from services.matrix_service import format_number, matrix_to_latex, matrix_to_list

def compute_lu_decomposition(mat_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    err = validate_square_matrix(mat_a)
    if err:
        return {"success": False, "error": err}

    n = mat_a.shape[0]
    P, L, U = la.lu(mat_a)

    steps = []
    if show_steps:
        steps.append(f"#### Step-by-Step LU Decomposition ($P \\cdot L \\cdot U = A$):")
        steps.append(f"Decomposes square matrix $A$ (${n} \\times {n}$) into Permutation $P$, Lower triangular $L$, and Upper triangular $U$.")
        steps.append(f"Permutation Matrix P: $$P = {matrix_to_latex(P)}$$")
        steps.append(f"Lower Triangular Matrix L: $$L = {matrix_to_latex(L)}$$")
        steps.append(f"Upper Triangular Matrix U: $$U = {matrix_to_latex(U)}$$")
        steps.append("Verification check: $P \\cdot L \\cdot U = A$")

    return {
        "success": True,
        "operation": "LU Decomposition",
        "P": matrix_to_list(P),
        "L": matrix_to_list(L),
        "U": matrix_to_list(U),
        "latex_result": f"A = P \\cdot L \\cdot U = {matrix_to_latex(P)} {matrix_to_latex(L)} {matrix_to_latex(U)}",
        "steps": steps,
        "explanation": "LU decomposition factors matrix A into lower and upper triangular matrices, accelerating linear system solving and determinant calculation.",
        "time_complexity": f"O({n}^3)"
    }


def compute_qr_decomposition(mat_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    r, c = mat_a.shape
    Q, R = np.linalg.qr(mat_a)

    steps = []
    if show_steps:
        steps.append(f"#### Step-by-Step QR Decomposition ($Q \\cdot R = A$):")
        steps.append(f"Decomposes matrix $A$ (${r} \\times {c}$) into Orthogonal matrix $Q$ and Upper triangular matrix $R$.")
        steps.append(f"Orthogonal Matrix Q ($Q^T Q = I$): $$Q = {matrix_to_latex(Q)}$$")
        steps.append(f"Upper Triangular Matrix R: $$R = {matrix_to_latex(R)}$$")
        steps.append("Verification check: $Q \\cdot R = A$")

    return {
        "success": True,
        "operation": "QR Decomposition",
        "Q": matrix_to_list(Q),
        "R": matrix_to_list(R),
        "latex_result": f"A = Q \\cdot R = {matrix_to_latex(Q)} {matrix_to_latex(R)}",
        "steps": steps,
        "explanation": "QR decomposition factorizes matrix A using Gram-Schmidt orthogonalization into orthogonal Q and upper triangular R.",
        "time_complexity": f"O({r} \\times {c}^2)"
    }


def compute_svd_decomposition(mat_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    r, c = mat_a.shape
    U, S, Vt = np.linalg.svd(mat_a)

    steps = []
    if show_steps:
        steps.append(f"#### Step-by-Step Singular Value Decomposition ($U \\cdot \\Sigma \\cdot V^T$):")
        steps.append(f"Decomposes matrix $A$ (${r} \\times {c}$) into Left singular vectors $U$, Singular values diagonal $\\Sigma$, and Right singular vectors $V^T$.")
        steps.append(f"Left Singular Matrix U (${r} \\times {r}$): $$U = {matrix_to_latex(U)}$$")
        s_formatted = ", ".join([format_number(x) for x in S])
        steps.append(f"Singular Values $\\Sigma = [\\sigma_1, \\sigma_2, \\dots] = [{s_formatted}]$")
        steps.append(f"Right Singular Matrix $V^T$ (${c} \\times {c}$): $$V^T = {matrix_to_latex(Vt)}$$")

    return {
        "success": True,
        "operation": "Singular Value Decomposition (SVD)",
        "U": matrix_to_list(U),
        "S": [round(float(x), 4) for x in S],
        "Vt": matrix_to_list(Vt),
        "latex_result": f"A = U \\Sigma V^T, \\quad \\Sigma = \\text{{diag}}({', '.join([format_number(x) for x in S])})",
        "steps": steps,
        "explanation": "SVD decomposes any real matrix into unitary rotation matrices and positive singular values. Essential for principal component analysis (PCA) and data compression.",
        "time_complexity": f"O({min(r,c)} \\times {max(r,c)}^2)"
    }


def compute_cholesky_decomposition(mat_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    err = validate_square_matrix(mat_a)
    if err:
        return {"success": False, "error": err}

    if not np.allclose(mat_a, mat_a.T):
        return {"success": False, "error": "Cholesky decomposition requires a Symmetric matrix (A = A^T)."}

    try:
        L = np.linalg.cholesky(mat_a)
    except np.linalg.LinAlgError:
        return {"success": False, "error": "Matrix A is not Positive Definite (all eigenvalues must be strictly > 0)."}

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Cholesky Decomposition ($L \\cdot L^T = A$):")
        steps.append("Factorizes Symmetric Positive Definite matrix $A$ into Lower Triangular matrix $L$ and its transpose $L^T$.")
        steps.append(f"Lower Triangular L: $$L = {matrix_to_latex(L)}$$")
        steps.append(f"Transpose $L^T$: $$L^T = {matrix_to_latex(L.T)}$$")

    return {
        "success": True,
        "operation": "Cholesky Decomposition",
        "L": matrix_to_list(L),
        "Lt": matrix_to_list(L.T),
        "latex_result": f"A = L L^T = {matrix_to_latex(L)} {matrix_to_latex(L.T)}",
        "steps": steps,
        "explanation": "Cholesky decomposition is twice as fast as LU decomposition for symmetric positive definite matrices.",
        "time_complexity": f"O({mat_a.shape[0]}^3 / 3)"
    }
