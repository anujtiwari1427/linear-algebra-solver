from flask import Blueprint, request, jsonify
from services.validation_service import sanitize_and_parse_matrix
from services import matrix_service

matrix_api = Blueprint('api_matrix', __name__, url_prefix='/api/matrix')

@matrix_api.route('/addition', methods=['POST'])
@matrix_api.route('/add', methods=['POST'])
def addition():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    mat_b, err_b = sanitize_and_parse_matrix(data.get('matrix_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Matrix B error: {err_b}"}), 400

    res = matrix_service.matrix_addition(mat_a, mat_b, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@matrix_api.route('/subtraction', methods=['POST'])
@matrix_api.route('/subtract', methods=['POST'])
def subtraction():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    mat_b, err_b = sanitize_and_parse_matrix(data.get('matrix_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Matrix B error: {err_b}"}), 400

    res = matrix_service.matrix_subtraction(mat_a, mat_b, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@matrix_api.route('/multiplication', methods=['POST'])
@matrix_api.route('/multiply', methods=['POST'])
def multiplication():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    mat_b, err_b = sanitize_and_parse_matrix(data.get('matrix_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Matrix B error: {err_b}"}), 400

    res = matrix_service.matrix_multiplication(mat_a, mat_b, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@matrix_api.route('/scalar', methods=['POST'])
def scalar():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)
    scalar_val = float(data.get('scalar', 1.0))

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = matrix_service.scalar_multiplication(mat_a, scalar_val, show_steps=show_steps)
    return jsonify(res), 200


@matrix_api.route('/transpose', methods=['POST'])
def transpose():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = matrix_service.matrix_transpose(mat_a, show_steps=show_steps)
    return jsonify(res), 200


@matrix_api.route('/trace', methods=['POST'])
def trace():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = matrix_service.matrix_trace(mat_a, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@matrix_api.route('/rank', methods=['POST'])
def rank():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = matrix_service.matrix_rank(mat_a, show_steps=show_steps)
    return jsonify(res), 200


@matrix_api.route('/determinant', methods=['POST'])
def determinant():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = matrix_service.matrix_determinant(mat_a, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@matrix_api.route('/inverse', methods=['POST'])
def inverse():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = matrix_service.matrix_inverse(mat_a, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code
