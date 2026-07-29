import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go
from utils.style import render_banner
from utils.helpers import render_vector_input, render_matrix_input, to_sympy_matrix, display_matrix_latex

def render_vectors_transformations_module():
    render_banner(
        "Vectors & Linear Transformations",
        "Explore vector arithmetic, dot/cross products, projections, and visualize 2D/3D grid morphing under linear transformation matrices.",
        "🏹"
    )

    tab1, tab2 = st.tabs(["📐 Vector Operations & Plotter", "🌀 2D Linear Transformations"])

    # ---------------- TAB 1: VECTOR OPERATIONS ----------------
    with tab1:
        dim = st.radio("Vector Dimension", [2, 3], horizontal=True)

        col_u, col_v = st.columns(2)
        with col_u:
            st.subheader("Vector u")
            u = render_vector_input("vec_u", size=dim, default_vals=np.array([3.0, 1.0, 2.0][:dim]))
        with col_v:
            st.subheader("Vector v")
            v = render_vector_input("vec_v", size=dim, default_vals=np.array([1.0, 4.0, -1.0][:dim]))

        st.divider()

        # Vector calculations
        norm_u = np.linalg.norm(u)
        norm_v = np.linalg.norm(v)
        dot_uv = np.dot(u, v)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("||u|| (Euclidean Norm)", f"{norm_u:.4f}")
            st.metric("||u||₁ (L1 Norm)", f"{np.sum(np.abs(u)):.2f}")
        with col2:
            st.metric("||v|| (Euclidean Norm)", f"{norm_v:.4f}")
            st.metric("||v||∞ (L∞ Norm)", f"{np.max(np.abs(u)):.2f}")
        with col3:
            st.metric("Dot Product (u · v)", f"{dot_uv:.4f}")
            if norm_u > 1e-7 and norm_v > 1e-7:
                cos_theta = np.clip(dot_uv / (norm_u * norm_v), -1.0, 1.0)
                angle_rad = np.arccos(cos_theta)
                angle_deg = np.degrees(angle_rad)
                st.metric("Angle θ", f"{angle_deg:.2f}° ({angle_rad:.3f} rad)")

        st.write("#### Projection of u onto v")
        if norm_v > 1e-7:
            proj_uv = (dot_uv / (norm_v**2)) * v
            st.latex(f"\\text{{proj}}_{{\\vec{{v}}}}(\\vec{{u}}) = \\frac{{\\vec{{u}} \\cdot \\vec{{v}}}}{{\\|\\vec{{v}}\\|^2}} \\vec{{v}} = {sp.latex(to_sympy_matrix(proj_uv.reshape(-1, 1)))}")

        if dim == 3:
            cross_uv = np.cross(u, v)
            st.write("#### Cross Product (u × v)")
            st.latex(f"\\vec{{u}} \\times \\vec{{v}} = {sp.latex(to_sympy_matrix(cross_uv.reshape(-1, 1)))}")

        st.divider()
        st.write("#### Vector Visualization")

        fig = go.Figure()
        if dim == 2:
            # 2D plot
            fig.add_trace(go.Scatter(x=[0, u[0]], y=[0, u[1]], mode='lines+markers+text', name='Vector u', line=dict(color='#6366F1', width=4), text=["", "u"]))
            fig.add_trace(go.Scatter(x=[0, v[0]], y=[0, v[1]], mode='lines+markers+text', name='Vector v', line=dict(color='#EC4899', width=4), text=["", "v"]))
            # Addition u + v
            u_plus_v = u + v
            fig.add_trace(go.Scatter(x=[0, u_plus_v[0]], y=[0, u_plus_v[1]], mode='lines+markers+text', name='u + v', line=dict(color='#10B981', width=3, dash='dash'), text=["", "u+v"]))

            if norm_v > 1e-7:
                fig.add_trace(go.Scatter(x=[0, proj_uv[0]], y=[0, proj_uv[1]], mode='lines+markers+text', name='proj_v(u)', line=dict(color='#F59E0B', width=3), text=["", "proj"]))

            fig.update_layout(template="plotly_dark", title="2D Vector Plot", xaxis=dict(range=[-10, 10]), yaxis=dict(range=[-10, 10]), height=500)
            st.plotly_chart(fig, use_container_width=True)

        elif dim == 3:
            # 3D plot
            fig.add_trace(go.Scatter3d(x=[0, u[0]], y=[0, u[1]], z=[0, u[2]], mode='lines+markers+text', name='Vector u', line=dict(color='#6366F1', width=6), text=["", "u"]))
            fig.add_trace(go.Scatter3d(x=[0, v[0]], y=[0, v[1]], z=[0, v[2]], mode='lines+markers+text', name='Vector v', line=dict(color='#EC4899', width=6), text=["", "v"]))
            cross_uv = np.cross(u, v)
            fig.add_trace(go.Scatter3d(x=[0, cross_uv[0]], y=[0, cross_uv[1]], z=[0, cross_uv[2]], mode='lines+markers+text', name='u × v', line=dict(color='#10B981', width=5), text=["", "u×v"]))

            fig.update_layout(template="plotly_dark", title="3D Vector Plot", height=550)
            st.plotly_chart(fig, use_container_width=True)

    # ---------------- TAB 2: LINEAR TRANSFORMATIONS ----------------
    with tab2:
        st.subheader("2D Transformation Matrix T")

        preset = st.selectbox(
            "Transformation Presets",
            ["Custom", "Rotation (θ)", "Scaling (sx, sy)", "Shear X (k)", "Shear Y (k)", "Reflection (X-axis)", "Reflection (Y-axis)", "Projection onto X-axis"]
        )

        mat_t = np.eye(2)
        if preset == "Rotation (θ)":
            angle_deg = st.slider("Rotation Angle (degrees)", -180, 180, 45)
            rad = np.radians(angle_deg)
            mat_t = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
        elif preset == "Scaling (sx, sy)":
            sx = st.slider("Scale X", -3.0, 3.0, 1.5, 0.1)
            sy = st.slider("Scale Y", -3.0, 3.0, 0.8, 0.1)
            mat_t = np.array([[sx, 0], [0, sy]])
        elif preset == "Shear X (k)":
            k = st.slider("Shear factor k", -3.0, 3.0, 1.0, 0.1)
            mat_t = np.array([[1, k], [0, 1]])
        elif preset == "Shear Y (k)":
            k = st.slider("Shear factor k", -3.0, 3.0, 1.0, 0.1)
            mat_t = np.array([[1, 0], [k, 1]])
        elif preset == "Reflection (X-axis)":
            mat_t = np.array([[1, 0], [0, -1]])
        elif preset == "Reflection (Y-axis)":
            mat_t = np.array([[-1, 0], [0, 1]])
        elif preset == "Projection onto X-axis":
            mat_t = np.array([[1, 0], [0, 0]])
        else:
            mat_t = render_matrix_input("trans_mat", rows=2, cols=2, default_vals=np.array([[2.0, 1.0], [0.5, 1.5]]))

        st.write("**Transformation Matrix T:**")
        display_matrix_latex(mat_t, "T")
        st.write(f"**Determinant det(T)** = `{np.linalg.det(mat_t):.4f}` *(Area Scaling Factor)*")

        # Create original grid & shape (Unit Circle & Unit Square)
        theta = np.linspace(0, 2*np.pi, 100)
        circle_orig = np.vstack([np.cos(theta), np.sin(theta)])
        circle_trans = mat_t @ circle_orig

        square_orig = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]])
        square_trans = mat_t @ square_orig

        fig_t = go.Figure()

        # Plot original unit square
        fig_t.add_trace(go.Scatter(x=square_orig[0], y=square_orig[1], mode='lines', name='Original Unit Square', line=dict(color='#9CA3AF', dash='dash')))
        # Plot transformed unit square
        fig_t.add_trace(go.Scatter(x=square_trans[0], y=square_trans[1], mode='lines+markers', name='Transformed Square', fill='toself', fillcolor='rgba(99, 102, 241, 0.3)', line=dict(color='#6366F1', width=3)))

        # Plot unit circle & transformed ellipse
        fig_t.add_trace(go.Scatter(x=circle_orig[0], y=circle_orig[1], mode='lines', name='Original Unit Circle', line=dict(color='#6B7280', dash='dot')))
        fig_t.add_trace(go.Scatter(x=circle_trans[0], y=circle_trans[1], mode='lines', name='Transformed Shape', line=dict(color='#EC4899', width=2)))

        fig_t.update_layout(template="plotly_dark", title="2D Plane Grid Morphing", xaxis=dict(range=[-5, 5]), yaxis=dict(range=[-5, 5]), height=550)
        st.plotly_chart(fig_t, use_container_width=True)
