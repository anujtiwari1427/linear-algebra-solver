import streamlit as st
import numpy as np
import sympy as sp
from PIL import Image
import io
from utils.style import render_banner
from utils.ocr_helper import process_image_matrix_upload, extract_text_from_image, extract_numbers_from_text
from utils.helpers import render_matrix_input, to_sympy_matrix, display_matrix_latex

def render_image_solver_module():
    render_banner(
        "Image Question Solver (OCR)",
        "Upload photos or screenshots of linear algebra problems, textbook questions, or matrix equations to extract and solve them automatically.",
        "📷"
    )

    st.write("#### 1. Upload Question Image")
    uploaded_file = st.file_uploader(
        "Choose a math question image (PNG, JPG, JPEG)",
        type=["png", "jpg", "jpeg"],
        key="image_solver_uploader"
    )

    if uploaded_file is not None:
        c1, c2 = st.columns([1, 2])
        with c1:
            st.image(uploaded_file, caption="Uploaded Question Image", use_container_width=True)
            image_bytes = uploaded_file.getvalue()

        with c2:
            st.write("#### 2. OCR Text & Parameter Extraction")
            with st.spinner("Analyzing image text & scanning for matrix parameters..."):
                pil_img = Image.open(io.BytesIO(image_bytes))
                extracted_text = extract_text_from_image(pil_img)
                extracted_numbers = extract_numbers_from_text(extracted_text)

            if extracted_text:
                st.text_area("Raw Extracted Text (OCR)", value=extracted_text, height=100)
            else:
                st.info("No raw OCR text detected automatically. You can enter/edit matrix values below.")

            st.write(f"**Extracted Numbers Found ({len(extracted_numbers)})**: `{extracted_numbers}`")

        st.divider()
        st.write("#### 3. Select Problem Type to Solve")
        
        r_img = st.number_input("Detected Matrix Rows", 1, 6, 3, key="img_r")
        c_img = st.number_input("Detected Matrix Cols", 1, 6, 3, key="img_c")

        # Auto construct matrix from numbers
        req_len = r_img * c_img
        if len(extracted_numbers) >= req_len:
            init_mat = np.array(extracted_numbers[:req_len]).reshape(r_img, c_img)
        else:
            init_mat = np.eye(r_img, c_img)

        mat_extracted = render_matrix_input("img_solver_mat", rows=r_img, cols=c_img, default_vals=init_mat, label="Extracted Matrix A")

        problem_type = st.selectbox(
            "Select Solver Task",
            [
                "Matrix Determinant & Inverse",
                "Eigenvalues & Eigenvectors",
                "Solve Ax = b System of Equations",
                "Rank, Trace & Structural Properties",
                "LU & QR Decompositions"
            ]
        )

        st.divider()
        st.write("#### 4. Step-by-Step Solution:")

        if problem_type == "Matrix Determinant & Inverse":
            if r_img != c_img:
                st.error("Determinant & Inverse require a square matrix.")
            else:
                det_val = np.linalg.det(mat_extracted)
                st.latex(f"\\det(A) = {det_val:.4f}")
                if abs(det_val) > 1e-7:
                    inv_mat = np.linalg.inv(mat_extracted)
                    st.write("**Inverse Matrix $A^{-1}$:**")
                    display_matrix_latex(inv_mat, "A^{-1}")
                else:
                    st.error(r"Matrix is Singular ($\det(A) = 0$). Inverse does not exist.")

        elif problem_type == "Eigenvalues & Eigenvectors":
            if r_img != c_img:
                st.error("Eigenvalues require a square matrix.")
            else:
                sp_a = to_sympy_matrix(mat_extracted)
                lam = sp.Symbol('\\lambda')
                char_poly = sp_a.charpoly(lam)
                st.latex(f"\\text{{Characteristic Polynomial: }} {sp.latex(char_poly.as_expr())} = 0")
                
                try:
                    eigen_info = sp_a.eigenvects()
                    for i, (val, mult, vecs) in enumerate(eigen_info):
                        st.write(f"**Eigenvalue $\\lambda_{{{i+1}}} = {sp.latex(val)}$** (Multiplicity: `{mult}`):")
                        for vec in vecs:
                            st.latex(f"\\vec{{v}} = {sp.latex(vec)}")
                except Exception as e:
                    st.error(f"Eigen calculation error: {e}")

        elif problem_type == "Solve Ax = b System of Equations":
            st.write("Enter/Verify Right-Hand Side Constants Vector b:")
            # Use last columns if available or default
            init_b = np.array(extracted_numbers[req_len:req_len+r_img]) if len(extracted_numbers) >= req_len + r_img else np.ones(r_img)
            vec_b = render_matrix_input("img_b_vec", rows=r_img, cols=1, default_vals=init_b.reshape(-1, 1), label="Vector b")
            
            aug = np.hstack([mat_extracted, vec_b])
            sp_aug = to_sympy_matrix(aug)
            rref_m, _ = sp_aug.rref()
            st.latex(f"\\text{{RREF}}([A \\mid b]) = {sp.latex(rref_m)}")

        elif problem_type == "Rank, Trace & Structural Properties":
            rank_val = np.linalg.matrix_rank(mat_extracted)
            st.info(f"**Rank of A**: `{rank_val}`")
            if r_img == c_img:
                st.info(f"**Trace of A**: `{np.trace(mat_extracted):.4f}`")

        elif problem_type == "LU & QR Decompositions":
            if r_img == c_img:
                import scipy.linalg as la
                P, L, U = la.lu(mat_extracted)
                st.write("**Lower Triangular L:**")
                display_matrix_latex(L, "L")
                st.write("**Upper Triangular U:**")
                display_matrix_latex(U, "U")
    else:
        st.info("💡 Upload a photo or screenshot of any linear algebra question above to begin OCR solution extraction.")
