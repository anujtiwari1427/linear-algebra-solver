from flask import Blueprint, request, jsonify
from services.validation_service import sanitize_and_parse_matrix
from services import decomposition_service

decomposition_api = Blueprint('api_decomposition', __name__, url_prefix='/api/decomposition')

@decomposition_api.route('/lu', methods=['POST'])
def lu():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = decomposition_service.compute_lu_decomposition(mat_a, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@decomposition_api.route('/qr', methods=['POST'])
def qr():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = decomposition_service.compute_qr_decomposition(mat_a, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@decomposition_api.route('/svd', methods=['POST'])
def svd():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = decomposition_service.compute_svd_decomposition(mat_a, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@decomposition_api.route('/cholesky', methods=['POST'])
def cholesky():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = decomposition_service.compute_cholesky_decomposition(mat_a, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code
