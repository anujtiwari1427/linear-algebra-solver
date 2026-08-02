from flask import Blueprint, request, jsonify
from services.validation_service import sanitize_and_parse_matrix, sanitize_and_parse_vector
from services import advanced_service

advanced_api = Blueprint('api_advanced', __name__, url_prefix='/api/advanced')

@advanced_api.route('/gf2', methods=['POST'])
def gf2():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)
    operation = data.get('operation', 'rank')

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    vec_b = None
    if 'vector_b' in data and data['vector_b'] is not None:
        vec_b, err_b = sanitize_and_parse_vector(data.get('vector_b'))

    res = advanced_service.compute_gf2_operations(mat_a, vec_b=vec_b, operation=operation, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@advanced_api.route('/change_of_basis', methods=['POST'])
def change_of_basis():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_b, err_b = sanitize_and_parse_matrix(data.get('basis_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Basis B error: {err_b}"}), 400

    mat_bp, err_bp = sanitize_and_parse_matrix(data.get('basis_b_prime'))
    if err_bp:
        return jsonify({"success": False, "error": f"Basis B' error: {err_bp}"}), 400

    mat_t, err_t = sanitize_and_parse_matrix(data.get('mat_t_b'))
    if err_t:
        return jsonify({"success": False, "error": f"Transformation T error: {err_t}"}), 400

    res = advanced_service.compute_change_of_basis(mat_b, mat_bp, mat_t, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@advanced_api.route('/inner_product', methods=['POST'])
def inner_product():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    vec_u, err_u = sanitize_and_parse_vector(data.get('vector_u'))
    if err_u:
        return jsonify({"success": False, "error": f"Vector u error: {err_u}"}), 400

    vec_v, err_v = sanitize_and_parse_vector(data.get('vector_v'))
    if err_v:
        return jsonify({"success": False, "error": f"Vector v error: {err_v}"}), 400

    mat_w, err_w = sanitize_and_parse_matrix(data.get('weight_matrix'))
    if err_w:
        return jsonify({"success": False, "error": f"Weight matrix W error: {err_w}"}), 400

    res = advanced_service.compute_weighted_inner_product(vec_u, vec_v, mat_w, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code
