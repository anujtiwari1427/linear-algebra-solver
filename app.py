import streamlit as st

st.set_page_config(
    page_title="Linear Algebra Suite",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

from utils.style import apply_custom_css, render_home_dashboard
from modules.matrix_ops import render_matrix_ops_module
from modules.linear_equations import render_linear_equations_module
from modules.vectors_transformations import render_vectors_transformations_module
from modules.vector_spaces import render_vector_spaces_module
from modules.determinants_inverses import render_determinants_inverses_module
from modules.eigen import render_eigen_module
from modules.syllabus_solvers import render_syllabus_solvers_module
from modules.image_solver import render_image_solver_module

apply_custom_css()

# ── Session state ──
if "selected_module" not in st.session_state:
    st.session_state["selected_module"] = "🏠 Home"

ALL_MODULES = [
    "🏠 Home",
    "📷 Image Question Solver (OCR)",
    "🧮 Matrix Operations & Properties",
    "⚖️ Systems of Linear Equations",
    "🏹 Vectors & Transformations",
    "🌌 Vector Spaces & Subspaces",
    "💎 Determinants & Inverses",
    "⚡ Eigenvalues & Eigenvectors",
    "🎓 Advanced Syllabus Solvers",
]

GROUPS = {
    "AI Tools": ["📷 Image Question Solver (OCR)"],
    "Core Algebra": [
        "🧮 Matrix Operations & Properties",
        "⚖️ Systems of Linear Equations",
        "🏹 Vectors & Transformations",
    ],
    "Advanced Topics": [
        "🌌 Vector Spaces & Subspaces",
        "💎 Determinants & Inverses",
        "⚡ Eigenvalues & Eigenvectors",
    ],
    "Syllabus": ["🎓 Advanced Syllabus Solvers"],
}

current = st.session_state["selected_module"]

# ── Sidebar ──
with st.sidebar:
    # Brand
    st.markdown("""
        <div class="sidebar-brand">
            <div class="logo-row">
                <div class="logo-icon">∑</div>
                <div>
                    <h1>Linear Algebra</h1>
                </div>
            </div>
            <p>Interactive Python Suite</p>
        </div>
    """, unsafe_allow_html=True)

    # Home
    st.markdown('<div class="nav-label">Navigation</div>', unsafe_allow_html=True)
    if st.button("🏠  Home", key="nav_home", use_container_width=True):
        st.session_state["selected_module"] = "🏠 Home"
        st.rerun()

    # Grouped expanders
    for group, items in GROUPS.items():
        with st.expander(group, expanded=current in items):
            for item in items:
                if st.button(item, key=f"nav_{item}", use_container_width=True):
                    st.session_state["selected_module"] = item
                    st.rerun()

    st.markdown("---")

    # Quick jump
    st.markdown('<div class="nav-label">Quick Jump</div>', unsafe_allow_html=True)
    jump = st.selectbox(
        "module",
        ALL_MODULES,
        index=ALL_MODULES.index(current),
        label_visibility="collapsed",
        key="quick_jump"
    )
    if jump != current:
        st.session_state["selected_module"] = jump
        st.rerun()

    st.markdown("---")

    # Active module chip
    st.markdown(f"""
        <div class="status-chip">
            <div class="dot"></div>
            <span>{current}</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="height:16px"></div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="font-size:0.68rem;color:#374151;padding:0 4px;line-height:2;">
            SymPy &nbsp;·&nbsp; NumPy &nbsp;·&nbsp; SciPy<br/>
            Plotly &nbsp;·&nbsp; EasyOCR &nbsp;·&nbsp; Streamlit
        </div>
    """, unsafe_allow_html=True)

# ── Routing ──
m = st.session_state["selected_module"]

if m == "🏠 Home":
    render_home_dashboard()
elif m == "📷 Image Question Solver (OCR)":
    render_image_solver_module()
elif m == "🧮 Matrix Operations & Properties":
    render_matrix_ops_module()
elif m == "⚖️ Systems of Linear Equations":
    render_linear_equations_module()
elif m == "🏹 Vectors & Transformations":
    render_vectors_transformations_module()
elif m == "🌌 Vector Spaces & Subspaces":
    render_vector_spaces_module()
elif m == "💎 Determinants & Inverses":
    render_determinants_inverses_module()
elif m == "⚡ Eigenvalues & Eigenvectors":
    render_eigen_module()
elif m == "🎓 Advanced Syllabus Solvers":
    render_syllabus_solvers_module()
