import streamlit as st
import numpy as np
import scipy.linalg as la
import sympy as sp
import plotly.express as px
import plotly.graph_objects as go
from utils.style import render_banner
from utils.helpers import render_matrix_input, to_sympy_matrix, display_matrix_latex

def render_matrix_ops_module():
    render_banner(
        "Matrix Operations & Properties",
        "Perform basic and advanced matrix arithmetic, evaluate fundamental properties, and compute decompositions (LU, QR, SVD, Cholesky).",
        "🧮"
    )

    tab1, tab2, tab3, tab4 = st.tabs([
        "🔢 Single Matrix Operations",
        "➕ Matrix Arithmetic (A & B)",
        "📊 Properties & Analysis",
        "🧱 Decompositions (LU, QR, SVD)"
    ])

    # ---------------- TAB 1: Single Matrix Ops ----------------
    with tab1:
        st.subheader("Matrix A Configuration")
        c1, c2 = st.columns(2)
        with c1:
            rows_a = st.number_input("Rows (A)", min_value=1, max_value=6, value=3, key="s_rows_a")
        with c2:
            cols_a = st.number_input("Columns (A)", min_value=1, max_value=6, value=3, key="s_cols_a")

        mat_a = render_matrix_input("single_mat_a", rows=rows_a, cols=cols_a, label="Matrix A")
        
        st.divider()
        st.write("#### Select Operation")
        op = st.radio(
            "Operation on A",
            ["Transpose (Aᵀ)", "Scalar Multiplication (c · A)", "Matrix Power (Aᵏ)", "Rank & Trace"],
            horizontal=True
        )

        if op == "Transpose (Aᵀ)":
            mat_a_t = mat_a.T
            st.latex(f"A^T = {sp.latex(to_sympy_matrix(mat_a_t))}")

        elif op == "Scalar Multiplication (c · A)":
            c_val = st.number_input("Scalar c", value=2.5, step=0.5)
            res = c_val * mat_a
            st.latex(f"{c_val} \\cdot A = {sp.latex(to_sympy_matrix(res))}")

        elif op == "Matrix Power (Aᵏ)":
            if rows_a != cols_a:
                st.error("⚠️ Matrix power requires a square matrix!")
            else:
                k_val = st.number_input("Exponent k", min_value=0, max_value=10, value=2, step=1)
                res = np.linalg.matrix_power(mat_a.astype(int if np.all(mat_a == mat_a.astype(int)) else float), k_val)
                st.latex(f"A^{{{k_val}}} = {sp.latex(to_sympy_matrix(res))}")

        elif op == "Rank & Trace":
            rank_val = np.linalg.matrix_rank(mat_a)
            st.info(f"**Rank of A**: `{rank_val}`")
            if rows_a == cols_a:
                trace_val = np.trace(mat_a)
                st.info(f"**Trace of A (sum of diagonal)**: `{trace_val:.4f}`")
            else:
                st.warning("Trace is only defined for square matrices.")

    # ---------------- TAB 2: Dual Matrix Ops (A & B) ----------------
    with tab2:
        st.subheader("Matrices A and B Setup")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            r_a = st.number_input("Rows (A)", 1, 6, 3, key="d_r_a")
        with c2:
            c_a = st.number_input("Cols (A)", 1, 6, 3, key="d_c_a")
        with c3:
            r_b = st.number_input("Rows (B)", 1, 6, 3, key="d_r_b")
        with c4:
            c_b = st.number_input("Cols (B)", 1, 6, 3, key="d_c_b")

        col_left, col_right = st.columns(2)
        with col_left:
            mat_a_dual = render_matrix_input("dual_mat_a", rows=r_a, cols=c_a, label="Matrix A")
        with col_right:
            mat_b_dual = render_matrix_input("dual_mat_b", rows=r_b, cols=c_b, label="Matrix B")

        st.divider()
        operation = st.selectbox(
            "Choose Operation",
            ["Addition (A + B)", "Subtraction (A - B)", "Multiplication (A × B)", "Hadamard Product (A ⊙ B)"]
        )

        if operation == "Addition (A + B)":
            if (r_a, c_a) != (r_b, c_b):
                st.error("⚠️ Addition requires matrices of the same dimensions!")
            else:
                res = mat_a_dual + mat_b_dual
                st.latex(f"A + B = {sp.latex(to_sympy_matrix(mat_a_dual))} + {sp.latex(to_sympy_matrix(mat_b_dual))} = {sp.latex(to_sympy_matrix(res))}")

        elif operation == "Subtraction (A - B)":
            if (r_a, c_a) != (r_b, c_b):
                st.error("⚠️ Subtraction requires matrices of the same dimensions!")
            else:
                res = mat_a_dual - mat_b_dual
                st.latex(f"A - B = {sp.latex(to_sympy_matrix(mat_a_dual))} - {sp.latex(to_sympy_matrix(mat_b_dual))} = {sp.latex(to_sympy_matrix(res))}")

        elif operation == "Multiplication (A × B)":
            if c_a != r_b:
                st.error(f"⚠️ Cannot multiply {r_a}x{c_a} matrix by {r_b}x{c_b} matrix! Columns of A ({c_a}) must equal Rows of B ({r_b}).")
            else:
                res = np.matmul(mat_a_dual, mat_b_dual)
                st.success(f"Result is a **{r_a} × {c_b}** matrix.")
                st.latex(f"A \\times B = {sp.latex(to_sympy_matrix(res))}")

        elif operation == "Hadamard Product (A ⊙ B)":
            if (r_a, c_a) != (r_b, c_b):
                st.error("⚠️ Hadamard product requires matrices of identical dimensions!")
            else:
                res = mat_a_dual * mat_b_dual
                st.latex(f"A \\odot B = {sp.latex(to_sympy_matrix(res))}")

    # ---------------- TAB 3: Properties & Classification ----------------
    with tab3:
        st.subheader("Matrix Classification & Structural Properties")
        r_p = st.number_input("Rows", 1, 6, 3, key="p_r")
        c_p = st.number_input("Cols", 1, 6, 3, key="p_c")
        mat_prop = render_matrix_input("prop_mat", rows=r_p, cols=c_p, label="Target Matrix A")

        st.divider()
        st.write("#### Classification Badges")
        
        badges = []
        is_square = (r_p == c_p)
        if is_square:
            badges.append("Square Matrix")
            # Symmetric check
            if np.allclose(mat_prop, mat_prop.T):
                badges.append("Symmetric Matrix")
            if np.allclose(mat_prop, -mat_prop.T):
                badges.append("Skew-Symmetric Matrix")
            # Identity check
            if np.allclose(mat_prop, np.eye(r_p)):
                badges.append("Identity Matrix")
            # Diagonal check
            if np.allclose(mat_prop, np.diag(np.diagonal(mat_prop))):
                badges.append("Diagonal Matrix")
            # Orthogonal check
            if np.allclose(mat_prop @ mat_prop.T, np.eye(r_p)):
                badges.append("Orthogonal Matrix (AᵀA = I)")
            # Invertibility check
            det_val = np.linalg.det(mat_prop)
            if abs(det_val) > 1e-9:
                badges.append(f"Invertible (det ≠ 0)")
            else:
                badges.append("Singular Matrix (det = 0)")
            # Definiteness for symmetric matrices
            if np.allclose(mat_prop, mat_prop.T):
                eigs = np.linalg.eigvals(mat_prop)
                if np.all(eigs > 1e-9):
                    badges.append("Positive Definite")
                elif np.all(eigs >= -1e-9):
                    badges.append("Positive Semi-Definite")
        else:
            badges.append("Rectangular Matrix")

        badge_html = "".join([f'<span class="metric-badge">{b}</span>' for b in badges])
        st.markdown(badge_html, unsafe_allow_html=True)

        st.divider()
        st.write("#### Numerical Summary")
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.metric("Rank", int(np.linalg.matrix_rank(mat_prop)))
        with col_m2:
            if is_square:
                st.metric("Determinant", f"{np.linalg.det(mat_prop):.4f}")
            else:
                st.metric("Determinant", "N/A")
        with col_m3:
            cond_num = np.linalg.cond(mat_prop)
            st.metric("Condition Number (L2)", f"{cond_num:.4e}")

    # ---------------- TAB 4: Decompositions ----------------
    with tab4:
        st.subheader("Matrix Decompositions")
        st.caption("Decompose matrix A into product of simpler canonical matrices.")

        r_d = st.number_input("Rows", 1, 6, 3, key="d_r")
        c_d = st.number_input("Cols", 1, 6, 3, key="d_c")
        mat_dec = render_matrix_input("dec_mat", rows=r_d, cols=c_d, label="Matrix A")

        decomp_type = st.selectbox(
            "Select Decomposition Method",
            ["LU Decomposition (P·L·U)", "QR Decomposition (Q·R)", "Singular Value Decomposition (SVD: U·Σ·Vᵀ)", "Cholesky Decomposition (L·Lᵀ)"]
        )

        if decomp_type == "LU Decomposition (P·L·U)":
            if r_d != c_d:
                st.error("LU Decomposition requires a square matrix.")
            else:
                try:
                    P, L, U = la.lu(mat_dec)
                    st.write("**Permutation Matrix P:**")
                    display_matrix_latex(P, "P")
                    st.write("**Lower Triangular Matrix L:**")
                    display_matrix_latex(L, "L")
                    st.write("**Upper Triangular Matrix U:**")
                    display_matrix_latex(U, "U")
                    st.success("Verification: $P \\cdot L \\cdot U = A$")
                except Exception as e:
                    st.error(f"LU decomposition error: {e}")

        elif decomp_type == "QR Decomposition (Q·R)":
            try:
                Q, R = np.linalg.qr(mat_dec)
                st.write("**Orthogonal Matrix Q (QᵀQ = I):**")
                display_matrix_latex(Q, "Q")
                st.write("**Upper Triangular Matrix R:**")
                display_matrix_latex(R, "R")
                st.success("Verification: $Q \\cdot R = A$")
            except Exception as e:
                st.error(f"QR decomposition error: {e}")

        elif decomp_type == "Singular Value Decomposition (SVD: U·Σ·Vᵀ)":
            try:
                U, S, Vt = np.linalg.svd(mat_dec)
                st.write("**Left Singular Vectors U:**")
                display_matrix_latex(U, "U")
                st.write("**Singular Values Σ (Diagonal):**")
                st.write([f"{val:.4f}" for val in S])
                st.write("**Right Singular Vectors Vᵀ:**")
                display_matrix_latex(Vt, "V^T")

                # Singular Values Bar Chart
                fig = px.bar(
                    x=[f"σ_{i+1}" for i in range(len(S))],
                    y=S,
                    title="Singular Values Spectrum",
                    labels={'x': 'Singular Value Index', 'y': 'Magnitude'},
                    color=S,
                    color_continuous_scale="Viridis"
                )
                fig.update_layout(template="plotly_dark", height=300)
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"SVD error: {e}")

        elif decomp_type == "Cholesky Decomposition (L·Lᵀ)":
            if r_d != c_d:
                st.error("Cholesky decomposition requires a square matrix.")
            elif not np.allclose(mat_dec, mat_dec.T):
                st.error("Cholesky decomposition requires a Symmetric matrix (A = Aᵀ).")
            else:
                try:
                    L = np.linalg.cholesky(mat_dec)
                    st.write("**Lower Triangular Matrix L:**")
                    display_matrix_latex(L, "L")
                    st.latex(f"L^T = {sp.latex(to_sympy_matrix(L.T))}")
                    st.success("Verification: $L \\cdot L^T = A$")
                except np.linalg.LinAlgError:
                    st.error("Matrix is not Positive Definite (all eigenvalues must be > 0).")
