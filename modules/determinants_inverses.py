import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go
from utils.style import render_banner
from utils.helpers import render_matrix_input, to_sympy_matrix, display_matrix_latex

def render_determinants_inverses_module():
    render_banner(
        "Determinants & Matrix Inverses",
        "Explore determinant calculation methods (Cofactor expansion, Row reduction), Adjugate matrix derivation, and 2D/3D geometric Area & Volume visualizers.",
        "💎"
    )

    tab1, tab2 = st.tabs(["🧮 Step-by-Step Determinant & Inverse", "🧊 Geometric Area & Volume"])

    # ---------------- TAB 1: STEP-BY-STEP DETERMINANT ----------------
    with tab1:
        n = st.number_input("Matrix Size (n × n)", min_value=2, max_value=5, value=3, step=1, key="det_n")
        mat_a = render_matrix_input("det_mat", rows=n, cols=n, label="Square Matrix A")

        st.divider()
        det_val = np.linalg.det(mat_a)
        st.write(f"### Determinant: $\\det(A) = {det_val:.4f}$")

        sp_a = to_sympy_matrix(mat_a)

        if n == 2:
            st.write("#### 2 × 2 Determinant Formula:")
            st.latex(f"\\det\\begin{{pmatrix}} a & b \\\\ c & d \\end{{pmatrix}} = ad - bc = ({mat_a[0,0]:.2f} \\times {mat_a[1,1]:.2f}) - ({mat_a[0,1]:.2f} \\times {mat_a[1,0]:.2f}) = {det_val:.4f}")
        elif n == 3:
            st.write("#### 3 × 3 Cofactor Expansion along Row 1:")
            a11, a12, a13 = mat_a[0, 0], mat_a[0, 1], mat_a[0, 2]
            m11 = mat_a[1:, [1, 2]]
            m12 = mat_a[1:, [0, 2]]
            m13 = mat_a[1:, [0, 1]]

            det11 = np.linalg.det(m11)
            det12 = np.linalg.det(m12)
            det13 = np.linalg.det(m13)

            st.latex(f"\\det(A) = {a11:.2f} \\det{sp.latex(to_sympy_matrix(m11))} - {a12:.2f} \\det{sp.latex(to_sympy_matrix(m12))} + {a13:.2f} \\det{sp.latex(to_sympy_matrix(m13))}")
            st.latex(f"\\det(A) = ({a11:.2f})({det11:.2f}) - ({a12:.2f})({det12:.2f}) + ({a13:.2f})({det13:.2f}) = {det_val:.4f}")

        # Cofactor & Adjugate Matrix
        if abs(det_val) > 1e-9:
            st.divider()
            st.write("#### Adjugate Matrix & Formula Inverse $A^{-1} = \\frac{1}{\\det(A)} \\text{adj}(A)$")

            cofactor_mat = sp_a.cofactor_matrix()
            adjugate_mat = sp_a.adjugate()
            inv_mat = sp_a.inv()

            col_c, col_adj = st.columns(2)
            with col_c:
                st.write("**Cofactor Matrix C:**")
                st.latex(f"C = {sp.latex(cofactor_mat)}")
            with col_adj:
                st.write("**Adjugate Matrix adj(A) = Cᵀ:**")
                st.latex(f"\\text{{adj}}(A) = {sp.latex(adjugate_mat)}")

            st.write("**Inverse Matrix $A^{-1}$:**")
            st.latex(f"A^{{-1}} = \\frac{{1}}{{{sp.latex(sp_a.det())}}} {sp.latex(adjugate_mat)} = {sp.latex(inv_mat)}")
        else:
            st.error(r"⚠️ Determinant is ZERO ($\det(A) = 0$). Matrix A is singular and cannot be inverted!")

    # ---------------- TAB 2: GEOMETRIC INTERPRETATION ----------------
    with tab2:
        st.subheader("Geometric Meaning of Determinant")
        dim = st.radio("Dimension", [2, 3], horizontal=True, key="geo_dim")

        if dim == 2:
            st.write("For a $2 \\times 2$ matrix, $|\\det(A)|$ represents the **Area of the Parallelogram** formed by column vectors $\\vec{c}_1$ and $\\vec{c}_2$.")
            mat_2d = render_matrix_input("geo_2d", rows=2, cols=2, default_vals=np.array([[3.0, 1.0], [1.0, 3.0]]))
            
            c1, c2 = mat_2d[:, 0], mat_2d[:, 1]
            area = abs(np.linalg.det(mat_2d))
            st.info(f"**Parallelogram Area**: `{area:.4f}` | **det(A)**: `{np.linalg.det(mat_2d):.4f}`")

            # Create Parallelogram polygon vertices: (0,0) -> c1 -> c1+c2 -> c2 -> (0,0)
            p_x = [0, c1[0], c1[0]+c2[0], c2[0], 0]
            p_y = [0, c1[1], c1[1]+c2[1], c2[1], 0]

            fig_p = go.Figure()
            # Parallelogram shape
            fig_p.add_trace(go.Scatter(x=p_x, y=p_y, mode='lines+markers', fill='toself', fillcolor='rgba(99, 102, 241, 0.4)', line=dict(color='#6366F1', width=3), name='Parallelogram Area'))
            # Vectors
            fig_p.add_trace(go.Scatter(x=[0, c1[0]], y=[0, c1[1]], mode='lines+text', name='Vector c₁', line=dict(color='#EC4899', width=4), text=["", "c1"]))
            fig_p.add_trace(go.Scatter(x=[0, c2[0]], y=[0, c2[1]], mode='lines+text', name='Vector c₂', line=dict(color='#10B981', width=4), text=["", "c2"]))

            fig_p.update_layout(template="plotly_white", title="2D Parallelogram Area", xaxis=dict(range=[-8, 8]), yaxis=dict(range=[-8, 8]), height=500)
            st.plotly_chart(fig_p, use_container_width=True)

        elif dim == 3:
            st.write("For a $3 \\times 3$ matrix, $|\\det(A)|$ represents the **Volume of the Parallelepiped** formed by 3 column vectors $\\vec{c}_1, \\vec{c}_2, \\vec{c}_3$.")
            mat_3d = render_matrix_input("geo_3d", rows=3, cols=3, default_vals=np.array([[2.0, 0.0, 0.0], [0.0, 3.0, 0.0], [0.0, 0.0, 2.5]]))

            c1, c2, c3 = mat_3d[:, 0], mat_3d[:, 1], mat_3d[:, 2]
            vol = abs(np.linalg.det(mat_3d))
            st.info(f"**Parallelepiped Volume**: `{vol:.4f}` | **det(A)**: `{np.linalg.det(mat_3d):.4f}`")

            # 3D Parallelepiped vertices
            vertices = np.array([
                [0, 0, 0],
                c1,
                c2,
                c1 + c2,
                c3,
                c1 + c3,
                c2 + c3,
                c1 + c2 + c3
            ])

            fig_v = go.Figure()
            # Plot column vectors
            fig_v.add_trace(go.Scatter3d(x=[0, c1[0]], y=[0, c1[1]], z=[0, c1[2]], mode='lines+markers', name='c₁', line=dict(color='#6366F1', width=6)))
            fig_v.add_trace(go.Scatter3d(x=[0, c2[0]], y=[0, c2[1]], z=[0, c2[2]], mode='lines+markers', name='c₂', line=dict(color='#EC4899', width=6)))
            fig_v.add_trace(go.Scatter3d(x=[0, c3[0]], y=[0, c3[1]], z=[0, c3[2]], mode='lines+markers', name='c₃', line=dict(color='#10B981', width=6)))

            fig_v.update_layout(template="plotly_white", title="3D Parallelepiped Volume Visualizer", height=550)
            st.plotly_chart(fig_v, use_container_width=True)
