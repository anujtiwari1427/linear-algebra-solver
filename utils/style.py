import streamlit as st

def apply_custom_css():
    """Applies a clean white professional theme."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

        /* ── Base ── */
        html, body, [class*="css"], .stApp {
            font-family: 'Inter', sans-serif;
            background: #FFFFFF;
            color: #111827;
        }

        /* ── Remove default Streamlit padding ── */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
        }

        /* ── Sidebar ── */
        section[data-testid="stSidebar"] {
            background: #FAFAFA !important;
            border-right: 1px solid #E5E7EB !important;
        }
        section[data-testid="stSidebar"] > div {
            padding-top: 0 !important;
        }

        /* ── Sidebar brand ── */
        .sidebar-brand {
            padding: 24px 20px 20px;
            border-bottom: 1px solid #E5E7EB;
            margin-bottom: 8px;
        }
        .sidebar-brand .logo-row {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 4px;
        }
        .sidebar-brand .logo-icon {
            width: 28px; height: 28px;
            background: #111827;
            border-radius: 6px;
            display: flex; align-items: center; justify-content: center;
            font-size: 0.85rem;
            color: #fff;
            font-weight: 700;
            font-family: 'JetBrains Mono', monospace;
            flex-shrink: 0;
        }
        .sidebar-brand h1 {
            margin: 0;
            font-size: 0.95rem;
            font-weight: 700;
            color: #111827;
            letter-spacing: -0.3px;
        }
        .sidebar-brand p {
            margin: 0;
            font-size: 0.7rem;
            color: #9CA3AF;
            font-weight: 400;
        }

        /* ── Nav group labels ── */
        .nav-label {
            padding: 12px 20px 4px;
            font-size: 0.63rem;
            font-weight: 600;
            color: #9CA3AF;
            text-transform: uppercase;
            letter-spacing: 0.9px;
        }

        /* ── Sidebar buttons ── */
        .stButton > button {
            background: transparent !important;
            border: none !important;
            border-radius: 6px !important;
            color: #6B7280 !important;
            font-weight: 500 !important;
            font-size: 0.82rem !important;
            text-align: left !important;
            padding: 7px 12px !important;
            width: 100% !important;
            transition: all 0.15s ease !important;
            box-shadow: none !important;
            justify-content: flex-start !important;
        }
        .stButton > button:hover {
            background: #F3F4F6 !important;
            color: #111827 !important;
            transform: none !important;
        }
        .stButton > button:active {
            background: #E5E7EB !important;
        }

        /* ── Selectbox ── */
        .stSelectbox > div > div {
            background: #FFFFFF !important;
            border: 1px solid #E5E7EB !important;
            border-radius: 7px !important;
            color: #111827 !important;
            font-size: 0.84rem !important;
            font-family: 'Inter', sans-serif !important;
        }
        .stSelectbox > div > div:hover {
            border-color: #6366F1 !important;
        }

        /* ── Module banner ── */
        .module-banner {
            padding: 0 0 22px 0;
            border-bottom: 1px solid #E5E7EB;
            margin-bottom: 28px;
        }
        .module-banner .breadcrumb {
            font-size: 0.7rem;
            color: #9CA3AF;
            font-weight: 500;
            letter-spacing: 0.3px;
            margin-bottom: 8px;
            text-transform: uppercase;
        }
        .module-banner h2 {
            margin: 0 0 6px 0;
            color: #111827;
            font-size: 1.6rem;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        .module-banner p {
            margin: 0;
            color: #6B7280;
            font-size: 0.875rem;
            line-height: 1.6;
        }

        /* ── Tabs ── */
        .stTabs [data-baseweb="tab-list"] {
            background: transparent !important;
            border-bottom: 1px solid #E5E7EB !important;
            border-radius: 0 !important;
            padding: 0 !important;
            gap: 0 !important;
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 0 !important;
            font-size: 0.82rem !important;
            font-weight: 500 !important;
            padding: 8px 18px !important;
            color: #9CA3AF !important;
            background: transparent !important;
            border-bottom: 2px solid transparent !important;
            margin-bottom: -1px !important;
            transition: color 0.15s ease !important;
        }
        .stTabs [data-baseweb="tab"]:hover {
            color: #374151 !important;
        }
        .stTabs [aria-selected="true"] {
            color: #111827 !important;
            border-bottom: 2px solid #111827 !important;
            background: transparent !important;
            box-shadow: none !important;
            font-weight: 600 !important;
        }
        .stTabs [data-baseweb="tab-panel"] {
            padding-top: 24px !important;
        }

        /* ── Metrics ── */
        .stMetric {
            background: #F9FAFB !important;
            border: 1px solid #E5E7EB !important;
            border-radius: 8px !important;
            padding: 14px 16px !important;
        }
        .stMetric label {
            color: #9CA3AF !important;
            font-size: 0.7rem !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.6px !important;
        }
        [data-testid="stMetricValue"] {
            color: #111827 !important;
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 1.25rem !important;
            font-weight: 700 !important;
        }

        /* ── Badge ── */
        .badge {
            display: inline-block;
            background: #F3F4F6;
            color: #374151;
            border: 1px solid #E5E7EB;
            border-radius: 4px;
            padding: 2px 9px;
            font-size: 0.73rem;
            font-weight: 500;
            margin: 2px 3px 2px 0;
        }
        .badge-accent {
            background: #EEF2FF;
            color: #4338CA;
            border-color: #C7D2FE;
        }

        /* ── Data editor ── */
        .stDataEditor [data-testid="stDataFrameResizable"] {
            border: 1px solid #E5E7EB !important;
            border-radius: 8px !important;
        }

        /* ── Number input ── */
        .stNumberInput input {
            background: #FFFFFF !important;
            border: 1px solid #E5E7EB !important;
            border-radius: 7px !important;
            color: #111827 !important;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.88rem;
            text-align: center;
        }
        .stNumberInput input:focus {
            border-color: #6366F1 !important;
            box-shadow: 0 0 0 3px rgba(99,102,241,0.08) !important;
        }

        /* ── Text inputs ── */
        .stTextInput input, .stTextArea textarea {
            background: #FFFFFF !important;
            border: 1px solid #E5E7EB !important;
            border-radius: 7px !important;
            color: #111827 !important;
            font-family: 'Inter', sans-serif;
            font-size: 0.84rem;
        }
        .stTextInput input:focus, .stTextArea textarea:focus {
            border-color: #6366F1 !important;
            box-shadow: 0 0 0 3px rgba(99,102,241,0.08) !important;
        }

        /* ── Divider ── */
        hr {
            border-color: #E5E7EB !important;
            margin: 20px 0 !important;
        }

        /* ── Alerts ── */
        .stAlert {
            border-radius: 8px !important;
            font-size: 0.84rem !important;
        }

        /* ── Expander ── */
        .streamlit-expanderHeader {
            background: transparent !important;
            border: none !important;
            font-size: 0.82rem !important;
            font-weight: 500 !important;
            color: #6B7280 !important;
            padding: 6px 20px !important;
        }
        .streamlit-expanderHeader:hover { color: #111827 !important; }
        .streamlit-expanderContent {
            border: none !important;
            padding: 2px 8px 4px !important;
        }

        /* ── Scrollbar ── */
        ::-webkit-scrollbar { width: 4px; height: 4px; }
        ::-webkit-scrollbar-track { background: #F9FAFB; }
        ::-webkit-scrollbar-thumb { background: #D1D5DB; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #9CA3AF; }

        /* ── Dashboard cards ── */
        .mod-card {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 10px;
            padding: 20px;
            transition: box-shadow 0.2s ease, border-color 0.2s ease;
            height: 100%;
        }
        .mod-card:hover {
            border-color: #6366F1;
            box-shadow: 0 4px 16px rgba(99,102,241,0.08);
        }
        .mod-card .icon {
            font-size: 1.3rem;
            margin-bottom: 10px;
        }
        .mod-card h4 {
            margin: 0 0 6px;
            color: #111827;
            font-size: 0.88rem;
            font-weight: 600;
        }
        .mod-card p {
            margin: 0;
            color: #9CA3AF;
            font-size: 0.76rem;
            line-height: 1.55;
        }

        /* ── Step box ── */
        .step-box {
            background: #F9FAFB;
            border: 1px solid #E5E7EB;
            border-radius: 8px;
            padding: 12px 16px;
            margin: 10px 0;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.82rem;
            color: #374151;
        }

        /* ── Status chip ── */
        .status-chip {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 12px;
            background: #F9FAFB;
            border: 1px solid #E5E7EB;
            border-radius: 7px;
            font-size: 0.73rem;
            color: #9CA3AF;
        }
        .status-chip .dot {
            width: 6px; height: 6px;
            background: #6366F1;
            border-radius: 50%;
            flex-shrink: 0;
        }
        .status-chip span {
            color: #374151;
            font-weight: 500;
        }

        /* ── Metric badge (text inline) ── */
        .metric-badge {
            display: inline-block;
            background: #F3F4F6;
            color: #374151;
            border: 1px solid #E5E7EB;
            border-radius: 5px;
            padding: 3px 10px;
            font-size: 0.75rem;
            font-weight: 500;
            margin: 2px 3px 2px 0;
        }

        /* ── Plotly chart frame ── */
        .stPlotlyChart {
            border: 1px solid #E5E7EB;
            border-radius: 10px;
            overflow: hidden;
        }

        /* ── Radio buttons ── */
        .stRadio label {
            font-size: 0.84rem !important;
            color: #374151 !important;
        }
        </style>
    """, unsafe_allow_html=True)


