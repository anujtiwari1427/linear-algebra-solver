"""
Minimal polynomial of a matrix computed via Jordan Normal Form.
Works with SymPy Matrix (symbolic or integer entries).
"""
import sympy as sp


def matrix_minimal_poly(sp_mat: sp.Matrix, lam: sp.Symbol) -> sp.Expr:
    """
    Return the minimal polynomial of *sp_mat* as a SymPy expression in *lam*.

    Algorithm:
        For each distinct eigenvalue λᵢ, find the largest Jordan block size kᵢ.
        The minimal polynomial is  m(λ) = ∏ (λ - λᵢ)^kᵢ

    Raises ValueError if Jordan form cannot be computed.
    """
    n = sp_mat.shape[0]
    try:
        _, J = sp_mat.jordan_form()
    except Exception as exc:
        raise ValueError(f"Jordan form failed: {exc}") from exc

    # Walk through Jordan blocks and track max block size per eigenvalue
    eigen_max_block: dict = {}
    i = 0
    while i < n:
        val = J[i, i]
        block_size = 1
        while i + block_size < n and J[i + block_size - 1, i + block_size] == 1:
            block_size += 1
        key = val
        if key not in eigen_max_block or block_size > eigen_max_block[key]:
            eigen_max_block[key] = block_size
        i += block_size

    min_poly = sp.Integer(1)
    for val, size in eigen_max_block.items():
        min_poly *= (lam - val) ** size

    return sp.expand(min_poly)
