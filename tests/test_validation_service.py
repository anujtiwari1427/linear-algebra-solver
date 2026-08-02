import pytest
import numpy as np
from services import validation_service

def test_sanitize_matrix_valid():
    data = [[1, 2], [3, 4]]
    mat, err = validation_service.sanitize_and_parse_matrix(data)
    assert err is None
    assert mat.shape == (2, 2)
    assert np.array_equal(mat, np.array([[1, 2], [3, 4]]))

def test_sanitize_matrix_non_numeric():
    data = [["a", "b"], [1, 2]]
    mat, err = validation_service.sanitize_and_parse_matrix(data)
    assert mat is None
    assert "non-numeric" in err.lower()

def test_sanitize_matrix_nan():
    data = [[1, float('nan')], [3, 4]]
    mat, err = validation_service.sanitize_and_parse_matrix(data)
    assert mat is None
    assert "nan" in err.lower()

def test_validate_square_matrix():
    rect = np.zeros((2, 3))
    err = validation_service.validate_square_matrix(rect)
    assert err is not None
    assert "square matrix" in err

def test_validate_invertible_matrix():
    singular = np.array([[1, 2], [2, 4]])
    is_inv, det, err = validation_service.validate_invertible_matrix(singular)
    assert not is_inv
    assert "singular" in err.lower()
