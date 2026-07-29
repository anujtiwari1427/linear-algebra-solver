import streamlit as st

def apply_custom_css():
    """Applies custom CSS for a modern, sleek dark glassmorphism theme."""
    st.markdown("""
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=Fira+Code:wght@400;500;600&display=swap');

        /* Root styling & typography */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* Glassmorphic Cards */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 20px 24px;
            margin-bottom: 20px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.25);
            transition: all 0.3s ease;
        }
        .glass-card:hover {
            border-color: rgba(99, 102, 241, 0.4);
            box-shadow: 0 12px 40px 0 rgba(99, 102, 241, 0.15);
        }

        /* Gradient Accent Text */
        .gradient-text {
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 50%, #EC4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }

        /* Module Header Banner */
        .module-banner {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%);
            border-left: 5px solid #6366F1;
            border-radius: 12px;
            padding: 16px 20px;
            margin-bottom: 24px;
        }
        .module-banner h2 {
            margin: 0;
            color: #F3F4F6;
            font-size: 1.6rem;
            font-weight: 700;
        }
        .module-banner p {
            margin: 4px 0 0 0;
            color: #9CA3AF;
            font-size: 0.95rem;
        }

        /* Metric Badge */
        .metric-badge {
            display: inline-block;
            background: rgba(99, 102, 241, 0.12);
            color: #818CF8;
            border: 1px solid rgba(129, 140, 248, 0.3);
            border-radius: 20px;
            padding: 4px 12px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-right: 8px;
        }

        /* Step box for step-by-step math */
        .step-box {
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(51, 65, 85, 0.8);
            border-radius: 10px;
            padding: 14px 18px;
            margin: 12px 0;
            font-family: 'Fira Code', monospace;
        }

        /* Custom matrix input styling */
        .stNumberInput input {
            text-align: center;
            font-family: 'Fira Code', monospace;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

def render_banner(title: str, description: str, icon: str = "📐"):
    """Renders a sleek top banner for each module."""
    st.markdown(f"""
        <div class="module-banner">
            <h2>{icon} {title}</h2>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)
