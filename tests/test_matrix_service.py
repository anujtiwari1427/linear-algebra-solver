import pytest
import numpy as np
from services import matrix_service

def test_matrix_addition():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    res = matrix_service.matrix_addition(a, b)
    assert res['success']
    assert res['result'] == [[6, 8], [10, 12]]

def test_matrix_multiplication():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    res = matrix_service.matrix_multiplication(a, b)
    assert res['success']
    assert res['result'] == [[19, 22], [43, 50]]

def test_matrix_rank():
    # Rank 2 matrix (Row 3 dependent on Row 1)
    a = np.array([[1, 2, 3], [0, 1, 4], [2, 4, 6]])
    res = matrix_service.matrix_rank(a)
    assert res['success']
    assert res['result'] == 2

def test_matrix_determinant():
    a = np.array([[1, 2], [3, 4]])
    res = matrix_service.matrix_determinant(a)
    assert res['success']
    assert res['result'] == -2.0

def test_matrix_inverse_singular():
    a = np.array([[1, 2], [2, 4]])
    res = matrix_service.matrix_inverse(a)
    assert not res['success']
    assert "singular" in res['error'].lower()
