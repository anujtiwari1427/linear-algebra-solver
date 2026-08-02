from flask import Blueprint, request, jsonify
from services.validation_service import sanitize_and_parse_vector
from services import vector_service

vector_api = Blueprint('api_vector', __name__, url_prefix='/api/vector')

@vector_api.route('/dot', methods=['POST'])
def dot():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    vec_a, err_a = sanitize_and_parse_vector(data.get('vector_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Vector A error: {err_a}"}), 400

    vec_b, err_b = sanitize_and_parse_vector(data.get('vector_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Vector B error: {err_b}"}), 400

    res = vector_service.vector_dot_product(vec_a, vec_b, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@vector_api.route('/cross', methods=['POST'])
def cross():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    vec_a, err_a = sanitize_and_parse_vector(data.get('vector_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Vector A error: {err_a}"}), 400

    vec_b, err_b = sanitize_and_parse_vector(data.get('vector_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Vector B error: {err_b}"}), 400

    res = vector_service.vector_cross_product(vec_a, vec_b, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@vector_api.route('/magnitude', methods=['POST'])
def magnitude():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    vec_a, err_a = sanitize_and_parse_vector(data.get('vector_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Vector A error: {err_a}"}), 400

    res = vector_service.vector_magnitude(vec_a, show_steps=show_steps)
    return jsonify(res), 200


@vector_api.route('/unit', methods=['POST'])
def unit():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    vec_a, err_a = sanitize_and_parse_vector(data.get('vector_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Vector A error: {err_a}"}), 400

    res = vector_service.vector_unit_vector(vec_a, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@vector_api.route('/projection', methods=['POST'])
def projection():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    vec_a, err_a = sanitize_and_parse_vector(data.get('vector_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Vector A error: {err_a}"}), 400

    vec_b, err_b = sanitize_and_parse_vector(data.get('vector_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Vector B error: {err_b}"}), 400

    res = vector_service.vector_projection(vec_a, vec_b, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@vector_api.route('/angle', methods=['POST'])
def angle():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    vec_a, err_a = sanitize_and_parse_vector(data.get('vector_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Vector A error: {err_a}"}), 400

    vec_b, err_b = sanitize_and_parse_vector(data.get('vector_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Vector B error: {err_b}"}), 400

    res = vector_service.vector_angle(vec_a, vec_b, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code


@vector_api.route('/distance', methods=['POST'])
def distance():
    data = request.get_json() or {}
    show_steps = data.get('show_steps', True)

    vec_a, err_a = sanitize_and_parse_vector(data.get('vector_a'))
    if err_a:
        return jsonify({"success": False, "error": f"Vector A error: {err_a}"}), 400

    vec_b, err_b = sanitize_and_parse_vector(data.get('vector_b'))
    if err_b:
        return jsonify({"success": False, "error": f"Vector B error: {err_b}"}), 400

    res = vector_service.vector_distance(vec_a, vec_b, show_steps=show_steps)
    status_code = 200 if res.get('success') else 400
    return jsonify(res), status_code
