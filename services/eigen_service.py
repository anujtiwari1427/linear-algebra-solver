import numpy as np
import sympy as sp
from typing import Dict, Any, List, Optional
from services.validation_service import validate_square_matrix
from services.matrix_service import format_number, matrix_to_latex, matrix_to_list

def compute_eigen_analysis(mat_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    err = validate_square_matrix(mat_a)
    if err:
        return {"success": False, "error": err}

    n = mat_a.shape[0]
    sp_a = sp.Matrix(mat_a)
    lam = sp.Symbol('\\lambda')

    # Characteristic polynomial P(lambda) = det(A - lambda I)
    char_poly = sp_a.charpoly(lam)
    char_poly_expr = char_poly.as_expr()

    # NumPy numerical eigenvalues & eigenvectors
    evals, evecs = np.linalg.eig(mat_a)

    steps = []
    if show_steps:
        steps.append(f"#### Step-by-Step Eigenvalue & Eigenvector Derivation ({n}x{n}):")
        steps.append("1. Formulate characteristic polynomial $\\det(A - \\lambda I) = 0$:")
        steps.append(f"$$P(\\lambda) = {sp.latex(char_poly_expr)} = 0$$")
        steps.append("2. Solve roots of characteristic equation for eigenvalues $\\lambda_i$:")

        for i, val in enumerate(evals):
            val_str = f"{val.real:.4f}" if np.isreal(val) else f"{val.real:.4f} + {val.imag:.4f}i"
            steps.append(f"$\\lambda_{{{i+1}}} = {val_str}$")

        steps.append("3. Solve $(A - \\lambda_i I) \\vec{v}_i = \\mathbf{0}$ for corresponding eigenvectors $\\vec{v}_i$:")

    # SymPy symbolic eigenspaces
    eigenspaces = []
    try:
        sym_eigen = sp_a.eigenvects()
        for i, (val, mult, vecs) in enumerate(sym_eigen):
            vec_strs = [sp.latex(v) for v in vecs]
            eigenspaces.append({
                "eigenvalue": sp.latex(val),
                "multiplicity": mult,
                "eigenvectors": vec_strs
            })
            if show_steps:
                steps.append(f"Eigenvalue $\\lambda = {sp.latex(val)}$ (Multiplicity {mult}): Eigenbasis $v = {', '.join(vec_strs)}$")
    except Exception as e:
        steps.append(f"Symbolic eigenspace note: {e}")

    # Numerical result arrays
    evals_list = [round(float(x.real), 4) if np.isreal(x) else f"{x.real:.4f}+{x.imag:.4f}j" for x in evals]
    evecs_list = matrix_to_list(np.real(evecs))

    return {
        "success": True,
        "operation": "Eigenvalues & Eigenvectors",
        "input_a": matrix_to_list(mat_a),
        "characteristic_polynomial": sp.latex(char_poly_expr),
        "eigenvalues": evals_list,
        "eigenvectors": evecs_list,
        "eigenspaces": eigenspaces,
        "latex_result": f"P(\\lambda) = {sp.latex(char_poly_expr)}",
        "steps": steps,
        "explanation": "Eigenvalues scale eigenvectors under linear matrix transformations without changing their directional line.",
        "time_complexity": f"O({n}^3)"
    }


def compute_diagonalization(mat_a: np.ndarray, k_exp: int = 5, show_steps: bool = True) -> Dict[str, Any]:
    err = validate_square_matrix(mat_a)
    if err:
        return {"success": False, "error": err}

    n = mat_a.shape[0]
    sp_a = sp.Matrix(mat_a)

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Matrix Diagonalization $A = P D P^{-1}$:")

    try:
        if sp_a.is_diagonalizable():
            P, D = sp_a.diagonalize()
            P_inv = P.inv()
            
            D_k = D**k_exp
            A_k = P * D_k * P_inv

            if show_steps:
                steps.append("Matrix A is **Diagonalizable** (has $n$ linearly independent eigenvectors).")
                steps.append(f"Modal Matrix $P$ (columns are eigenvectors): $$P = {sp.latex(P)}$$")
                steps.append(f"Diagonal Matrix $D$ (eigenvalues on main diagonal): $$D = {sp.latex(D)}$$")
                steps.append(f"Compute matrix power $A^{{{k_exp}}} = P \\cdot D^{{{k_exp}}} \\cdot P^{{-1}}$:")
                steps.append(f"$$A^{{{k_exp}}} = {sp.latex(A_k)}$$")

            return {
                "success": True,
                "is_diagonalizable": True,
                "modal_matrix_P": sp.latex(P),
                "diagonal_matrix_D": sp.latex(D),
                "matrix_power_Ak": sp.latex(A_k),
                "exponent_k": k_exp,
                "latex_result": f"A = P D P^{{-1}}, \\quad A^{{{k_exp}}} = {sp.latex(A_k)}",
                "steps": steps,
                "explanation": "Diagonalization simplifies matrix powers A^k to diagonal element powers D^k.",
                "time_complexity": f"O({n}^3)"
            }
        else:
            return {
                "success": True,
                "is_diagonalizable": False,
                "explanation": "Matrix is defective (not diagonalizable) because it lacks n linearly independent eigenvectors.",
                "steps": steps + ["Matrix is **defective** (total independent eigenvectors < n)."]
            }
    except Exception as e:
        return {"success": False, "error": f"Diagonalization evaluation error: {e}"}


def compute_cayley_hamilton(mat_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    err = validate_square_matrix(mat_a)
    if err:
        return {"success": False, "error": err}

    n = mat_a.shape[0]
    sp_a = sp.Matrix(mat_a)
    lam = sp.Symbol('\\lambda')
    char_poly = sp_a.charpoly(lam)
    coeffs = char_poly.all_coeffs()

    pa_mat = sp.zeros(n, n)
    degree = len(coeffs) - 1
    for idx, c in enumerate(coeffs):
        power = degree - idx
        pa_mat += c * (sp_a**power)

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Cayley-Hamilton Verification:")
        steps.append("The **Cayley-Hamilton Theorem** states every square matrix $A$ satisfies its own characteristic equation: $P(A) = \\mathbf{0}$.")
        steps.append(f"Characteristic polynomial: $$P(\\lambda) = {sp.latex(char_poly.as_expr())}$$")
        steps.append(f"Substitute matrix A into polynomial expression $P(A)$:")
        steps.append(f"$$P(A) = {sp.latex(pa_mat)}$$")

    is_verified = (pa_mat == sp.zeros(n, n))

    return {
        "success": True,
        "operation": "Cayley-Hamilton Theorem",
        "verified": is_verified,
        "characteristic_poly": sp.latex(char_poly.as_expr()),
        "result_matrix": sp.latex(pa_mat),
        "latex_result": f"P(A) = {sp.latex(pa_mat)} = \\mathbf{{0}}",
        "steps": steps,
        "explanation": "Cayley-Hamilton Theorem proves that evaluating P(A) yields the zero matrix.",
        "time_complexity": f"O({n}^4)"
    }
