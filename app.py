import streamlit as st

# Configure page settings
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

# Apply custom dark glassmorphic styling
apply_custom_css()

# ── Module groups for sidebar dropdowns ──
MODULE_GROUPS = {
    "🏠 Home Dashboard": ["🏠 Home Dashboard"],
    "📷 AI & OCR Tools": [
        "📷 Image Question Solver (OCR)"
    ],
    "📐 Core Linear Algebra": [
        "🧮 Matrix Operations & Properties",
        "⚖️ Systems of Linear Equations",
        "🏹 Vectors & Transformations",
    ],
    "🔬 Advanced Topics": [
        "🌌 Vector Spaces & Subspaces",
        "💎 Determinants & Inverses",
        "⚡ Eigenvalues & Eigenvectors",
    ],
    "🎓 Syllabus Solvers": [
        "🎓 Advanced Syllabus Solvers",
    ],
}

ALL_MODULES = [m for group_items in MODULE_GROUPS.values() for m in group_items]

# ── Initialize session state ──
if "selected_module" not in st.session_state:
    st.session_state["selected_module"] = "🏠 Home Dashboard"

# ── Sidebar ──
with st.sidebar:
    # Brand header
    st.markdown("""
        <div class="sidebar-brand">
            <h1>📐 Linear Algebra</h1>
            <p>Interactive Python Web Suite</p>
            <span class="version-badge">v2.0 — Python 3.13</span>
        </div>
    """, unsafe_allow_html=True)

    # Navigation via grouped dropdowns
    st.markdown('<div class="nav-group-label">📂 Navigate to Module</div>', unsafe_allow_html=True)

    for group_label, group_items in MODULE_GROUPS.items():
        if group_label == "🏠 Home Dashboard":
            if st.button("🏠 Home Dashboard", key="nav_home", use_container_width=True):
                st.session_state["selected_module"] = "🏠 Home Dashboard"
                st.rerun()
        else:
            with st.expander(group_label, expanded=(
                st.session_state["selected_module"] in group_items
            )):
                for item in group_items:
                    is_active = st.session_state["selected_module"] == item
                    label = f"▶ {item}" if is_active else f"   {item}"
                    if st.button(label, key=f"nav_{item}", use_container_width=True):
                        st.session_state["selected_module"] = item
                        st.rerun()

    st.divider()

    # Current module indicator
    current = st.session_state["selected_module"]
    st.markdown(f"""
        <div style="padding:8px 10px; background:rgba(99,102,241,0.08);
                    border:1px solid rgba(99,102,241,0.2); border-radius:8px;
                    font-size:0.75rem; color:#818CF8; font-weight:600;">
            ✦ Active: {current}
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Quick jump selectbox
    st.markdown('<div class="nav-group-label">⚡ Quick Jump</div>', unsafe_allow_html=True)
    quick_jump = st.selectbox(
        "Jump to any module",
        ALL_MODULES,
        index=ALL_MODULES.index(current),
        key="quick_jump_select",
        label_visibility="collapsed"
    )
    if quick_jump != current:
        st.session_state["selected_module"] = quick_jump
        st.rerun()

    st.divider()

    # Tech stack info
    st.markdown("""
        <div style="padding:12px 10px; background:rgba(255,255,255,0.02);
                    border:1px solid rgba(255,255,255,0.05); border-radius:10px;
                    font-size:0.72rem; color:#6B7280; line-height:1.8;">
            <span style="color:#9CA3AF; font-weight:700; font-size:0.75rem;">🛠 Tech Stack</span><br/>
            SymPy &nbsp;·&nbsp; NumPy &nbsp;·&nbsp; SciPy<br/>
            Plotly &nbsp;·&nbsp; Pandas &nbsp;·&nbsp; Streamlit<br/>
            EasyOCR &nbsp;·&nbsp; Pillow &nbsp;·&nbsp; PyTesseract
        </div>
    """, unsafe_allow_html=True)

# ── Main Content Routing ──
module = st.session_state["selected_module"]

if module == "🏠 Home Dashboard":
    render_home_dashboard()

elif module == "📷 Image Question Solver (OCR)":
    render_image_solver_module()

elif module == "🧮 Matrix Operations & Properties":
    render_matrix_ops_module()

elif module == "⚖️ Systems of Linear Equations":
    render_linear_equations_module()

elif module == "🏹 Vectors & Transformations":
    render_vectors_transformations_module()

elif module == "🌌 Vector Spaces & Subspaces":
    render_vector_spaces_module()

elif module == "💎 Determinants & Inverses":
    render_determinants_inverses_module()

elif module == "⚡ Eigenvalues & Eigenvectors":
    render_eigen_module()

elif module == "🎓 Advanced Syllabus Solvers":
    render_syllabus_solvers_module()
