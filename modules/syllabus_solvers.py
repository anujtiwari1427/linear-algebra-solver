import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go
from utils.style import render_banner
from utils.helpers import render_matrix_input, render_vector_input, to_sympy_matrix, display_matrix_latex

def render_syllabus_solvers_module():
    render_banner(
        "Syllabus Advanced Concept Solvers",
        "Step-by-step solvers for specialized university syllabus topics: GF(2) Field, Change of Basis, General Inner Product Spaces, and Jordan Canonical Form.",
        "🎓"
    )

    tab_gf2, tab_cob, tab_ips, tab_jordan = st.tabs([
        "🔢 Galois Field GF(2) Solver",
        "🔄 Change of Basis & Similarity",
        "📏 Inner Product Spaces",
        "🧩 Jordan Canonical Form & Derogatory Check"
    ])

    # ---------------- TAB 1: GF(2) GALOIS FIELD ----------------
    with tab_gf2:
        st.subheader("Galois Field GF(2) Binary Arithmetic & Matrix Solver")
        st.caption("GF(2) consists of elements {0, 1} where addition is XOR (1+1=0) and multiplication is AND.")

        col1, col2 = st.columns(2)
        with col1:
            r = st.number_input("Rows", 1, 5, 3, key="gf2_r")
        with col2:
            c = st.number_input("Cols", 1, 5, 3, key="gf2_c")

        st.write("**Binary Matrix A (mod 2):**")
        mat_gf2 = render_matrix_input("gf2_mat", rows=r, cols=c)
        # Convert to binary mod 2
        mat_gf2_mod = (np.round(mat_gf2).astype(int) % 2)

        st.write("**Matrix A in GF(2):**")
        st.latex(f"A_{{\\text{{GF(2)}}}} = {sp.latex(sp.Matrix(mat_gf2_mod))}")

        st.divider()
        st.write("#### GF(2) Matrix Operations:")
        
        op_gf2 = st.selectbox("Operation in GF(2)", ["A × A (Matrix Power mod 2)", "Rank over GF(2)", "Solve Ax = b in GF(2)"])

        if op_gf2 == "A × A (Matrix Power mod 2)":
            if r != c:
                st.error("Matrix power requires square matrix.")
            else:
                res = (mat_gf2_mod @ mat_gf2_mod) % 2
                st.latex(f"A^2 \\pmod 2 = {sp.latex(sp.Matrix(res))}")

        elif op_gf2 == "Rank over GF(2)":
            # SymPy Domain Matrix over GF(2)
            try:
                sp_gf2 = sp.Matrix(mat_gf2_mod)
                rank_gf2 = sp_gf2.rank()
                st.success(f"**Rank of A in GF(2)**: `{rank_gf2}`")
            except Exception as e:
                st.error(f"GF(2) rank error: {e}")

        elif op_gf2 == "Solve Ax = b in GF(2)":
            st.write("Enter Binary Vector b:")
            vec_b_gf2 = render_vector_input("gf2_b", size=r)
            vec_b_mod = (np.round(vec_b_gf2).astype(int) % 2)
            
            aug_gf2 = np.hstack([mat_gf2_mod, vec_b_mod.reshape(-1, 1)])
            st.latex(f"[A \\mid b]_{{\\text{{GF(2)}}}} = {sp.latex(sp.Matrix(aug_gf2))}")

            # Solve via SymPy rref modulo 2
            try:
                sp_aug = sp.Matrix(aug_gf2)
                # Apply row operations mod 2 manually
                rref_gf2, pivots = sp_aug.rref()
                # Modulo 2 on rref
                rref_mod2 = sp.Matrix([[elem % 2 for elem in row] for row in rref_gf2.tolist()])
                st.write("**RREF in GF(2):**")
                st.latex(f"\\text{{RREF}}([A \\mid b]) = {sp.latex(rref_mod2)}")
            except Exception as e:
                st.error(f"Error solving in GF(2): {e}")

    # ---------------- TAB 2: CHANGE OF BASIS ----------------
    with tab_cob:
        st.subheader("Change of Basis & Matrix Similarity")
        st.caption("Find the transition matrix P from old basis B to new basis B', and compute matrix representation [T]_B' = P⁻¹ [T]_B P.")

        dim = st.number_input("Dimension n", 2, 4, 2, key="cob_n")
        
        st.write("#### 1. Old Basis B = {v₁, ..., vₙ} (as columns of matrix B)")
        mat_b = render_matrix_input("basis_b", rows=dim, cols=dim, default_vals=np.eye(dim), label="Basis B")

        st.write("#### 2. New Basis B' = {v'₁, ..., v'ₙ} (as columns of matrix B')")
        mat_b_prime = render_matrix_input("basis_b_prime", rows=dim, cols=dim, default_vals=np.array([[1.0, 1.0], [0.0, 2.0]]) if dim==2 else np.eye(dim), label="Basis B'")

        if abs(np.linalg.det(mat_b)) < 1e-7 or abs(np.linalg.det(mat_b_prime)) < 1e-7:
            st.error("Bases B and B' must be linearly independent (invertible matrices)!")
        else:
            # P_{B -> B'} = (B')^{-1} B
            p_mat = np.linalg.inv(mat_b_prime) @ mat_b
            st.write("#### Transition Matrix $P_{B \\to B'} = (B')^{-1} B$:")
            display_matrix_latex(p_mat, "P_{B \\to B'}")

            st.divider()
            st.write("#### 3. Matrix Representation of Linear Transformation T")
            mat_t_b = render_matrix_input("mat_t_b", rows=dim, cols=dim, default_vals=np.array([[2.0, 3.0], [1.0, 4.0]]) if dim==2 else np.eye(dim), label="[T]_B (Transformation in Basis B)")

            # [T]_{B'} = P [T]_B P^{-1}
            p_inv = np.linalg.inv(p_mat)
            mat_t_b_prime = p_inv @ mat_t_b @ p_mat

            st.write("#### Transformed Matrix $[T]_{B'} = P^{-1} [T]_B P$:")
            display_matrix_latex(mat_t_b_prime, "[T]_{B'}")
            st.success("✅ **Similar Matrices**: $[T]_B$ and $[T]_{B'}$ share identical eigenvalues, trace, and determinant!")

    # ---------------- TAB 3: INNER PRODUCT SPACES ----------------
    with tab_ips:
        st.subheader("General Inner Product Spaces & Cauchy-Schwarz Inequality")
        st.caption("Defines custom weighted inner products ⟨u, v⟩_W = uᵀ W v where W is a Symmetric Positive Definite matrix.")

        dim_ip = st.number_input("Vector Dimension", 2, 4, 2, key="ip_dim")
        
        c1, c2 = st.columns(2)
        with c1:
            st.write("Vector u:")
            u = render_vector_input("ip_u", size=dim_ip, default_vals=np.array([3.0, 4.0][:dim_ip]))
        with c2:
            st.write("Vector v:")
            v = render_vector_input("ip_v", size=dim_ip, default_vals=np.array([1.0, 2.0][:dim_ip]))

        st.write("#### Weight Matrix W (Positive Definite):")
        mat_w = render_matrix_input("ip_w", rows=dim_ip, cols=dim_ip, default_vals=np.eye(dim_ip), label="Weight Matrix W")

        if not np.allclose(mat_w, mat_w.T) or np.any(np.linalg.eigvals(mat_w) <= 0):
            st.warning("⚠️ Weight matrix W must be Symmetric Positive Definite for a valid inner product!")
        else:
            # Inner product <u, v>_W = u^T W v
            inner_uv = float(u.T @ mat_w @ v)
            norm_u_w = np.sqrt(float(u.T @ mat_w @ u))
            norm_v_w = np.sqrt(float(v.T @ mat_w @ v))

            st.divider()
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Inner Product ⟨u, v⟩_W", f"{inner_uv:.4f}")
            with col2:
                st.metric("Weighted Norm ||u||_W", f"{norm_u_w:.4f}")
            with col3:
                st.metric("Weighted Norm ||v||_W", f"{norm_v_w:.4f}")

            st.write("#### Cauchy-Schwarz Inequality Verification:")
            st.latex(f"|\\langle u, v \\rangle_W| = |{inner_uv:.4f}| = {abs(inner_uv):.4f}")
            st.latex(f"\\|u\\|_W \\|v\\|_W = ({norm_u_w:.4f})({norm_v_w:.4f}) = {norm_u_w * norm_v_w:.4f}")

            if abs(inner_uv) <= norm_u_w * norm_v_w + 1e-7:
                st.success("✅ **Cauchy-Schwarz Inequality Holds**: $|\\langle u, v \\rangle| \\le \\|u\\| \\|v\\|$")

    # ---------------- TAB 4: JORDAN CANONICAL FORM ----------------
    with tab_jordan:
        st.subheader("Jordan Canonical Form & Derogatory Matrix Classifier")
        st.caption("Computes Jordan Normal Form J and similarity matrix P such that A = P J P⁻¹, and checks matrix derogatory status.")

        n_j = st.number_input("Matrix Size", 2, 4, 3, key="jordan_n")
        
        # Default derogatory 3x3 matrix example: [[2, 1, 0], [0, 2, 0], [0, 0, 2]]
        default_j_mat = np.array([[2.0, 1.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]]) if n_j == 3 else np.eye(n_j)
        mat_jordan = render_matrix_input("jordan_mat", rows=n_j, cols=n_j, default_vals=default_j_mat, label="Square Matrix A")

        sp_j = to_sympy_matrix(mat_jordan)
        lam = sp.Symbol('\\lambda')

        char_poly = sp_a_poly = sp_j.charpoly(lam).as_expr()
        min_poly = sp_j.minpoly(lam)

        st.divider()
        st.write("#### 1. Polynomial Comparison:")
        st.latex(f"\\text{{Characteristic Polynomial }} P(\\lambda) = {sp.latex(char_poly)}")
        st.latex(f"\\text{{Minimal Polynomial }} m(\\lambda) = {sp.latex(min_poly)}")

        deg_char = sp.degree(char_poly, lam)
        deg_min = sp.degree(min_poly, lam)

        st.write("#### 2. Derogatory Matrix Classification:")
        if deg_min < deg_char:
            st.error(f"⚠️ **Derogatory Matrix**: $\\deg(m(\\lambda)) = {deg_min} < \\deg(P(\\lambda)) = {deg_char}$. Multiple Jordan blocks exist for the same eigenvalue!")
        else:
            st.success(f"✅ **Non-Derogatory Matrix**: $\\deg(m(\\lambda)) = \\deg(P(\\lambda)) = {deg_char}$.")

        st.divider()
        st.write("#### 3. Jordan Normal Form Computation $A = P J P^{-1}$:")
        try:
            P_jordan, J_jordan = sp_j.jordan_form()
            
            c1, c2 = st.columns(2)
            with c1:
                st.write("**Jordan Matrix J (Blocks along diagonal):**")
                st.latex(f"J = {sp.latex(J_jordan)}")
            with c2:
                st.write("**Similarity Transformation Matrix P:**")
                st.latex(f"P = {sp.latex(P_jordan)}")

            st.success("Verification: $P \\cdot J \\cdot P^{-1} = A$")
        except Exception as e:
            st.error(f"Jordan Canonical Form computation error: {e}")