def render_banner(title: str, description: str, icon: str = ""):
    """Renders a clean minimal module header — white theme."""
    st.markdown(f"""
        <div class="module-banner">
            <div class="breadcrumb">Linear Algebra Suite</div>
            <h2>{icon}&nbsp; {title}</h2>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)


def render_section_header(title: str):
    """Renders a minimal section label."""
    st.markdown(
        f'<p style="font-size:0.7rem;font-weight:600;color:#9CA3AF;text-transform:uppercase;'
        f'letter-spacing:0.9px;margin:20px 0 8px 0;">{title}</p>',
        unsafe_allow_html=True
    )


def _navigate_to_module(key: str):
    st.session_state["selected_module"] = key
    st.session_state["_quick_jump_val"] = key


def render_home_dashboard():
    """Clean white professional home dashboard."""
    st.markdown("""
        <div style="padding: 32px 0 24px 0; max-width: 680px;">
            <p style="font-size:0.7rem;font-weight:600;color:#9CA3AF;
                      text-transform:uppercase;letter-spacing:0.9px;margin:0 0 10px 0;">
                Linear Algebra Suite
            </p>
            <h1 style="font-size:2rem;font-weight:700;color:#111827;
                       margin:0 0 12px 0;letter-spacing:-0.6px;line-height:1.25;
                       font-family:'Inter',sans-serif;">
                Interactive Solver &amp; Visualizer
            </h1>
            <p style="font-size:0.88rem;color:#6B7280;margin:0;line-height:1.65;max-width:560px;">
                A Python toolkit for matrix algebra, linear systems, vector spaces, eigenvalues, and
                advanced university topics — with step-by-step symbolic solutions and interactive plots.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="height:1px;background:#E5E7EB;margin-bottom:28px;"></div>',
                unsafe_allow_html=True)

    modules = [
        ("📷", "Image Solver (OCR)", "Upload photos. OCR extracts matrix values and solves automatically.", "📷 Image Question Solver (OCR)"),
        ("🧮", "Matrix Operations",  "Arithmetic, transpose, matrix power, LU/QR/SVD/Cholesky.", "🧮 Matrix Operations & Properties"),
        ("⚖️", "Linear Equations",   "Gauss-Jordan, Cramer's Rule, Inverse method, 2D/3D graphs.", "⚖️ Systems of Linear Equations"),
        ("🏹", "Vectors & Transforms","Dot/cross products, projections, norms, 2D grid animator.", "🏹 Vectors & Transformations"),
        ("🌌", "Vector Spaces",       "Subspaces, Rank-Nullity theorem, Gram-Schmidt.", "🌌 Vector Spaces & Subspaces"),
        ("💎", "Determinants",        "Cofactor expansion, adjugate, area and volume visualizer.", "💎 Determinants & Inverses"),
        ("⚡", "Eigenvalues",         "Characteristic polynomial, diagonalization, Cayley-Hamilton.", "⚡ Eigenvalues & Eigenvectors"),
        ("🎓", "Syllabus Solvers",    "GF(2), Change of Basis, Inner Products, Jordan Canonical Form.", "🎓 Advanced Syllabus Solvers"),
    ]

    for i in range(0, len(modules), 4):
        cols = st.columns(4, gap="small")
        for j, col in enumerate(cols):
            idx = i + j
            if idx < len(modules):
                icon, title, desc, key = modules[idx]
                with col:
                    with st.container(border=True):
                        st.markdown(f"""
                            <div style="min-height: 120px; display: flex; flex-direction: column; justify-content: flex-start;">
                                <div style="font-size: 1.4rem; margin-bottom: 8px;">{icon}</div>
                                <h4 style="margin: 0 0 6px 0; color: #111827; font-size: 0.88rem; font-weight: 600;">{title}</h4>
                                <p style="margin: 0 0 12px 0; color: #6B7280; font-size: 0.76rem; line-height: 1.5;">{desc}</p>
                            </div>
                        """, unsafe_allow_html=True)
                        st.button(
                            "Open →",
                            key=f"dash_btn_{idx}",
                            use_container_width=True,
                            on_click=_navigate_to_module,
                            args=(key,)
                        )
