from flask import Blueprint, request, jsonify
from services.validation_service import sanitize_and_parse_matrix, sanitize_and_parse_vector
from services import system_service

system_api = Blueprint('api_system', __name__, url_prefix='/api/system')

@system_api.route('/gaussian', methods=['POST'])
def gaussian():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Coefficient Matrix A error: {err_a}"}), 400

    vec_b, err_b = sanitize_and_parse_vector(data.get('vector_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Constants Vector b error: {err_b}"}), 400

    res = system_service.solve_gaussian_elimination(mat_a, vec_b, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@system_api.route('/gauss_jordan', methods=['POST'])
def gauss_jordan():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Coefficient Matrix A error: {err_a}"}), 400

    vec_b, err_b = sanitize_and_parse_vector(data.get('vector_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Constants Vector b error: {err_b}"}), 400

    res = system_service.solve_gauss_jordan(mat_a, vec_b, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@system_api.route('/lu_method', methods=['POST'])
def lu_method():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Coefficient Matrix A error: {err_a}"}), 400

    vec_b, err_b = sanitize_and_parse_vector(data.get('vector_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Constants Vector b error: {err_b}"}), 400

    res = system_service.solve_lu_method(mat_a, vec_b, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@system_api.route('/cramer', methods=['POST'])
def cramer():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Coefficient Matrix A error: {err_a}"}), 400

    vec_b, err_b = sanitize_and_parse_vector(data.get('vector_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Constants Vector b error: {err_b}"}), 400

    res = system_service.solve_cramers_rule(mat_a, vec_b, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code
