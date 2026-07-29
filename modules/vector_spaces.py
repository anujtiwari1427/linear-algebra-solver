import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go
from utils.style import render_banner
from utils.helpers import render_matrix_input, to_sympy_matrix, display_matrix_latex

def render_vector_spaces_module():
    render_banner(
        "Vector Spaces & Subspaces",
        "Analyze linear independence, compute bases for fundamental matrix subspaces, and execute the Gram-Schmidt orthonormalization process with 3D step visualizer.",
        "🌌"
    )

    tab1, tab2, tab3 = st.tabs([
        "⛓️ Linear Independence & Span",
        "🏛️ Fundamental Subspaces",
        "✨ Gram-Schmidt Orthonormalization"
    ])

    # ---------------- TAB 1: LINEAR INDEPENDENCE ----------------
    with tab1:
        st.subheader("Linear Independence Test")
        col1, col2 = st.columns(2)
        with col1:
            num_vecs = st.number_input("Number of Vectors (k)", 1, 6, 3, key="li_k")
        with col2:
            dim_vecs = st.number_input("Vector Dimension (n)", 1, 6, 3, key="li_n")

        st.write("Enter vectors as columns of matrix V:")
        mat_v = render_matrix_input("li_mat", rows=dim_vecs, cols=num_vecs, label="Vectors Matrix V = [v₁ v₂ ... vₖ]")

        st.divider()
        rank_v = np.linalg.matrix_rank(mat_v)
        
        st.write(f"**Rank of V**: `{rank_v}` | **Number of Vectors k**: `{num_vecs}` | **Dimension n**: `{dim_vecs}`")

        if rank_v == num_vecs:
            st.success(f"✅ The {num_vecs} vectors are **Linearly Independent**! None can be formed as a linear combination of others.")
            if num_vecs == dim_vecs:
                st.info(f"🌟 Since k = n = {dim_vecs}, these vectors form a **Basis** for ℝ^{dim_vecs}!")
        else:
            st.warning(f"⚠️ The vectors are **Linearly Dependent**! (Rank = {rank_v} < k = {num_vecs}). Redundant vectors exist.")

        # Compute SymPy Column Basis
        sp_v = to_sympy_matrix(mat_v)
        rref_mat, pivot_indices = sp_v.rref()
        st.write("**Basis for Span(v₁, ..., vₖ):**")
        basis_vecs = [sp_v[:, idx] for idx in pivot_indices]
        for idx, b_vec in enumerate(basis_vecs):
            st.latex(f"\\vec{{b}}_{{{idx+1}}} = {sp.latex(b_vec)}")

    # ---------------- TAB 2: FUNDAMENTAL SUBSPACES ----------------
    with tab2:
        st.subheader("The Four Fundamental Subspaces of Matrix A")
        r_fs = st.number_input("Rows m", 1, 6, 3, key="fs_r")
        c_fs = st.number_input("Cols n", 1, 6, 4, key="fs_c")
        mat_fs = render_matrix_input("fs_mat", rows=r_fs, cols=c_fs, label="Matrix A (m × n)")

        sp_a = to_sympy_matrix(mat_fs)
        st.divider()

        # SymPy Subspaces
        col_space = sp_a.columnspace()
        null_space = sp_a.nullspace()
        row_space = sp_a.rowspace()
        left_null_space = sp_a.T.nullspace()

        rank_val = len(col_space)
        nullity_val = len(null_space)

        st.markdown(f"""
        <div style="background: rgba(99, 102, 241, 0.1); padding: 14px; border-radius: 10px; margin-bottom: 16px;">
            <h4>Rank-Nullity Theorem Check:</h4>
            <p style="font-size: 1.1rem;">
                <b>Rank(A)</b> [{rank_val}] + <b>Nullity(A)</b> [{nullity_val}] = <b>n (Columns)</b> [{c_fs}]
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.write(f"#### 1. Column Space C(A) ⊆ ℝ^{r_fs}")
            st.write(f"**Dimension (Rank)**: `{rank_val}`")
            for i, vec in enumerate(col_space):
                st.latex(f"c_{{{i+1}}} = {sp.latex(vec)}")

            st.write(f"#### 3. Row Space C(Aᵀ) ⊆ ℝ^{c_fs}")
            st.write(f"**Dimension (Rank)**: `{rank_val}`")
            for i, vec in enumerate(row_space):
                st.latex(f"r_{{{i+1}}} = {sp.latex(vec.T)}")

        with col2:
            st.write(f"#### 2. Null Space N(A) ⊆ ℝ^{c_fs}")
            st.write(f"**Dimension (Nullity)**: `{nullity_val}`")
            if not null_space:
                st.write("Trivial Null Space: {0}")
            else:
                for i, vec in enumerate(null_space):
                    st.latex(f"n_{{{i+1}}} = {sp.latex(vec)}")

            st.write(f"#### 4. Left Null Space N(Aᵀ) ⊆ ℝ^{r_fs}")
            st.write(f"**Dimension**: `{r_fs - rank_val}`")
            if not left_null_space:
                st.write("Trivial Left Null Space: {0}")
            else:
                for i, vec in enumerate(left_null_space):
                    st.latex(f"ln_{{{i+1}}} = {sp.latex(vec)}")

    # ---------------- TAB 3: GRAM-SCHMIDT ----------------
    with tab3:
        st.subheader("Gram-Schmidt Orthonormalization Process")
        st.caption("Transforms a linearly independent basis into an orthogonal and orthonormal basis.")

        k_gs = st.number_input("Number of Vectors (3D)", min_value=2, max_value=3, value=3, key="gs_k")
        mat_gs = render_matrix_input("gs_mat", rows=3, cols=k_gs, label="Input Vectors v₁, ..., vₖ")

        if np.linalg.matrix_rank(mat_gs) < k_gs:
            st.error("Gram-Schmidt requires linearly independent input vectors!")
        else:
            # Execute Gram-Schmidt algorithm step by step
            v_vecs = [mat_gs[:, i] for i in range(k_gs)]
            u_vecs = [] # Orthogonal
            e_vecs = [] # Orthonormal

            for i in range(k_gs):
                vi = v_vecs[i]
                ui = vi.copy()
                for j in range(i):
                    uj = u_vecs[j]
                    proj = (np.dot(vi, uj) / np.dot(uj, uj)) * uj
                    ui -= proj
                u_vecs.append(ui)
                ei = ui / np.linalg.norm(ui)
                e_vecs.append(ei)

            st.write("#### Step-by-Step Orthogonal Vectors u_i:")
            for i, ui in enumerate(u_vecs):
                st.latex(f"\\vec{{u}}_{{{i+1}}} = {sp.latex(to_sympy_matrix(ui.reshape(-1, 1)))}")

            st.write("#### Orthonormal Vectors e_i (Normalized to Unit Length):")
            for i, ei in enumerate(e_vecs):
                st.latex(f"\\vec{{e}}_{{{i+1}}} = {sp.latex(to_sympy_matrix(ei.reshape(-1, 1)))}")

            # 3D Plotly visualizer
            fig_gs = go.Figure()
            colors_orig = ['#9CA3AF', '#6B7280', '#4B5563']
            colors_ortho = ['#6366F1', '#EC4899', '#10B981']

            for i in range(k_gs):
                # Original
                fig_gs.add_trace(go.Scatter3d(x=[0, v_vecs[i][0]], y=[0, v_vecs[i][1]], z=[0, v_vecs[i][2]], mode='lines', name=f'Original v_{i+1}', line=dict(color=colors_orig[i], width=3, dash='dash')))
                # Orthonormal
                fig_gs.add_trace(go.Scatter3d(x=[0, e_vecs[i][0]], y=[0, e_vecs[i][1]], z=[0, e_vecs[i][2]], mode='lines+markers', name=f'Orthonormal e_{i+1}', line=dict(color=colors_ortho[i], width=6)))

            fig_gs.update_layout(template="plotly_dark", title="Original vs Orthonormal Basis Vectors", height=500)
            st.plotly_chart(fig_gs, use_container_width=True)
