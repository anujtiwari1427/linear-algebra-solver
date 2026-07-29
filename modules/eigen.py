import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go
from utils.style import render_banner
from utils.helpers import render_matrix_input, to_sympy_matrix, display_matrix_latex
from utils.min_poly import matrix_minimal_poly

def render_eigen_module():
    render_banner(
        "Eigenvalues & Eigenvectors",
        "Compute characteristic polynomials, real/complex eigenvalues, eigenspaces, matrix diagonalization (A = P D P⁻¹), and visualize eigenvector invariance.",
        "⚡"
    )

    tab1, tab2, tab3, tab4 = st.tabs([
        "🔬 Characteristic Polynomial & Eigenspaces",
        "🔀 Matrix Diagonalization & Powers",
        "📜 Cayley-Hamilton & Minimal Polynomial",
        "🧭 Eigenvector Span Transformation Plot"
    ])

    # ---------------- TAB 1: EIGENVALUES & EIGENVECTORS ----------------
    with tab1:
        n = st.number_input("Matrix Size (n × n)", min_value=2, max_value=5, value=2, step=1, key="eig_n")
        mat_a = render_matrix_input("eig_mat", rows=n, cols=n, default_vals=np.array([[3.0, 1.0], [1.0, 3.0]]) if n == 2 else None, label="Square Matrix A")

        sp_a = to_sympy_matrix(mat_a)
        lam = sp.Symbol('\\lambda')
        char_poly = sp_a.charpoly(lam)

        st.divider()
        st.write("#### 1. Characteristic Polynomial $\\det(A - \\lambda I) = 0$:")
        st.latex(f"P(\\lambda) = {sp.latex(char_poly.as_expr())} = 0")

        st.write("#### 2. Eigenvalues & Eigenspaces:")
        try:
            eigen_info = sp_a.eigenvects()
            for i, (val, mult, vecs) in enumerate(eigen_info):
                st.markdown(f"**Eigenvalue $\\lambda_{{{i+1}}} = {sp.latex(val)}$** (Algebraic Multiplicity: `{mult}`):")
                for j, vec in enumerate(vecs):
                    st.latex(f"\\vec{{v}}_{{{i+1},{j+1}}} = {sp.latex(vec)}")
        except Exception as e:
            st.error(f"Error computing symbolic eigenvectors: {e}")

    # ---------------- TAB 2: DIAGONALIZATION ----------------
    with tab2:
        st.subheader("Matrix Diagonalization $A = P D P^{-1}$")
        sp_a = to_sympy_matrix(mat_a)

        try:
            if sp_a.is_diagonalizable():
                P, D = sp_a.diagonalize()
                st.success("✅ **Matrix A is Diagonalizable!**")
                
                c1, c2 = st.columns(2)
                with c1:
                    st.write("**Modal Matrix P (Columns are Eigenvectors):**")
                    st.latex(f"P = {sp.latex(P)}")
                with c2:
                    st.write("**Diagonal Matrix D (Diagonal entries are Eigenvalues):**")
                    st.latex(f"D = {sp.latex(D)}")

                st.divider()
                st.write("#### Compute Matrix Power $A^k = P D^k P^{-1}$:")
                k_exp = st.number_input("Exponent k", min_value=1, max_value=20, value=5, key="eig_k")
                D_k = D**k_exp
                A_k = P * D_k * P.inv()
                st.latex(f"A^{{{k_exp}}} = P \\cdot D^{{{k_exp}}} \\cdot P^{{-1}} = {sp.latex(A_k)}")
            else:
                st.warning("⚠️ Matrix A is **Not Diagonalizable** (Defective matrix: total independent eigenvectors < n).")
        except Exception as e:
            st.error(f"Diagonalization check error: {e}")

    # ---------------- TAB 3: CAYLEY-HAMILTON & MINIMAL POLY ----------------
    with tab3:
        st.subheader("Cayley-Hamilton Theorem & Minimal Polynomial")
        st.write("The **Cayley-Hamilton Theorem** states that every square matrix $A$ satisfies its own characteristic equation:")
        st.latex(r"P(A) = a_n A^n + a_{n-1} A^{n-1} + \dots + a_1 A + a_0 I = \mathbf{0}")

        sp_a = to_sympy_matrix(mat_a)
        lam = sp.Symbol('\\lambda')
        char_poly = sp_a.charpoly(lam)
        coeffs = char_poly.all_coeffs()

        # Evaluate P(A) matrix sum
        pa_mat = sp.zeros(n, n)
        degree = len(coeffs) - 1
        for idx, c in enumerate(coeffs):
            power = degree - idx
            pa_mat += c * (sp_a**power)

        st.write("**Evaluating $P(A)$ Matrix Sum:**")
        st.latex(f"P(A) = {sp.latex(pa_mat)}")
        if pa_mat == sp.zeros(n, n):
            st.success("✅ **Cayley-Hamilton Theorem Verified!** $P(A) = \\mathbf{0}$ zero matrix.")

        st.divider()
        st.write("#### Minimal Polynomial $m(\\lambda)$:")
        try:
            min_poly_expr = matrix_minimal_poly(sp_a, lam)
            st.latex(f"m(\\lambda) = {sp.latex(min_poly_expr)}")
            st.caption("The minimal polynomial is the monic polynomial of lowest degree such that m(A) = 0.")
        except Exception as e:
            st.warning(f"Minimal polynomial could not be computed: {e}")

    # ---------------- TAB 4: EIGENVECTOR TRANSFORMATION PLOT ----------------
    with tab4:
        st.subheader("Visualizing Eigenvector Directional Invariance $A \\vec{v} = \\lambda \\vec{v}$")
        st.caption("Eigenvectors remain strictly on their original directional line under matrix transformation A, only scaled by factor λ.")

        if n != 2:
            st.info("Interactive eigenvector span visualizer is provided for 2 × 2 matrices.")
        else:
            evals, evecs = np.linalg.eig(mat_a)
            st.write(f"**Eigenvalues**: $\\lambda_1 = {evals[0]:.2f}, \\quad \\lambda_2 = {evals[1]:.2f}$")

            # Create a grid of directional vectors on unit circle
            angles = np.linspace(0, 2*np.pi, 24)
            unit_vecs = np.vstack([np.cos(angles), np.sin(angles)])
            trans_vecs = mat_a @ unit_vecs

            fig_e = go.Figure()

            # Plot transformed unit vectors (grey dashed)
            for i in range(unit_vecs.shape[1]):
                u_x, u_y = unit_vecs[0, i], unit_vecs[1, i]
                t_x, t_y = trans_vecs[0, i], trans_vecs[1, i]
                fig_e.add_trace(go.Scatter(x=[0, u_x], y=[0, u_y], mode='lines', line=dict(color='rgba(156, 163, 175, 0.4)', dash='dot'), showlegend=False))
                fig_e.add_trace(go.Scatter(x=[0, t_x], y=[0, t_y], mode='lines', line=dict(color='rgba(156, 163, 175, 0.6)'), showlegend=False))

            # Highlight Eigenvector 1
            if np.isreal(evals[0]):
                v1 = np.real(evecs[:, 0])
                v1_t = mat_a @ v1
                fig_e.add_trace(go.Scatter(x=[0, v1[0]], y=[0, v1[1]], mode='lines+markers', name=f'Eigenvector v₁ (λ₁={evals[0]:.2f})', line=dict(color='#6366F1', width=5)))
                fig_e.add_trace(go.Scatter(x=[0, v1_t[0]], y=[0, v1_t[1]], mode='lines+markers', name=f'Transformed A v₁', line=dict(color='#A855F7', width=5, dash='dash')))

            # Highlight Eigenvector 2
            if np.isreal(evals[1]):
                v2 = np.real(evecs[:, 1])
                v2_t = mat_a @ v2
                fig_e.add_trace(go.Scatter(x=[0, v2[0]], y=[0, v2[1]], mode='lines+markers', name=f'Eigenvector v₂ (λ₂={evals[1]:.2f})', line=dict(color='#10B981', width=5)))
                fig_e.add_trace(go.Scatter(x=[0, v2_t[0]], y=[0, v2_t[1]], mode='lines+markers', name=f'Transformed A v₂', line=dict(color='#F59E0B', width=5, dash='dash')))

            fig_e.update_layout(template="plotly_white", title="Eigenvectors Directional Invariance under A", xaxis=dict(range=[-5, 5]), yaxis=dict(range=[-5, 5]), height=550)
            st.plotly_chart(fig_e, use_container_width=True)
