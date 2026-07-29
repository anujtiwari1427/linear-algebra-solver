import streamlit as st

def apply_custom_css():
    """Applies premium dark glassmorphism theme with animations and polished UI."""
    st.markdown("""
        <style>
        /* ── Google Fonts ── */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Fira+Code:wght@400;500;600&family=Space+Grotesk:wght@400;500;600;700&display=swap');

        /* ── Global Reset & Typography ── */
        html, body, [class*="css"], .stApp {
            font-family: 'Inter', sans-serif;
            background: #080C18;
        }

        /* ── Animated Gradient Background ── */
        .stApp {
            background: radial-gradient(ellipse at 20% 10%, rgba(99,102,241,0.08) 0%, transparent 50%),
                        radial-gradient(ellipse at 80% 80%, rgba(168,85,247,0.06) 0%, transparent 50%),
                        radial-gradient(ellipse at 50% 50%, rgba(16,185,129,0.03) 0%, transparent 70%),
                        #080C18;
        }

        /* ── Sidebar Overhaul ── */
        section[data-testid="stSidebar"] {
            background: rgba(10, 14, 28, 0.95) !important;
            border-right: 1px solid rgba(99, 102, 241, 0.2) !important;
            backdrop-filter: blur(20px);
        }
        section[data-testid="stSidebar"] > div {
            padding-top: 0 !important;
        }

        /* ── Sidebar Brand Header ── */
        .sidebar-brand {
            background: linear-gradient(135deg, rgba(99,102,241,0.2) 0%, rgba(168,85,247,0.15) 50%, rgba(236,72,153,0.1) 100%);
            border-bottom: 1px solid rgba(99,102,241,0.25);
            padding: 20px 16px 16px 16px;
            margin-bottom: 8px;
            position: relative;
            overflow: hidden;
        }
        .sidebar-brand::before {
            content: '';
            position: absolute;
            top: -30px; left: -20px;
            width: 120px; height: 120px;
            background: radial-gradient(circle, rgba(99,102,241,0.3), transparent 70%);
            pointer-events: none;
        }
        .sidebar-brand h1 {
            margin: 0;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 50%, #EC4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }
        .sidebar-brand p {
            margin: 4px 0 0 0;
            color: #6B7280;
            font-size: 0.72rem;
            font-weight: 500;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }
        .sidebar-brand .version-badge {
            display: inline-block;
            background: rgba(99,102,241,0.15);
            color: #818CF8;
            border: 1px solid rgba(129,140,248,0.3);
            border-radius: 12px;
            padding: 2px 8px;
            font-size: 0.65rem;
            font-weight: 600;
            margin-top: 6px;
        }

        /* ── Sidebar Nav Groups ── */
        .nav-group-label {
            padding: 10px 16px 4px 16px;
            font-size: 0.65rem;
            font-weight: 700;
            color: #4B5563;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* ── Sidebar selectbox styling ── */
        .stSelectbox > div > div {
            background: rgba(255,255,255,0.04) !important;
            border: 1px solid rgba(99,102,241,0.2) !important;
            border-radius: 10px !important;
            color: #E5E7EB !important;
            font-size: 0.88rem !important;
            transition: border-color 0.2s ease !important;
        }
        .stSelectbox > div > div:hover {
            border-color: rgba(99,102,241,0.5) !important;
        }
        .stSelectbox > div > div:focus-within {
            border-color: #6366F1 !important;
            box-shadow: 0 0 0 2px rgba(99,102,241,0.15) !important;
        }

        /* ── Module Landing Dashboard ── */
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 16px;
            margin-top: 12px;
        }
        .module-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 16px;
            padding: 20px 22px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4,0,0.2,1);
            position: relative;
            overflow: hidden;
        }
        .module-card::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(99,102,241,0.05) 0%, transparent 60%);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .module-card:hover {
            border-color: rgba(99,102,241,0.4);
            transform: translateY(-3px);
            box-shadow: 0 12px 40px rgba(99,102,241,0.15);
        }
        .module-card:hover::before { opacity: 1; }
        .module-card .card-icon {
            font-size: 2rem;
            margin-bottom: 12px;
            display: block;
        }
        .module-card h3 {
            margin: 0 0 6px 0;
            color: #F3F4F6;
            font-size: 1rem;
            font-weight: 700;
        }
        .module-card p {
            margin: 0;
            color: #6B7280;
            font-size: 0.8rem;
            line-height: 1.5;
        }
        .module-card .card-tags {
            margin-top: 12px;
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
        }
        .card-tag {
            background: rgba(99,102,241,0.1);
            color: #818CF8;
            border: 1px solid rgba(129,140,248,0.2);
            border-radius: 6px;
            padding: 2px 8px;
            font-size: 0.68rem;
            font-weight: 600;
        }

        /* ── Module Header Banner (enhanced) ── */
        .module-banner {
            background: linear-gradient(135deg, rgba(99,102,241,0.12) 0%, rgba(168,85,247,0.08) 100%);
            border: 1px solid rgba(99,102,241,0.2);
            border-left: 5px solid #6366F1;
            border-radius: 14px;
            padding: 18px 22px;
            margin-bottom: 22px;
            position: relative;
            overflow: hidden;
        }
        .module-banner::after {
            content: '';
            position: absolute;
            right: -30px; top: -30px;
            width: 120px; height: 120px;
            background: radial-gradient(circle, rgba(99,102,241,0.15), transparent 70%);
            pointer-events: none;
        }
        .module-banner h2 {
            margin: 0 0 4px 0;
            color: #F3F4F6;
            font-size: 1.5rem;
            font-weight: 800;
            font-family: 'Space Grotesk', sans-serif;
        }
        .module-banner p {
            margin: 0;
            color: #9CA3AF;
            font-size: 0.88rem;
            line-height: 1.5;
        }

        /* ── Tabs (enhanced) ── */
        .stTabs [data-baseweb="tab-list"] {
            background: rgba(255,255,255,0.03) !important;
            border-radius: 12px !important;
            padding: 4px !important;
            border: 1px solid rgba(255,255,255,0.07) !important;
            gap: 2px !important;
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 8px !important;
            font-size: 0.83rem !important;
            font-weight: 600 !important;
            padding: 7px 16px !important;
            color: #9CA3AF !important;
            transition: all 0.2s ease !important;
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #6366F1, #7C3AED) !important;
            color: #FFFFFF !important;
            box-shadow: 0 4px 12px rgba(99,102,241,0.4) !important;
        }
        .stTabs [data-baseweb="tab-panel"] {
            padding-top: 20px !important;
        }

        /* ── Metric Cards ── */
        .stMetric {
            background: rgba(255,255,255,0.03) !important;
            border: 1px solid rgba(255,255,255,0.07) !important;
            border-radius: 12px !important;
            padding: 12px 16px !important;
        }
        .stMetric label {
            color: #6B7280 !important;
            font-size: 0.75rem !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
        }
        .stMetric [data-testid="stMetricValue"] {
            color: #F3F4F6 !important;
            font-family: 'Fira Code', monospace !important;
            font-size: 1.3rem !important;
            font-weight: 700 !important;
        }

        /* ── Metric Badge (pill) ── */
        .metric-badge {
            display: inline-block;
            background: rgba(99,102,241,0.12);
            color: #818CF8;
            border: 1px solid rgba(129,140,248,0.3);
            border-radius: 20px;
            padding: 4px 12px;
            font-size: 0.8rem;
            font-weight: 600;
            margin: 3px 4px 3px 0;
            transition: all 0.2s ease;
        }

        /* ── Info / Success / Error boxes ── */
        .stAlert {
            border-radius: 10px !important;
            border-width: 1px !important;
        }

        /* ── Buttons ── */
        .stButton > button {
            background: linear-gradient(135deg, rgba(99,102,241,0.15), rgba(168,85,247,0.1)) !important;
            border: 1px solid rgba(99,102,241,0.3) !important;
            border-radius: 8px !important;
            color: #C7D2FE !important;
            font-weight: 600 !important;
            font-size: 0.8rem !important;
            transition: all 0.25s cubic-bezier(0.4,0,0.2,1) !important;
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, rgba(99,102,241,0.3), rgba(168,85,247,0.2)) !important;
            border-color: #6366F1 !important;
            box-shadow: 0 4px 16px rgba(99,102,241,0.3) !important;
            transform: translateY(-1px) !important;
            color: #FFFFFF !important;
        }
        .stButton > button:active { transform: translateY(0) !important; }

        /* ── Data Editor ── */
        .stDataEditor [data-testid="stDataFrameResizable"] {
            border: 1px solid rgba(99,102,241,0.2) !important;
            border-radius: 10px !important;
            overflow: hidden;
        }

        /* ── Divider ── */
        hr {
            border-color: rgba(255,255,255,0.06) !important;
            margin: 20px 0 !important;
        }

        /* ── Number inputs ── */
        .stNumberInput input {
            text-align: center;
            font-family: 'Fira Code', monospace;
            font-weight: 600;
            background: rgba(255,255,255,0.04) !important;
            border-color: rgba(99,102,241,0.25) !important;
            border-radius: 8px !important;
            color: #F3F4F6 !important;
        }

        /* ── Scrollbar ── */
        ::-webkit-scrollbar { width: 4px; height: 4px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(99,102,241,0.4); border-radius: 4px; }

        /* ── Gradient accent text ── */
        .gradient-text {
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 50%, #EC4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }

        /* ── Section header divider ── */
        .section-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin: 18px 0 12px 0;
        }
        .section-header h4 {
            margin: 0;
            font-size: 0.85rem;
            font-weight: 700;
            color: #9CA3AF;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            white-space: nowrap;
        }
        .section-header .divider-line {
            flex: 1;
            height: 1px;
            background: rgba(255,255,255,0.07);
        }

        /* ── Step box for step-by-step math ── */
        .step-box {
            background: rgba(15,23,42,0.6);
            border: 1px solid rgba(51,65,85,0.8);
            border-radius: 10px;
            padding: 14px 18px;
            margin: 12px 0;
            font-family: 'Fira Code', monospace;
        }

        /* ── Popover content ── */
        .stPopover [data-testid="stPopoverBody"] {
            background: rgba(15,20,40,0.98) !important;
            border: 1px solid rgba(99,102,241,0.25) !important;
            border-radius: 12px !important;
        }
        </style>
    """, unsafe_allow_html=True)


