import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Linear Algebra Interactive Web Suite",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

from utils.style import apply_custom_css
from modules.matrix_ops import render_matrix_ops_module
from modules.linear_equations import render_linear_equations_module
from modules.vectors_transformations import render_vectors_transformations_module
from modules.vector_spaces import render_vector_spaces_module
from modules.determinants_inverses import render_determinants_inverses_module
from modules.eigen import render_eigen_module
from modules.syllabus_solvers import render_syllabus_solvers_module
from modules.image_solver import render_image_solver_module

# Apply custom dark glassmorphic styling
apply_custom_css()

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 10px 0 20px 0;">
            <h1 style="margin: 0; font-size: 1.8rem;" class="gradient-text">Linear Algebra</h1>
            <p style="margin: 2px 0 0 0; color: #9CA3AF; font-size: 0.85rem;">Interactive Python Web Suite</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    module_choice = st.radio(
        "Select Learning Module",
        [
            "📷 Image Question Solver (OCR)",
            "🎓 Advanced Syllabus Solvers",
            "🧮 Matrix Operations & Properties",
            "⚖️ Systems of Linear Equations",
            "🏹 Vectors & Transformations",
            "🌌 Vector Spaces & Subspaces",
            "💎 Determinants & Inverses",
            "⚡ Eigenvalues & Eigenvectors"
        ]
    )

    st.divider()

    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.03); border-radius: 10px; padding: 12px; font-size: 0.8rem; color: #9CA3AF;">
            <b style="color: #F3F4F6;">Powered By:</b><br/>
            • <b>SymPy</b> (Exact Math & LaTeX)<br/>
            • <b>Plotly</b> (Interactive 2D/3D Graphs)<br/>
            • <b>NumPy / SciPy</b> (Matrix Computations)<br/>
            • <b>Streamlit</b> (UI Framework)
        </div>
    """, unsafe_allow_html=True)

# Main Content Routing
if module_choice == "📷 Image Question Solver (OCR)":
    render_image_solver_module()

elif module_choice == "🎓 Advanced Syllabus Solvers":
    render_syllabus_solvers_module()

elif module_choice == "🧮 Matrix Operations & Properties":
    render_matrix_ops_module()

elif module_choice == "⚖️ Systems of Linear Equations":
    render_linear_equations_module()

elif module_choice == "🏹 Vectors & Transformations":
    render_vectors_transformations_module()

elif module_choice == "🌌 Vector Spaces & Subspaces":
    render_vector_spaces_module()

elif module_choice == "💎 Determinants & Inverses":
    render_determinants_inverses_module()

elif module_choice == "⚡ Eigenvalues & Eigenvectors":
    render_eigen_module()
