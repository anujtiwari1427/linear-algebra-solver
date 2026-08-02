from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html', title="Linear Algebra Suite | Dashboard")

@main_bp.route('/matrix')
def matrix_view():
    return render_template('matrix.html', title="Matrix Operations")

@main_bp.route('/vector')
def vector_view():
    return render_template('vector.html', title="Vector Operations")

@main_bp.route('/system')
def system_view():
    return render_template('system.html', title="Systems of Linear Equations")

@main_bp.route('/eigen')
def eigen_view():
    return render_template('eigen.html', title="Eigenvalues & Eigenspaces")

@main_bp.route('/decomposition')
def decomposition_view():
    return render_template('decomposition.html', title="Matrix Decompositions")

@main_bp.route('/advanced')
def advanced_view():
    return render_template('advanced.html', title="Advanced Syllabus Solvers")
