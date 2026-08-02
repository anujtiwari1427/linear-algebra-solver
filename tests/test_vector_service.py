import pytest
import numpy as np
from services import vector_service

def test_dot_product():
    u = np.array([1, 2, 3])
    v = np.array([4, 5, 6])
    res = vector_service.vector_dot_product(u, v)
    assert res['success']
    assert res['result'] == 32.0

def test_cross_product_3d():
    u = np.array([1, 0, 0])
    v = np.array([0, 1, 0])
    res = vector_service.vector_cross_product(u, v)
    assert res['success']
    assert res['result'] == [0, 0, 1]

def test_unit_vector_zero_length():
    u = np.array([0, 0, 0])
    res = vector_service.vector_unit_vector(u)
    assert not res['success']
    assert "zero" in res['error'].lower()

def test_vector_angle():
    u = np.array([1, 0])
    v = np.array([0, 1])
    res = vector_service.vector_angle(u, v)
    assert res['success']
    assert abs(res['degrees'] - 90.0) < 1e-4
