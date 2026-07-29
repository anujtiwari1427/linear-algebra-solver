import streamlit as st
import numpy as np
import sympy as sp
import pandas as pd
import re
from typing import Tuple, Optional

def parse_matrix_string(text: str, rows: int, cols: int) -> Optional[np.ndarray]:
    """Parses raw text strings like [[1, 2], [3, 4]] or 1 2; 3 4 into a NumPy matrix."""
    try:
        clean_str = text.strip()
        if not clean_str:
            return None
        # Handle python/numpy bracket syntax [[1,2],[3,4]]
        if "[" in clean_str:
            clean_str = clean_str.replace("[", "").replace("]", "")
            numbers = [float(x) for x in re.split(r'[\s,;]+', clean_str) if x.strip()]
            if len(numbers) == rows * cols:
                return np.array(numbers).reshape(rows, cols)
        # Handle semicolon separated rows "1 2; 3 4"
        elif ";" in clean_str:
            row_strs = clean_str.split(";")
            parsed_rows = []
            for r_str in row_strs:
                nums = [float(x) for x in re.split(r'[\s,]+', r_str.strip()) if x.strip()]
                parsed_rows.append(nums)
            arr = np.array(parsed_rows)
            if arr.shape == (rows, cols):
                return arr
        # Handle space/comma separated numbers
        else:
            numbers = [float(x) for x in re.split(r'[\s,]+', clean_str) if x.strip()]
            if len(numbers) == rows * cols:
                return np.array(numbers).reshape(rows, cols)
    except Exception:
        return None
    return None

def render_matrix_input(
    key_prefix: str,
    rows: int = 3,
    cols: int = 3,
    default_vals: Optional[np.ndarray] = None,
    label: str = "Matrix Input"
) -> np.ndarray:
    """Renders a highly interactive spreadsheet-style matrix editor with quick presets and text paste parsing."""
    st.markdown(f"##### 🧮 {label} (`{rows} × {cols}`)")
    
    # Initialize session state for matrix data if dimension changed or not set
    state_key = f"{key_prefix}_matrix_state"
    
    if default_vals is None or default_vals.shape != (rows, cols):
        default_vals = np.eye(rows, cols) if rows == cols else np.zeros((rows, cols))
        
    if state_key not in st.session_state or st.session_state[state_key].shape != (rows, cols):
        st.session_state[state_key] = default_vals.copy()

    # Preset Action Bar (Buttons)
    btn_col1, btn_col2, btn_col3, btn_col4, btn_col5, btn_col6 = st.columns([1, 1, 1, 1, 1.5, 1.5])
    
    with btn_col1:
        if st.button("🎲 Random", key=f"{key_prefix}_btn_rand", help="Generate random integer matrix"):
            st.session_state[state_key] = np.random.randint(-5, 6, size=(rows, cols)).astype(float)
            st.rerun()

    with btn_col2:
        if st.button("🆔 Identity", key=f"{key_prefix}_btn_eye", help="Set to Identity matrix"):
            st.session_state[state_key] = np.eye(rows, cols)
            st.rerun()

    with btn_col3:
        if st.button("🔄 Symmetric", key=f"{key_prefix}_btn_sym", help="Set to Symmetric matrix"):
            rand_m = np.random.randint(-4, 5, size=(max(rows, cols), max(rows, cols))).astype(float)
            sym_m = (rand_m + rand_m.T) / 2.0
            st.session_state[state_key] = sym_m[:rows, :cols]
            st.rerun()

    with btn_col4:
        if st.button("0️⃣ Clear", key=f"{key_prefix}_btn_zero", help="Set all elements to 0"):
            st.session_state[state_key] = np.zeros((rows, cols))
            st.rerun()

    with btn_col5:
        with st.popover("📋 Paste Text"):
            pasted_text = st.text_area(
                "Paste matrix syntax e.g. [[1, 2], [3, 4]] or 1 2; 3 4",
                key=f"{key_prefix}_paste_area",
                height=100
            )
            if st.button("Apply Pasted Text", key=f"{key_prefix}_apply_paste"):
                parsed = parse_matrix_string(pasted_text, rows, cols)
                if parsed is not None:
                    st.session_state[state_key] = parsed
                    st.success("Matrix parsed successfully!")
                    st.rerun()
                else:
                    st.error(f"Could not parse text into a {rows}x{cols} matrix.")

    with btn_col6:
        with st.popover("📷 Upload Image"):
            img_file = st.file_uploader(
                "Upload matrix image/photo",
                type=["png", "jpg", "jpeg"],
                key=f"{key_prefix}_img_uploader"
            )
            if img_file is not None:
                st.image(img_file, caption="Matrix Image Preview", use_container_width=True)
                if st.button("Extract Matrix", key=f"{key_prefix}_btn_extract_img"):
                    from utils.ocr_helper import process_image_matrix_upload
                    mat_extracted, log_text = process_image_matrix_upload(img_file.getvalue(), rows, cols)
                    if mat_extracted is not None:
                        st.session_state[state_key] = mat_extracted
                        st.success("Extracted matrix from image!")
                        st.rerun()
                    else:
                        st.error(f"OCR warning: {log_text}")

    # Interactive Spreadsheet Data Editor
    df_data = pd.DataFrame(
        st.session_state[state_key],
        columns=[f"c_{j+1}" for j in range(cols)],
        index=[f"r_{i+1}" for i in range(rows)]
    )

    edited_df = st.data_editor(
        df_data,
        key=f"{key_prefix}_editor_widget",
        use_container_width=True,
        num_rows="fixed",
        column_config={
            col: st.column_config.NumberColumn(format="%.2f") for col in df_data.columns
        }
    )

    # Sync back edited array
    curr_mat = edited_df.to_numpy()
    st.session_state[state_key] = curr_mat
    return curr_mat

