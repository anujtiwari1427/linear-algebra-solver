import numpy as np
from typing import Tuple, Optional, Dict, Any, Union

def sanitize_and_parse_matrix(data: Any, rows: Optional[int] = None, cols: Optional[int] = None) -> Tuple[Optional[np.ndarray], Optional[str]]:
    """
    Validates and converts input data into a 2D float NumPy array.
    Checks for empty inputs, invalid types, NaN, Infinity, and shape constraints.
    """
    if data is None:
        return None, "Matrix data cannot be empty."

    try:
        arr = np.array(data, dtype=float)
    except (ValueError, TypeError):
        return None, "Matrix contains non-numeric values or invalid data structures."

    if arr.size == 0:
        return None, "Matrix cannot be empty."

    if arr.ndim == 1:
        # Reshape 1D vector to 2D row or col matrix if requested
        if rows is not None and cols is not None:
            if arr.size == rows * cols:
                arr = arr.reshape((rows, cols))
            else:
                return None, f"Expected matrix of size {rows}x{cols}, but got total {arr.size} elements."
        else:
            arr = arr.reshape(1, -1)
    elif arr.ndim != 2:
        return None, "Matrix must be a 2D array."

    if np.isnan(arr).any():
        return None, "Matrix contains NaN (Not a Number) values."

    if np.isinf(arr).any():
        return None, "Matrix contains Infinite (Inf) values."

    if rows is not None and arr.shape[0] != rows:
        return None, f"Expected {rows} rows, but received {arr.shape[0]} rows."

    if cols is not None and arr.shape[1] != cols:
        return None, f"Expected {cols} columns, but received {arr.shape[1]} columns."

    return arr, None


def sanitize_and_parse_vector(data: Any, expected_dim: Optional[int] = None) -> Tuple[Optional[np.ndarray], Optional[str]]:
    """
    Validates and converts input data into a 1D float NumPy vector.
    """
    if data is None:
        return None, "Vector data cannot be empty."

    try:
        vec = np.array(data, dtype=float).flatten()
    except (ValueError, TypeError):
        return None, "Vector contains non-numeric values."

    if vec.size == 0:
        return None, "Vector cannot be empty."

    if np.isnan(vec).any():
        return None, "Vector contains NaN (Not a Number) values."

    if np.isinf(vec).any():
        return None, "Vector contains Infinite (Inf) values."

    if expected_dim is not None and vec.size != expected_dim:
        return None, f"Expected vector of dimension {expected_dim}, but got dimension {vec.size}."

    return vec, None


def validate_square_matrix(mat: np.ndarray) -> Optional[str]:
    """Ensures the matrix is square (N x N)."""
    r, c = mat.shape
    if r != c:
        return f"Operation requires a square matrix, but got matrix of dimension {r}x{c}."
    return None


def validate_addition_dimensions(mat_a: np.ndarray, mat_b: np.ndarray) -> Optional[str]:
    """Ensures matrices A and B have identical dimensions for addition/subtraction."""
    if mat_a.shape != mat_b.shape:
        return f"Dimension mismatch: Matrix A is {mat_a.shape[0]}x{mat_a.shape[1]} while Matrix B is {mat_b.shape[0]}x{mat_b.shape[1]}. Addition/subtraction requires identical dimensions."
    return None


def validate_multiplication_dimensions(mat_a: np.ndarray, mat_b: np.ndarray) -> Optional[str]:
    """Ensures columns of A equal rows of B for matrix multiplication A x B."""
    if mat_a.shape[1] != mat_b.shape[0]:
        return f"Dimension mismatch: Columns of Matrix A ({mat_a.shape[1]}) must equal Rows of Matrix B ({mat_b.shape[0]}). Cannot multiply {mat_a.shape[0]}x{mat_a.shape[1]} by {mat_b.shape[0]}x{mat_b.shape[1]}."
    return None


def validate_non_zero_vector(vec: np.ndarray, vector_name: str = "Vector") -> Optional[str]:
    """Ensures the vector norm is greater than zero to prevent division by zero."""
    norm = np.linalg.norm(vec)
    if norm < 1e-12:
        return f"{vector_name} cannot be a zero vector (magnitude is zero)."
    return None


def validate_invertible_matrix(mat: np.ndarray) -> Tuple[bool, float, Optional[str]]:
    """
    Checks if matrix is square and non-singular.
    Returns (is_invertible, determinant, error_message)
    """
    err = validate_square_matrix(mat)
    if err:
        return False, 0.0, err

    det = float(np.linalg.det(mat))
    if abs(det) < 1e-9:
        return False, det, "Matrix is singular (determinant is zero) and has no inverse."

    return True, det, None
