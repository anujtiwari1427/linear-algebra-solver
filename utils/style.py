import streamlit as st

def apply_custom_css():
    """Applies a clean, minimal, professional dark theme."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

        /* ── Base ── */
        html, body, [class*="css"], .stApp {
            font-family: 'Inter', sans-serif;
            background: #0F1117;
            color: #E2E8F0;
        }

        /* ── Sidebar ── */
        section[data-testid="stSidebar"] {
            background: #0A0D14 !important;
            border-right: 1px solid #1E2330 !important;
        }
        section[data-testid="stSidebar"] > div {
            padding-top: 0 !important;
        }

        /* ── Sidebar brand ── */
        .sidebar-brand {
            padding: 24px 20px 18px;
            border-bottom: 1px solid #1E2330;
            margin-bottom: 4px;
        }
        .sidebar-brand .logo-row {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 4px;
        }
        .sidebar-brand .logo-icon {
            width: 30px; height: 30px;
            background: #4F46E5;
            border-radius: 7px;
            display: flex; align-items: center; justify-content: center;
            font-size: 0.95rem;
            flex-shrink: 0;
        }
        .sidebar-brand h1 {
            margin: 0;
            font-size: 1rem;
            font-weight: 700;
            color: #F1F5F9;
            letter-spacing: -0.3px;
        }
        .sidebar-brand p {
            margin: 0;
            font-size: 0.72rem;
            color: #475569;
            font-weight: 400;
        }

        /* ── Nav group labels ── */
        .nav-label {
            padding: 14px 20px 5px;
            font-size: 0.65rem;
            font-weight: 600;
            color: #374151;
            text-transform: uppercase;
            letter-spacing: 0.9px;
        }

        /* ── Sidebar buttons ── */
        .stButton > button {
            background: transparent !important;
            border: none !important;
            border-radius: 7px !important;
            color: #64748B !important;
            font-weight: 500 !important;
            font-size: 0.82rem !important;
            text-align: left !important;
            padding: 7px 12px !important;
            width: 100% !important;
            transition: all 0.15s ease !important;
            box-shadow: none !important;
        }
        .stButton > button:hover {
            background: #1E2330 !important;
            color: #CBD5E1 !important;
            transform: none !important;
        }

        /* ── Active nav button ── */
        .active-nav button {
            background: #1E2330 !important;
            color: #818CF8 !important;
            border-left: 2px solid #4F46E5 !important;
            border-radius: 0 7px 7px 0 !important;
        }

        /* ── Selectbox ── */
        .stSelectbox > div > div {
            background: #161B27 !important;
            border: 1px solid #1E2330 !important;
            border-radius: 8px !important;
            color: #CBD5E1 !important;
            font-size: 0.84rem !important;
        }
        .stSelectbox > div > div:hover {
            border-color: #4F46E5 !important;
        }

        /* ── Module banner ── */
        .module-banner {
            padding: 0 0 20px 0;
            border-bottom: 1px solid #1E2330;
            margin-bottom: 24px;
        }
        .module-banner .breadcrumb {
            font-size: 0.72rem;
            color: #475569;
            font-weight: 500;
            letter-spacing: 0.3px;
            margin-bottom: 6px;
            text-transform: uppercase;
        }
        .module-banner h2 {
            margin: 0 0 4px 0;
            color: #F1F5F9;
            font-size: 1.55rem;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        .module-banner p {
            margin: 0;
            color: #64748B;
            font-size: 0.875rem;
            line-height: 1.55;
        }

        /* ── Tabs ── */
        .stTabs [data-baseweb="tab-list"] {
            background: transparent !important;
            border-bottom: 1px solid #1E2330 !important;
            border-radius: 0 !important;
            padding: 0 !important;
            gap: 0 !important;
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 0 !important;
            font-size: 0.82rem !important;
            font-weight: 500 !important;
            padding: 8px 18px !important;
            color: #475569 !important;
            background: transparent !important;
            border-bottom: 2px solid transparent !important;
            margin-bottom: -1px !important;
            transition: color 0.15s ease !important;
        }
        .stTabs [data-baseweb="tab"]:hover {
            color: #94A3B8 !important;
        }
        .stTabs [aria-selected="true"] {
            color: #818CF8 !important;
            border-bottom: 2px solid #4F46E5 !important;
            background: transparent !important;
            box-shadow: none !important;
        }
        .stTabs [data-baseweb="tab-panel"] {
            padding-top: 22px !important;
        }

        /* ── Metrics ── */
        .stMetric {
            background: #161B27 !important;
            border: 1px solid #1E2330 !important;
            border-radius: 8px !important;
            padding: 14px 16px !important;
        }
        .stMetric label {
            color: #475569 !important;
            font-size: 0.72rem !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.6px !important;
        }
        [data-testid="stMetricValue"] {
            color: #F1F5F9 !important;
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 1.2rem !important;
            font-weight: 600 !important;
        }

        /* ── Badge / pill ── */
        .badge {
            display: inline-block;
            background: #1E2330;
            color: #94A3B8;
            border: 1px solid #2D3748;
            border-radius: 4px;
            padding: 2px 9px;
            font-size: 0.73rem;
            font-weight: 500;
            margin: 2px 3px 2px 0;
        }
        .badge-accent {
            background: rgba(79,70,229,0.12);
            color: #818CF8;
            border-color: rgba(79,70,229,0.25);
        }

        /* ── Data editor ── */
        .stDataEditor [data-testid="stDataFrameResizable"] {
            border: 1px solid #1E2330 !important;
            border-radius: 8px !important;
        }

        /* ── Number input ── */
        .stNumberInput input {
            background: #161B27 !important;
            border: 1px solid #1E2330 !important;
            border-radius: 7px !important;
            color: #E2E8F0 !important;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.88rem;
            text-align: center;
        }
        .stNumberInput input:focus {
            border-color: #4F46E5 !important;
            box-shadow: 0 0 0 2px rgba(79,70,229,0.12) !important;
        }

        /* ── Divider ── */
        hr {
            border-color: #1E2330 !important;
            margin: 18px 0 !important;
        }

        /* ── Alerts ── */
        .stAlert {
            border-radius: 8px !important;
            border-width: 1px !important;
        }

        /* ── Expandable (sidebar) ── */
        .streamlit-expanderHeader {
            background: transparent !important;
            border: none !important;
            font-size: 0.82rem !important;
            font-weight: 500 !important;
            color: #64748B !important;
            padding: 6px 20px !important;
        }
        .streamlit-expanderHeader:hover { color: #94A3B8 !important; }
        .streamlit-expanderContent {
            border: none !important;
            padding: 0 8px !important;
        }

        /* ── Scrollbar ── */
        ::-webkit-scrollbar { width: 3px; height: 3px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #2D3748; border-radius: 3px; }

        /* ── Dashboard cards ── */
        .mod-card {
            background: #161B27;
            border: 1px solid #1E2330;
            border-radius: 10px;
            padding: 18px 20px;
            transition: border-color 0.2s ease;
            height: 100%;
        }
        .mod-card:hover { border-color: #4F46E5; }
        .mod-card .icon { font-size: 1.4rem; margin-bottom: 10px; }
        .mod-card h4 {
            margin: 0 0 5px;
            color: #E2E8F0;
            font-size: 0.88rem;
            font-weight: 600;
        }
        .mod-card p {
            margin: 0;
            color: #475569;
            font-size: 0.76rem;
            line-height: 1.5;
        }

        /* ── Step box ── */
        .step-box {
            background: #161B27;
            border: 1px solid #1E2330;
            border-radius: 8px;
            padding: 12px 16px;
            margin: 10px 0;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.82rem;
        }

        /* ── Active status chip ── */
        .status-chip {
            display: flex;
            align-items: center;
            gap: 7px;
            padding: 7px 12px;
            background: #161B27;
            border: 1px solid #1E2330;
            border-radius: 7px;
            font-size: 0.74rem;
            color: #64748B;
        }
        .status-chip .dot {
            width: 6px; height: 6px;
            background: #4F46E5;
            border-radius: 50%;
            flex-shrink: 0;
        }
        .status-chip span { color: #94A3B8; font-weight: 500; }
        </style>
    """, unsafe_allow_html=True)