def render_vector_input(
    key_prefix: str,
    size: int = 3,
    default_vals: Optional[np.ndarray] = None,
    label: str = "Vector Input"
) -> np.ndarray:
    """Renders an interactive vector editor with quick presets."""
    st.markdown(f"##### 🏹 {label} (`Size {size}`)")
    
    state_key = f"{key_prefix}_vec_state"
    if default_vals is None or len(default_vals) != size:
        default_vals = np.ones(size)

    if state_key not in st.session_state or len(st.session_state[state_key]) != size:
        st.session_state[state_key] = default_vals.copy()

    # Preset buttons
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("🎲 Random", key=f"{key_prefix}_vbtn_rand"):
            st.session_state[state_key] = np.random.randint(-5, 6, size=size).astype(float)
            st.rerun()
    with c2:
        if st.button("1️⃣ Ones", key=f"{key_prefix}_vbtn_ones"):
            st.session_state[state_key] = np.ones(size)
            st.rerun()
    with c3:
        if st.button("0️⃣ Zeros", key=f"{key_prefix}_vbtn_zeros"):
            st.session_state[state_key] = np.zeros(size)
            st.rerun()
    with c4:
        if st.button("📐 Normalize", key=f"{key_prefix}_vbtn_norm"):
            norm = np.linalg.norm(st.session_state[state_key])
            if norm > 1e-7:
                st.session_state[state_key] = st.session_state[state_key] / norm
                st.rerun()

    # Vector input columns
    curr_vec = st.session_state[state_key].copy()
    cols_ui = st.columns(size)
    for i in range(size):
        with cols_ui[i]:
            val = st.number_input(
                label=f"v_{i+1}",
                value=float(curr_vec[i]),
                step=1.0,
                format="%.2f",
                key=f"{key_prefix}_vec_elem_{i}"
            )
            curr_vec[i] = val

    st.session_state[state_key] = curr_vec
    return curr_vec

def to_sympy_matrix(mat: np.ndarray, exact: bool = True) -> sp.Matrix:
    """Converts a NumPy array to a SymPy Matrix (with exact rational representations where clean)."""
    if exact:
        sympy_rows = []
        for row in mat:
            sympy_row = []
            for elem in row:
                if abs(elem - round(elem)) < 1e-7:
                    sympy_row.append(sp.Integer(int(round(elem))))
                else:
                    sympy_row.append(sp.nsimplify(elem, tolerance=1e-5, rational=True))
            sympy_rows.append(sympy_row)
        return sp.Matrix(sympy_rows)
    return sp.Matrix(mat)

def format_latex_matrix(mat: np.ndarray, name: str = "A") -> str:
    """Returns a LaTeX string representation of a matrix."""
    sp_mat = to_sympy_matrix(mat)
    latex_str = sp.latex(sp_mat)
    return f"{name} = {latex_str}"

def display_matrix_latex(mat: np.ndarray, name: str = "A"):
    """Displays matrix in LaTeX math format inside Streamlit."""
    st.latex(format_latex_matrix(mat, name))
