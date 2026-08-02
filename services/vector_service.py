import numpy as np
import sympy as sp
from typing import Dict, Any, List, Optional
from services.validation_service import (
    sanitize_and_parse_vector,
    validate_non_zero_vector
)
from services.matrix_service import format_number

def vector_to_list(vec: np.ndarray) -> List[float]:
    return [round(float(x), 4) for x in vec]

def vector_to_latex(vec: np.ndarray) -> str:
    elems = [format_number(x) for x in vec]
    return "\\begin{pmatrix} " + " \\\\ ".join(elems) + " \\end{pmatrix}"


def vector_dot_product(vec_a: np.ndarray, vec_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    if vec_a.size != vec_b.size:
        return {"success": False, "error": f"Vector size mismatch: Vector A is dimension {vec_a.size} while Vector B is dimension {vec_b.size}."}

    dot_val = float(np.dot(vec_a, vec_b))
    n = vec_a.size

    steps = []
    if show_steps:
        steps.append(f"#### Step-by-Step Dot Product (Dimension {n}):")
        steps.append("Formula: $\\vec{u} \\cdot \\vec{v} = \\sum_{i=1}^{n} u_i v_i = u_1 v_1 + u_2 v_2 + \\dots + u_n v_n$")
        terms = [f"({format_number(vec_a[i])} \\times {format_number(vec_b[i])})" for i in range(n)]
        steps.append(f"$\\vec{{u}} \\cdot \\vec{{v}} = {" + ".join(terms)} = {format_number(dot_val)}$")

    return {
        "success": True,
        "operation": "Dot Product",
        "vector_a": vector_to_list(vec_a),
        "vector_b": vector_to_list(vec_b),
        "result": round(dot_val, 4),
        "latex_result": f"\\vec{{u}} \\cdot \\vec{{v}} = {format_number(dot_val)}",
        "steps": steps,
        "explanation": "The dot product measures directional alignment between two vectors. It yields a scalar quantity.",
        "time_complexity": f"O({n})"
    }


def vector_cross_product(vec_a: np.ndarray, vec_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    if vec_a.size != 3 or vec_b.size != 3:
        return {"success": False, "error": f"Cross product is defined strictly for 3D vectors. Got dimensions {vec_a.size} and {vec_b.size}."}

    cross_vec = np.cross(vec_a, vec_b)
    a1, a2, a3 = vec_a
    b1, b2, b3 = vec_b
    c1, c2, c3 = cross_vec

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step 3D Cross Product:")
        steps.append("Evaluated via determinant of $3 \\times 3$ matrix with unit vectors $\\hat{i}, \\hat{j}, \\hat{k}$:")
        steps.append(f"$$\\vec{{u}} \\times \\vec{{v}} = \\begin{{vmatrix}} \\hat{{i}} & \\hat{{j}} & \\hat{{k}} \\\\ {format_number(a1)} & {format_number(a2)} & {format_number(a3)} \\\\ {format_number(b1)} & {format_number(b2)} & {format_number(b3)} \\end{{vmatrix}}$$")
        steps.append(f"$\\hat{{i}}$ component: $({format_number(a2)} \\times {format_number(b3)}) - ({format_number(a3)} \\times {format_number(b2)}) = {format_number(c1)}$")
        steps.append(f"$\\hat{{j}}$ component: $-(({format_number(a1)} \\times {format_number(b3)}) - ({format_number(a3)} \\times {format_number(b1)})) = {format_number(c2)}$")
        steps.append(f"$\\hat{{k}}$ component: $({format_number(a1)} \\times {format_number(b2)}) - ({format_number(a2)} \\times {format_number(b1)}) = {format_number(c3)}$")

    return {
        "success": True,
        "operation": "Cross Product",
        "vector_a": vector_to_list(vec_a),
        "vector_b": vector_to_list(vec_b),
        "result": vector_to_list(cross_vec),
        "latex_result": f"\\vec{{u}} \\times \\vec{{v}} = {vector_to_latex(cross_vec)}",
        "steps": steps,
        "explanation": "The cross product produces a vector that is orthogonal (perpendicular) to both input vectors.",
        "time_complexity": "O(1) [3D constant]"
    }


def vector_magnitude(vec_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    norm_val = float(np.linalg.norm(vec_a))
    n = vec_a.size

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Magnitude (Euclidean Norm):")
        steps.append(r"Formula: $\|\vec{v}\| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}$")
        sq_terms = [f"({format_number(x)})^2" for x in vec_a]
        sum_sq = sum(x**2 for x in vec_a)
        steps.append(f"$\\|\\vec{{v}}\\| = \\sqrt{{" + " + ".join(sq_terms) + f"}} = \\sqrt{{{format_number(sum_sq)}}} = {format_number(norm_val)}$")

    return {
        "success": True,
        "operation": "Vector Magnitude",
        "vector_a": vector_to_list(vec_a),
        "result": round(norm_val, 4),
        "latex_result": f"\\|\\vec{{v}}\\| = {format_number(norm_val)}",
        "steps": steps,
        "explanation": "The magnitude represents the geometric length of the vector in Euclidean space.",
        "time_complexity": f"O({n})"
    }


def vector_unit_vector(vec_a: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    err = validate_non_zero_vector(vec_a, "Vector A")
    if err:
        return {"success": False, "error": err}

    norm_val = float(np.linalg.norm(vec_a))
    unit_vec = vec_a / norm_val

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Unit Vector Calculation:")
        steps.append(r"1. Compute magnitude: $\|\vec{v}\| = " + format_number(norm_val) + "$")
        steps.append("2. Scale vector by reciprocal of magnitude: $\\hat{v} = \\frac{\\vec{v}}{\\|\\vec{v}\\|}$")
        steps.append(f"$$\\hat{{v}} = \\frac{{1}}{{{format_number(norm_val)}}} {vector_to_latex(vec_a)} = {vector_to_latex(unit_vec)}$$")

    return {
        "success": True,
        "operation": "Unit Vector",
        "vector_a": vector_to_list(vec_a),
        "result": vector_to_list(unit_vec),
        "magnitude": round(norm_val, 4),
        "latex_result": f"\\hat{{v}} = {vector_to_latex(unit_vec)}",
        "steps": steps,
        "explanation": "A unit vector has a magnitude of 1 and points in the exact same direction as the original vector.",
        "time_complexity": f"O({vec_a.size})"
    }


def vector_projection(vec_a: np.ndarray, vec_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    if vec_a.size != vec_b.size:
        return {"success": False, "error": f"Vector dimension mismatch ({vec_a.size} vs {vec_b.size})."}

    err = validate_non_zero_vector(vec_b, "Target Vector B")
    if err:
        return {"success": False, "error": err}

    dot_ab = float(np.dot(vec_a, vec_b))
    norm_b_sq = float(np.sum(vec_b**2))
    proj_vec = (dot_ab / norm_b_sq) * vec_b

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Projection of Vector A onto Vector B:")
        steps.append("Formula: $\\text{proj}_{\\vec{v}}(\\vec{u}) = \\frac{\\vec{u} \\cdot \\vec{v}}{\\|\\vec{v}\\|^2} \\vec{v}$")
        steps.append(f"1. Dot product $\\vec{{u}} \\cdot \\vec{{v}} = {format_number(dot_ab)}$")
        steps.append(f"2. Squared magnitude $\\|\\vec{{v}}\\|^2 = {format_number(norm_b_sq)}$")
        steps.append(f"3. Scalar projection factor $c = \\frac{{{format_number(dot_ab)}}}{{{format_number(norm_b_sq)}}} = {format_number(dot_ab / norm_b_sq)}$")
        steps.append(f"$$\\text{{proj}}_{{\\vec{{v}}}}(\\vec{{u}}) = {format_number(dot_ab / norm_b_sq)} \\times {vector_to_latex(vec_b)} = {vector_to_latex(proj_vec)}$$")

    return {
        "success": True,
        "operation": "Vector Projection",
        "vector_a": vector_to_list(vec_a),
        "vector_b": vector_to_list(vec_b),
        "result": vector_to_list(proj_vec),
        "latex_result": f"\\text{{proj}}_{{\\vec{{v}}}}(\\vec{{u}}) = {vector_to_latex(proj_vec)}",
        "steps": steps,
        "explanation": "Vector projection computes the shadow or component of Vector A along the direction of Vector B.",
        "time_complexity": f"O({vec_a.size})"
    }


def vector_angle(vec_a: np.ndarray, vec_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    if vec_a.size != vec_b.size:
        return {"success": False, "error": f"Vector dimension mismatch ({vec_a.size} vs {vec_b.size})."}

    err_a = validate_non_zero_vector(vec_a, "Vector A")
    if err_a:
        return {"success": False, "error": err_a}

    err_b = validate_non_zero_vector(vec_b, "Vector B")
    if err_b:
        return {"success": False, "error": err_b}

    norm_a = float(np.linalg.norm(vec_a))
    norm_b = float(np.linalg.norm(vec_b))
    dot_ab = float(np.dot(vec_a, vec_b))

    cos_theta = np.clip(dot_ab / (norm_a * norm_b), -1.0, 1.0)
    angle_rad = float(np.arccos(cos_theta))
    angle_deg = float(np.degrees(angle_rad))

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Angle Between Vectors:")
        steps.append("Formula: $\\cos\\theta = \\frac{\\vec{u} \\cdot \\vec{v}}{\\|\\vec{u}\\| \\|\\vec{v}\\|}$")
        steps.append(f"1. Dot product $\\vec{{u}} \\cdot \\vec{{v}} = {format_number(dot_ab)}$")
        steps.append(f"2. Magnitudes: $\\|\\vec{{u}}\\| = {format_number(norm_a)}$, $\\|\\vec{{v}}\\| = {format_number(norm_b)}$")
        steps.append(f"3. $\\cos\\theta = \\frac{{{format_number(dot_ab)}}}{{{format_number(norm_a)} \\times {format_number(norm_b)}}} = {format_number(cos_theta)}$")
        steps.append(f"4. $\\theta = \\arccos({format_number(cos_theta)}) = {format_number(angle_rad)}\\text{{ rad}} = {format_number(angle_deg)}^\\circ$")

    return {
        "success": True,
        "operation": "Angle Between Vectors",
        "vector_a": vector_to_list(vec_a),
        "vector_b": vector_to_list(vec_b),
        "radians": round(angle_rad, 4),
        "degrees": round(angle_deg, 4),
        "latex_result": f"\\theta = {format_number(angle_deg)}^\\circ \\quad ({format_number(angle_rad)} \\text{{ rad}})",
        "steps": steps,
        "explanation": "Calculates the inner geometric angle enclosed between two vectors.",
        "time_complexity": f"O({vec_a.size})"
    }


def vector_distance(vec_a: np.ndarray, vec_b: np.ndarray, show_steps: bool = True) -> Dict[str, Any]:
    if vec_a.size != vec_b.size:
        return {"success": False, "error": f"Vector dimension mismatch ({vec_a.size} vs {vec_b.size})."}

    diff = vec_b - vec_a
    dist_val = float(np.linalg.norm(diff))
    n = vec_a.size

    steps = []
    if show_steps:
        steps.append("#### Step-by-Step Euclidean Distance:")
        steps.append("Formula: $d(\\vec{u}, \\vec{v}) = \\sqrt{\\sum_{i=1}^{n} (v_i - u_i)^2}$")
        sq_diffs = [f"({format_number(vec_b[i])} - ({format_number(vec_a[i])}))^2" for i in range(n)]
        steps.append(f"$d(\\vec{{u}}, \\vec{{v}}) = \\sqrt{{" + " + ".join(sq_diffs) + f"}} = {format_number(dist_val)}$")

    return {
        "success": True,
        "operation": "Distance Between Vectors",
        "vector_a": vector_to_list(vec_a),
        "vector_b": vector_to_list(vec_b),
        "result": round(dist_val, 4),
        "latex_result": f"d(\\vec{{u}}, \\vec{{v}}) = {format_number(dist_val)}",
        "steps": steps,
        "explanation": "Computes the straight-line Euclidean distance between two points/vector tips in space.",
        "time_complexity": f"O({n})"
    }