def render_banner(title: str, description: str, icon: str = "📐"):
    """Renders an enhanced top banner for each module."""
    st.markdown(f"""
        <div class="module-banner">
            <h2>{icon} {title}</h2>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)


def render_section_header(title: str):
    """Renders a styled section divider with heading."""
    st.markdown(f"""
        <div class="section-header">
            <h4>{title}</h4>
            <div class="divider-line"></div>
        </div>
    """, unsafe_allow_html=True)


def render_home_dashboard():
    """Renders the main dashboard with module cards."""
    st.markdown("""
        <div style="text-align:center; padding: 30px 0 10px 0;">
            <h1 style="font-family:'Space Grotesk',sans-serif; font-size:2.8rem; font-weight:900;
                       background:linear-gradient(135deg,#6366F1,#A855F7,#EC4899);
                       -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin:0;">
                Linear Algebra Suite
            </h1>
            <p style="color:#6B7280; font-size:1rem; margin-top:8px; font-weight:400;">
                Interactive Python solver & visualizer for university-level linear algebra
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    modules = [
        {
            "icon": "📷",
            "title": "Image Question Solver (OCR)",
            "desc": "Upload textbook photos or screenshots. ML-powered OCR extracts and solves matrix problems automatically.",
            "tags": ["OCR", "EasyOCR", "Auto-Solve"],
            "key": "📷 Image Question Solver (OCR)"
        },
        {
            "icon": "🧮",
            "title": "Matrix Operations & Properties",
            "desc": "Arithmetic, transpose, power, LU / QR / SVD / Cholesky decompositions, and structural classification.",
            "tags": ["LU", "QR", "SVD", "Cholesky"],
            "key": "🧮 Matrix Operations & Properties"
        },
        {
            "icon": "⚖️",
            "title": "Systems of Linear Equations",
            "desc": "Gauss-Jordan RREF, Cramer's Rule, and Inverse method with 2D/3D intersection visualizer.",
            "tags": ["Gauss-Jordan", "Cramer's Rule", "2D/3D"],
            "key": "⚖️ Systems of Linear Equations"
        },
        {
            "icon": "🏹",
            "title": "Vectors & Transformations",
            "desc": "Dot/cross products, projections, norms, and 2D grid morphing animation under transformation matrix.",
            "tags": ["Dot Product", "Cross Product", "Animation"],
            "key": "🏹 Vectors & Transformations"
        },
        {
            "icon": "🌌",
            "title": "Vector Spaces & Subspaces",
            "desc": "Linear independence, four fundamental subspaces, Rank-Nullity theorem, and Gram-Schmidt process.",
            "tags": ["Null Space", "Rank-Nullity", "Gram-Schmidt"],
            "key": "🌌 Vector Spaces & Subspaces"
        },
        {
            "icon": "💎",
            "title": "Determinants & Inverses",
            "desc": "Cofactor expansion, adjugate matrix, and geometric area/volume interpretation of determinants.",
            "tags": ["Cofactor", "Adjugate", "Area/Volume"],
            "key": "💎 Determinants & Inverses"
        },
        {
            "icon": "⚡",
            "title": "Eigenvalues & Eigenvectors",
            "desc": "Characteristic polynomials, diagonalization, Cayley-Hamilton theorem, and minimal polynomial.",
            "tags": ["Eigenvalues", "Diagonalization", "Cayley-Hamilton"],
            "key": "⚡ Eigenvalues & Eigenvectors"
        },
        {
            "icon": "🎓",
            "title": "Advanced Syllabus Solvers",
            "desc": "GF(2) field, Change of Basis, General Inner Product Spaces, and Jordan Canonical Form.",
            "tags": ["GF(2)", "Jordan Form", "Cauchy-Schwarz"],
            "key": "🎓 Advanced Syllabus Solvers"
        },
    ]

    # 4-column grid
    cols_per_row = 4
    for i in range(0, len(modules), cols_per_row):
        row_cols = st.columns(cols_per_row)
        for j, col in enumerate(row_cols):
            idx = i + j
            if idx < len(modules):
                m = modules[idx]
                tags_html = "".join([f'<span class="card-tag">{t}</span>' for t in m["tags"]])
                with col:
                    st.markdown(f"""
                        <div class="module-card">
                            <span class="card-icon">{m["icon"]}</span>
                            <h3>{m["title"]}</h3>
                            <p>{m["desc"]}</p>
                            <div class="card-tags">{tags_html}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Open {m['icon']}", key=f"home_btn_{idx}", use_container_width=True):
                        st.session_state["selected_module"] = m["key"]
                        st.rerun()
