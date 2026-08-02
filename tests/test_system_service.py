import pytest
import numpy as np
from services import system_service

def test_gaussian_elimination_unique():
    A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], dtype=float)
    b = np.array([8, -11, -3], dtype=float)
    res = system_service.solve_gaussian_elimination(A, b)
    assert res['success']
    assert res['solution_type'] == 'Unique Solution'
    assert np.allclose(res['solution'], [2, 3, -1], atol=1e-3)

def test_gauss_jordan_unique():
    A = np.array([[1, 1], [1, -1]], dtype=float)
    b = np.array([4, 2], dtype=float)
    res = system_service.solve_gauss_jordan(A, b)
    assert res['success']
    assert res['solution'] == [3.0, 1.0]

def test_cramer_rule_unique():
    A = np.array([[3, 2], [1, -1]], dtype=float)
    b = np.array([7, 4], dtype=float)
    res = system_service.solve_cramers_rule(A, b)
    assert res['success']
    assert np.allclose(res['solution'], [3, -1], atol=1e-3)
