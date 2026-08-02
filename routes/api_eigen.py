from flask import Blueprint, request, jsonify
from services.validation_service import sanitize_and_parse_matrix
from services import eigen_service

eigen_api = Blueprint('api_eigen', __name__, url_prefix='/api/eigen')

@eigen_api.route('/analysis', methods=['POST'])
def analysis():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = eigen_service.compute_eigen_analysis(mat_a, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@eigen_api.route('/diagonalization', methods=['POST'])
def diagonalization():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)
    k_exp = int(data.get('exponent', 5))

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = eigen_service.compute_diagonalization(mat_a, k_exp=k_exp, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@eigen_api.route('/cayley_hamilton', methods=['POST'])
def cayley_hamilton():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    mat_a, err_a = sanitize_and_parse_matrix(data.get('matrix_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Matrix A error: {err_a}"}), 400

    res = eigen_service.compute_cayley_hamilton(mat_a, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code
