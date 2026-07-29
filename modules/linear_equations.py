import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go
from utils.style import render_banner
from utils.helpers import render_matrix_input, render_vector_input, to_sympy_matrix, display_matrix_latex

def render_linear_equations_module():
    render_banner(
        "Systems of Linear Equations",
        "Solve systems of equations Ax = b with step-by-step row reduction, inverse method, Cramer's rule, and 2D/3D geometric line/plane intersection visualizer.",
        "⚖️"
    )

    n = st.number_input("Number of Unknowns / Equations (n)", min_value=2, max_value=6, value=3, step=1)

    c1, c2 = st.columns([3, 2])
    with c1:
        st.subheader("Coefficient Matrix A")
        mat_a = render_matrix_input("eq_mat_a", rows=n, cols=n, label="Matrix A")
    with c2:
        st.subheader("Constants Vector b")
        vec_b = render_vector_input("eq_vec_b", size=n, label="Vector b")

    st.divider()

    # Formulate augmented matrix [A | b]
    aug_mat = np.hstack([mat_a, vec_b.reshape(-1, 1)])
    st.write("#### Augmented Matrix $[A \\mid b]$:")
    st.latex(f"[A \\mid b] = {sp.latex(to_sympy_matrix(aug_mat))}")

    # Tabs for methods and visualizer
    tab_gauss, tab_inv, tab_cramer, tab_vis = st.tabs([
        "🔄 Gauss-Jordan Step-by-Step",
        "🔲 Matrix Inverse Method",
        "📐 Cramer's Rule",
        "🌐 Geometric Visualizer (2D/3D)"
    ])

    # ---------------- GAUSS-JORDAN ----------------
    with tab_gauss:
        st.subheader("Gauss-Jordan Row Reduction Steps")
        sp_aug = to_sympy_matrix(aug_mat)
        rref_mat, pivot_cols = sp_aug.rref()
        
        st.write("Applying elementary row operations to achieve Reduced Row Echelon Form (RREF)...")
        st.latex(f"\\text{{RREF}}([A \\mid b]) = {sp.latex(rref_mat)}")

        rank_a = np.linalg.matrix_rank(mat_a)
        rank_aug = np.linalg.matrix_rank(aug_mat)

        if rank_a == rank_aug == n:
            st.success("✅ **Unique Solution Exists!**")
            solution = rref_mat[:, -1]
            sol_vars = [f"x_{{{i+1}}} = {sp.latex(val)}" for i, val in enumerate(solution)]
            st.latex(", \\quad ".join(sol_vars))
        elif rank_a < rank_aug:
            st.error("❌ **No Solution (Inconsistent System)**: Rank(A) < Rank([A|b]). The system represents parallel non-intersecting planes/lines.")
        else:
            st.warning(f"♾️ **Infinitely Many Solutions**: Rank(A) = {rank_a} < n ({n}). Free parameters exist.")

    # ---------------- MATRIX INVERSE ----------------
    with tab_inv:
        st.subheader("Solution via Matrix Inverse $x = A^{-1} b$")
        det_a = np.linalg.det(mat_a)
        if abs(det_a) < 1e-9:
            st.error(r"⚠️ Matrix A is singular ($\det(A) = 0$). Inverse $A^{-1}$ does not exist!")
        else:
            inv_a = np.linalg.inv(mat_a)
            st.write("**Inverse Matrix $A^{-1}$:**")
            display_matrix_latex(inv_a, "A^{-1}")
            
            x_sol = inv_a @ vec_b
            st.latex(f"x = A^{{-1}} b = {sp.latex(to_sympy_matrix(x_sol.reshape(-1, 1)))}")

    # ---------------- CRAMER'S RULE ----------------
    with tab_cramer:
        st.subheader("Cramer's Rule")
        det_a = np.linalg.det(mat_a)
        st.write(rf"**Determinant of A**: $\det(A) = {det_a:.4f}$")

        if abs(det_a) < 1e-9:
            st.error(r"Cramer's rule is only applicable when $\det(A) \neq 0$.")
        else:
            sols = []
            for i in range(n):
                mat_ai = mat_a.copy()
                mat_ai[:, i] = vec_b
                det_ai = np.linalg.det(mat_ai)
                xi = det_ai / det_a
                sols.append(xi)
                st.latex(f"x_{{{i+1}}} = \\frac{{\\det(A_{{{i+1}}}={sp.latex(to_sympy_matrix(mat_ai))})}}{{\\det(A)}} = \\frac{{{det_ai:.4f}}}{{{det_a:.4f}}} = {xi:.4f}")

    # ---------------- GEOMETRIC VISUALIZER ----------------
    with tab_vis:
        st.subheader("Geometric Representation")
        if n == 2:
            st.write("#### 2D Intersection of Lines")
            # a11 x + a12 y = b1  => y = (b1 - a11 x) / a12
            x_vals = np.linspace(-10, 10, 200)
            fig = go.Figure()

            # Line 1
            if abs(mat_a[0, 1]) > 1e-5:
                y1 = (vec_b[0] - mat_a[0, 0] * x_vals) / mat_a[0, 1]
                fig.add_trace(go.Scatter(x=x_vals, y=y1, mode='lines', name=f'{mat_a[0,0]}x + {mat_a[0,1]}y = {vec_b[0]}'))
            else:
                fig.add_vline(x=vec_b[0]/mat_a[0,0], name="Line 1")

            # Line 2
            if abs(mat_a[1, 1]) > 1e-5:
                y2 = (vec_b[1] - mat_a[1, 0] * x_vals) / mat_a[1, 1]
                fig.add_trace(go.Scatter(x=x_vals, y=y2, mode='lines', name=f'{mat_a[1,0]}x + {mat_a[1,1]}y = {vec_b[1]}'))
            else:
                fig.add_vline(x=vec_b[1]/mat_a[1,0], name="Line 2")

            # Intersection point
            if abs(np.linalg.det(mat_a)) > 1e-5:
                sol = np.linalg.solve(mat_a, vec_b)
                fig.add_trace(go.Scatter(x=[sol[0]], y=[sol[1]], mode='markers', marker=dict(size=12, color='red', symbol='cross'), name=f'Intersection ({sol[0]:.2f}, {sol[1]:.2f})'))

            fig.update_layout(template="plotly_dark", title="2D Linear System Lines", xaxis_title="x₁", yaxis_title="x₂", height=450)
            st.plotly_chart(fig, use_container_width=True)

        elif n == 3:
            st.write("#### 3D Plane Intersections")
            # Create a 3D grid
            x_range = np.linspace(-5, 5, 20)
            y_range = np.linspace(-5, 5, 20)
            X, Y = np.meshgrid(x_range, y_range)

            fig = go.Figure()
            colors = ['#6366F1', '#EC4899', '#10B981']

            for i in range(3):
                # a_i1 x + a_i2 y + a_i3 z = b_i  => z = (b_i - a_i1 x - a_i2 y) / a_i3
                if abs(mat_a[i, 2]) > 1e-5:
                    Z = (vec_b[i] - mat_a[i, 0] * X - mat_a[i, 1] * Y) / mat_a[i, 2]
                    fig.add_trace(go.Surface(x=X, y=Y, z=Z, opacity=0.6, colorscale=[[0, colors[i]], [1, colors[i]]], showscale=False, name=f'Plane {i+1}'))

            if abs(np.linalg.det(mat_a)) > 1e-5:
                sol = np.linalg.solve(mat_a, vec_b)
                fig.add_trace(go.Scatter3d(
                    x=[sol[0]], y=[sol[1]], z=[sol[2]],
                    mode='markers+text',
                    marker=dict(size=8, color='yellow'),
                    text=[f"Solution ({sol[0]:.2f}, {sol[1]:.2f}, {sol[2]:.2f})"],
                    name="Intersection Point"
                ))

            fig.update_layout(template="plotly_dark", scene=dict(xaxis_title='x₁', yaxis_title='x₂', zaxis_title='x₃'), height=550)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Geometric graph visualizer is available for 2D and 3D systems.")