def render_banner(title: str, description: str, icon: str = ""):
    """Renders a clean minimal module header."""
    st.markdown(f"""
        <div class="module-banner">
            <div class="breadcrumb">Linear Algebra Suite</div>
            <h2>{icon}&nbsp; {title}</h2>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)


def render_section_header(title: str):
    """Renders a minimal section label."""
    st.markdown(f'<p style="font-size:0.72rem;font-weight:600;color:#475569;text-transform:uppercase;letter-spacing:0.8px;margin:18px 0 8px 0;">{title}</p>', unsafe_allow_html=True)


def render_home_dashboard():
    """Minimal professional home dashboard."""
    st.markdown("""
        <div style="padding: 36px 0 28px 0; max-width: 720px;">
            <p style="font-size:0.72rem;font-weight:600;color:#475569;text-transform:uppercase;letter-spacing:0.9px;margin:0 0 10px 0;">
                Linear Algebra Suite
            </p>
            <h1 style="font-size:2.1rem;font-weight:700;color:#F1F5F9;margin:0 0 12px 0;letter-spacing:-0.8px;line-height:1.2;">
                Interactive Solver &amp; Visualizer
            </h1>
            <p style="font-size:0.9rem;color:#64748B;margin:0;line-height:1.6;max-width:580px;">
                A comprehensive Python toolkit for matrix algebra, linear systems, vector spaces,
                eigenvalues, and advanced university syllabus topics — with step-by-step solutions
                and interactive 2D/3D plots.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="height:1px;background:#1E2330;margin-bottom:28px;"></div>', unsafe_allow_html=True)

    modules = [
        ("📷", "Image Solver (OCR)", "Upload photos of math problems. OCR extracts and solves matrices automatically.", "📷 Image Question Solver (OCR)"),
        ("🧮", "Matrix Operations", "Arithmetic, power, decompositions: LU, QR, SVD, Cholesky.", "🧮 Matrix Operations & Properties"),
        ("⚖️", "Linear Equations", "Gauss-Jordan, Cramer's Rule, Inverse method with 2D/3D plots.", "⚖️ Systems of Linear Equations"),
        ("🏹", "Vectors & Transforms", "Dot/cross products, projections, and 2D transformation animator.", "🏹 Vectors & Transformations"),
        ("🌌", "Vector Spaces", "Subspaces, Rank-Nullity theorem, Gram-Schmidt orthonormalization.", "🌌 Vector Spaces & Subspaces"),
        ("💎", "Determinants", "Cofactor expansion, adjugate, and parallelogram/volume visualizer.", "💎 Determinants & Inverses"),
        ("⚡", "Eigenvalues", "Characteristic polynomial, diagonalization, Cayley-Hamilton theorem.", "⚡ Eigenvalues & Eigenvectors"),
        ("🎓", "Syllabus Solvers", "GF(2), Change of Basis, Inner Products, Jordan Canonical Form.", "🎓 Advanced Syllabus Solvers"),
    ]

    for i in range(0, len(modules), 4):
        cols = st.columns(4, gap="small")
        for j, col in enumerate(cols):
            idx = i + j
            if idx < len(modules):
                icon, title, desc, key = modules[idx]
                with col:
                    st.markdown(f"""
                        <div class="mod-card">
                            <div class="icon">{icon}</div>
                            <h4>{title}</h4>
                            <p>{desc}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    if st.button("Open →", key=f"dash_{idx}", use_container_width=True):
                        st.session_state["selected_module"] = key
                        st.rerun()
