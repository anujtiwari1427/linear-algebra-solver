# 📖 Linear Algebra Interactive Web Suite — Comprehensive Code & Working Guide

Welcome to the complete code explanation and user working guide for the **Linear Algebra Interactive Python Web Suite**. 

This application is built with **Python 3.13**, **Streamlit**, **Plotly**, **NumPy**, **SciPy**, **Pandas**, and **SymPy**. It provides an intuitive, interactive environment for calculating matrix algebra, solving linear systems, visualizing vector spaces & transformations, and exploring university-level linear algebra syllabus topics.

---

## 🗂️ Project Directory Structure

```
d:/linear-algebra-webapp/
├── app.py                         # Main Streamlit application entry point & navigation router
├── requirements.txt               # List of Python dependencies
├── explanation.md                 # Complete code explanation & working guide
├── utils/
│   ├── __init__.py                # Package marker
│   ├── style.py                   # Custom glassmorphic CSS styling & UI banners
│   ├── helpers.py                 # Interactive spreadsheet matrix/vector editors & LaTeX helpers
│   └── ocr_helper.py              # OCR text & matrix extraction from uploaded question images
└── modules/
    ├── __init__.py                # Package marker
    ├── image_solver.py            # Image question solver (OCR photo & screenshot input solver)
    ├── matrix_ops.py              # Matrix arithmetic, structural properties & decompositions (LU, QR, SVD, Cholesky)
    ├── linear_equations.py        # Ax = b solvers (Gauss-Jordan, Cramer's, Inverse) + 2D/3D intersection graphs
    ├── vectors_transformations.py # Vector arithmetic, projections, 2D/3D plotters & 2D grid transformation animator
    ├── vector_spaces.py           # Linear independence, fundamental subspaces & Gram-Schmidt orthonormalization
    ├── determinants_inverses.py   # Cofactor expansion, adjugate matrix, and 2D area / 3D volume visualizer
    ├── eigen.py                   # Characteristic polynomial, eigenvalues, diagonalization, Cayley-Hamilton & minimal poly
    └── syllabus_solvers.py        # GF(2) Galois Field, Change of Basis, Inner Product Spaces & Jordan Canonical Form
```

---

## 🚀 Working Guide: How to Launch & Use the Application

### 1. Installation & Setup
Open your terminal in the project directory and install the required dependencies:
```bash
cd d:/linear-algebra-webapp
pip install -r requirements.txt
```

### 2. Launching the App
Start the Streamlit development server:
```bash
streamlit run app.py
```
Open your web browser and navigate to:
`http://localhost:8501`

### 3. Using the Interactive Interface
* **Sidebar Navigation**: Select any of the 7 learning & solver modules from the radio menu on the left sidebar.
* **Spreadsheet Matrix Editor**: Double-click any cell in the input grid to edit numbers directly. Use `Tab`, `Enter`, or arrow keys to move between cells.
* **One-Click Presets**:
  * 🎲 **Random**: Populates matrix/vector with random values.
  * 🆔 **Identity**: Resets matrix to Identity matrix $I$.
  * 🔄 **Symmetric**: Generates a valid symmetric matrix ($A = A^T$).
  * 0️⃣ **Clear**: Sets all matrix/vector values to zero.
  * 📐 **Normalize**: Normalizes vector to unit length ($\|\vec{v}\| = 1$).
* **Text Paste Popover (📋 Paste Matrix Text)**: Click to type or paste raw text matrices in formats like `[[1, 2], [3, 4]]` or `1 2; 3 4` to instantly populate the grid.

---

## 🧩 Deep Dive Code Explanation by File

---

### 1. `app.py` — Main Application Entry & Routing
**File Link**: [`app.py`](file:///d:/linear-algebra-webapp/app.py)

#### Purpose:
Sets up the Streamlit page configuration, injects global dark glassmorphism CSS, renders the sidebar navigation menu, and routes execution to the selected module renderer function.

#### Key Functions & Flow:
* `st.set_page_config(...)`: Sets page title, browser tab icon (`📐`), wide layout mode, and expanded sidebar state.
* `apply_custom_css()`: Injects custom CSS styling defined in `utils/style.py`.
* `st.sidebar.radio(...)`: Displays module selection menu.
* **Routing Logic**:
  * `"🎓 Advanced Syllabus Solvers"` $\to$ `render_syllabus_solvers_module()`
  * `"🧮 Matrix Operations & Properties"` $\to$ `render_matrix_ops_module()`
  * `"⚖️ Systems of Linear Equations"` $\to$ `render_linear_equations_module()`
  * `"🏹 Vectors & Transformations"` $\to$ `render_vectors_transformations_module()`
  * `"🌌 Vector Spaces & Subspaces"` $\to$ `render_vector_spaces_module()`
  * `"💎 Determinants & Inverses"` $\to$ `render_determinants_inverses_module()`
  * `"⚡ Eigenvalues & Eigenvectors"` $\to$ `render_eigen_module()`

---

### 2. `utils/style.py` — CSS Theme & UI Components
**File Link**: [`utils/style.py`](file:///d:/linear-algebra-webapp/utils/style.py)

#### Purpose:
Provides custom dark glassmorphic CSS styling, styled metric badges, gradient headers, and reusable header banner components.

#### Key Functions:
* `apply_custom_css()`:
  * Injects Google Fonts (`Inter` and `Fira Code`).
  * `.glass-card`: Glassmorphism cards with `backdrop-filter: blur(12px)` and subtle borders.
  * `.gradient-text`: Linear gradient text (`#6366F1` $\to$ `#A855F7` $\to$ `#EC4899`).
  * `.module-banner`: Sleek colored banner at the top of each module.
  * `.metric-badge`: Rounded badge chips for matrix classifications (e.g., "Symmetric", "Positive Definite", "Invertible").
* `render_banner(title, description, icon)`: Renders HTML module header banner with custom icons.

---

### 3. `utils/helpers.py` — Interactive Matrix/Vector Editors & SymPy Formatters
**File Link**: [`utils/helpers.py`](file:///d:/linear-algebra-webapp/utils/helpers.py)

#### Purpose:
Implements interactive spreadsheet data editors, preset button actions, raw string matrix text parsing, SymPy exact conversion, and LaTeX formatting.

#### Key Functions:
* `parse_matrix_string(text, rows, cols)`:
  * Parses raw text strings into NumPy arrays. Handles bracket notation `[[1,2],[3,4]]`, semicolon row notation `1 2; 3 4`, or space/comma separated numbers.
* `render_matrix_input(key_prefix, rows, cols, default_vals, label)`:
  * Manages `st.session_state` matrix arrays.
  * Renders preset action buttons (`🎲 Random`, `🆔 Identity`, `🔄 Symmetric`, `0️⃣ Clear`, `📋 Paste Matrix Text`).
  * Renders `st.data_editor` interactive spreadsheet grid.
  * Returns updated $r \times c$ NumPy array.
* `render_vector_input(key_prefix, size, default_vals, label)`:
  * Interactive vector editor with preset buttons (`🎲 Random`, `1️⃣ Ones`, `0️⃣ Zeros`, `📐 Normalize`).
* `to_sympy_matrix(mat, exact=True)`:
  * Converts NumPy floats into exact SymPy rational matrices using `sp.nsimplify()` for clean mathematical output.
* `display_matrix_latex(mat, name)`:
  * Renders LaTeX matrix equation $A = \begin{pmatrix} ... \end{pmatrix}$ in Streamlit math mode.

---

### 4. `modules/matrix_ops.py` — Matrix Arithmetic, Properties & Decompositions
**File Link**: [`modules/matrix_ops.py`](file:///d:/linear-algebra-webapp/modules/matrix_ops.py)

#### Purpose:
Handles basic matrix arithmetic, matrix power, rank/trace evaluation, automatic matrix classification, and canonical decompositions.

#### Key Tabs & Code Logic:
* **Tab 1: Single Matrix Operations**:
  * Transpose $A^T$: `mat_a.T`
  * Scalar Multiplication $c \cdot A$: `c_val * mat_a`
  * Matrix Power $A^k$: `np.linalg.matrix_power(mat_a, k)`
  * Rank & Trace: `np.linalg.matrix_rank(mat_a)` & `np.trace(mat_a)`
* **Tab 2: Dual Matrix Operations**:
  * Addition $A + B$, Subtraction $A - B$, Matrix Multiplication $A \times B$ (`np.matmul`), Hadamard Element-wise Product $A \odot B$ (`mat_a * mat_b`).
* **Tab 3: Structural Properties & Classification**:
  * Validates properties and displays metric badges:
    * Square ($r = c$), Symmetric ($A = A^T$), Skew-Symmetric ($A = -A^T$).
    * Diagonal, Identity, Orthogonal ($A^T A = I$).
    * Invertible ($\det(A) \neq 0$) vs. Singular ($\det(A) = 0$).
    * Definiteness: Positive Definite ($\lambda_i > 0$) vs. Positive Semi-Definite ($\lambda_i \ge 0$).
* **Tab 4: Matrix Decompositions**:
  * **LU Decomposition** ($P L U = A$): Computed using `scipy.linalg.lu(mat_a)`.
  * **QR Decomposition** ($Q R = A$): Computed using `np.linalg.qr(mat_a)`.
  * **Singular Value Decomposition** ($U \Sigma V^T = A$): Computed via `np.linalg.svd(mat_a)` with Plotly singular values bar chart.
  * **Cholesky Decomposition** ($L L^T = A$): Computed via `np.linalg.cholesky(mat_a)` for symmetric positive definite matrices.

---

### 5. `modules/linear_equations.py` — Systems of Linear Equations ($Ax = b$)
**File Link**: [`modules/linear_equations.py`](file:///d:/linear-algebra-webapp/modules/linear_equations.py)

#### Purpose:
Solves system of linear equations $Ax = b$ using Gauss-Jordan elimination, Matrix Inverse method, Cramer's Rule, and renders 2D/3D geometric line/plane intersection graphs.

#### Key Tabs & Code Logic:
* **Augmented Matrix $[A \mid b]$**: Joined via `np.hstack([mat_a, vec_b.reshape(-1, 1)])`.
* **Tab 1: Gauss-Jordan Elimination**:
  * Computes Reduced Row Echelon Form (RREF) using SymPy `sp_aug.rref()`.
  * Compares $\text{Rank}(A)$ vs. $\text{Rank}([A \mid b])$:
    * $\text{Rank}(A) = \text{Rank}([A \mid b]) = n \implies$ **Unique Solution**.
    * $\text{Rank}(A) < \text{Rank}([A \mid b]) \implies$ **No Solution (Inconsistent System)**.
    * $\text{Rank}(A) = \text{Rank}([A \mid b]) < n \implies$ **Infinitely Many Solutions**.
* **Tab 2: Matrix Inverse Method**:
  * Calculates $x = A^{-1} b$ using `np.linalg.inv(mat_a) @ vec_b`.
* **Tab 3: Cramer's Rule**:
  * Replaces $i$-th column of $A$ with $b$ to form $A_i$, and computes $x_i = \frac{\det(A_i)}{\det(A)}$.
* **Tab 4: Geometric Visualizer**:
  * **2D Systems**: Plots line 1 ($a_{11}x + a_{12}y = b_1$) and line 2 ($a_{21}x + a_{22}y = b_2$) with intersection point.
  * **3D Systems**: Renders 3D planes $a_{i1}x_1 + a_{i2}x_2 + a_{i3}x_3 = b_i$ using Plotly `go.Surface` and plots 3D intersection point.

---

### 6. `modules/vectors_transformations.py` — Vector Algebra & 2D Grid Transformation Animator
**File Link**: [`modules/vectors_transformations.py`](file:///d:/linear-algebra-webapp/modules/vectors_transformations.py)

#### Purpose:
Calculates dot products, cross products, norms, angles, vector projections, and animates 2D plane grid transformations under a matrix $T$.

#### Key Tabs & Code Logic:
* **Tab 1: Vector Operations & Plotter**:
  * Dot Product $\vec{u} \cdot \vec{v}$: `np.dot(u, v)`.
  * Cross Product $\vec{u} \times \vec{v}$ (3D): `np.cross(u, v)`.
  * Norms: Euclidean $\|\vec{u}\|_2$, $L_1$ norm $\sum |u_i|$, $L_\infty$ norm $\max |u_i|$.
  * Angle $\theta$: $\arccos\left(\frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}\right)$.
  * Vector Projection: $\text{proj}_{\vec{v}}(\vec{u}) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{v}\|^2} \vec{v}$.
  * Renders 2D & 3D Plotly vector diagrams including head-to-tail vector addition $\vec{u} + \vec{v}$.
* **Tab 2: 2D Linear Transformations**:
  * Takes a $2 \times 2$ transformation matrix $T$.
  * Presets: Rotation, Scaling, Shear X/Y, Reflection, Projection.
  * Transforms unit circle and unit square coordinates: $\text{Shape}_{\text{trans}} = T \cdot \text{Shape}_{\text{orig}}$.
  * Displays real-time grid morphing plot and area scaling factor $\det(T)$.

---

### 7. `modules/vector_spaces.py` — Vector Spaces, Subspaces & Gram-Schmidt
**File Link**: [`modules/vector_spaces.py`](file:///d:/linear-algebra-webapp/modules/vector_spaces.py)

#### Purpose:
Tests linear independence, calculates bases for the four fundamental matrix subspaces, verifies the Rank-Nullity Theorem, and executes the Gram-Schmidt Orthonormalization process.

#### Key Tabs & Code Logic:
* **Tab 1: Linear Independence & Span**:
  * Evaluates matrix rank $r = \text{Rank}(V)$. If $r = k$ (number of vectors), vectors are linearly independent.
  * Extracts basis vectors from RREF pivot column indices.
* **Tab 2: Fundamental Subspaces (Rank-Nullity Theorem)**:
  * Computes Column Space $C(A)$, Null Space $N(A)$, Row Space $C(A^T)$, and Left Null Space $N(A^T)$ using SymPy.
  * Displays Rank-Nullity verification box: $\text{Rank}(A) + \text{Nullity}(A) = n$.
* **Tab 3: Gram-Schmidt Orthonormalization**:
  * Iteratively computes orthogonal vectors $\vec{u}_i$:
    $$\vec{u}_1 = \vec{v}_1, \quad \vec{u}_i = \vec{v}_i - \sum_{j=1}^{i-1} \frac{\vec{v}_i \cdot \vec{u}_j}{\|\vec{u}_j\|^2} \vec{u}_j$$
  * Normalizes to unit vectors $\vec{e}_i = \frac{\vec{u}_i}{\|\vec{u}_i\|}$.
  * Displays 3D Plotly vector comparison graph.

---

### 8. `modules/determinants_inverses.py` — Determinants, Adjugate Matrix & Area/Volume Plots
**File Link**: [`modules/determinants_inverses.py`](file:///d:/linear-algebra-webapp/modules/determinants_inverses.py)

#### Purpose:
Computes determinants step-by-step via cofactor expansion, evaluates cofactor and adjugate matrices, computes inverse via formula $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$, and visualizes 2D parallelogram area and 3D parallelepiped volume.

#### Key Tabs & Code Logic:
* **Tab 1: Cofactor Expansion & Formula Inverse**:
  * 2x2 formula: $ad - bc$.
  * 3x3 formula: Expansion along Row 1 with $2 \times 2$ minor determinants.
  * Computes Cofactor matrix $C$, Adjugate matrix $\text{adj}(A) = C^T$, and inverse $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$.
* **Tab 2: Geometric Area & Volume Visualizer**:
  * **2D Parallelogram Area**: Plots shaded parallelogram formed by column vectors $\vec{c}_1, \vec{c}_2$. Area equals $|\det(A)|$.
  * **3D Parallelepiped Volume**: Plots 3D parallelepiped formed by $\vec{c}_1, \vec{c}_2, \vec{c}_3$. Volume equals $|\det(A)|$.

---

### 9. `modules/eigen.py` — Eigenvalues, Diagonalization, Cayley-Hamilton & Minimal Poly
**File Link**: [`modules/eigen.py`](file:///d:/linear-algebra-webapp/modules/eigen.py)

#### Purpose:
Derives characteristic polynomials, computes exact real/complex eigenvalues & eigenspaces, checks matrix diagonalization, verifies Cayley-Hamilton theorem ($P(A) = \mathbf{0}$), computes minimal polynomials, and plots eigenvector span invariance.

#### Key Tabs & Code Logic:
* **Tab 1: Characteristic Polynomial & Eigenspaces**:
  * Computes $P(\lambda) = \det(A - \lambda I) = 0$ using SymPy `sp_a.charpoly(\lambda)`.
  * Computes symbolic eigenvalues $\lambda_i$, algebraic multiplicities, and eigenvector bases.
* **Tab 2: Matrix Diagonalization ($A = P D P^{-1}$)**:
  * Checks `sp_a.is_diagonalizable()`. If true, returns Modal Matrix $P$ and Diagonal Matrix $D$.
  * Computes matrix powers $A^k = P D^k P^{-1}$.
* **Tab 3: Cayley-Hamilton Theorem & Minimal Polynomial**:
  * Verifies Cayley-Hamilton theorem by evaluating the matrix polynomial sum $P(A) = \sum a_i A^i = \mathbf{0}$.
  * Calculates minimal polynomial $m(\lambda)$ via `sp_a.minpoly(\lambda)`.
* **Tab 4: Eigenvector Span Invariance Plot**:
  * Plots grid vectors under transformation $A \vec{v}$ for a $2 \times 2$ matrix. Demonstrates that eigenvectors $\vec{v}_1, \vec{v}_2$ remain strictly on their span lines ($A \vec{v} = \lambda \vec{v}$).

---

### 10. `modules/syllabus_solvers.py` — Advanced Syllabus Concept Solvers
**File Link**: [`modules/syllabus_solvers.py`](file:///d:/linear-algebra-webapp/modules/syllabus_solvers.py)

#### Purpose:
Provides dedicated step-by-step solvers for specialized university syllabus topics: Galois Field $\text{GF}(2)$, Change of Basis, General Inner Product Spaces, and Jordan Canonical Form.

#### Key Tabs & Code Logic:
* **Tab 1: Galois Field $\text{GF}(2)$ Binary Solver**:
  * Binary matrix arithmetic modulo 2 (`mat % 2`).
  * Matrix power over $\text{GF}(2)$, rank over $\text{GF}(2)$, and solving $A x = b \pmod 2$.
* **Tab 2: Change of Basis & Similarity**:
  * Given basis $B$ and $B'$, computes transition matrix $P_{B \to B'} = (B')^{-1} B$.
  * Computes transformed matrix $[T]_{B'} = P^{-1} [T]_B P$.
* **Tab 3: Inner Product Spaces & Cauchy-Schwarz**:
  * Evaluates weighted inner products $\langle u, v \rangle_W = u^T W v$ for Symmetric Positive Definite weight matrix $W$.
  * Computes weighted norms $\|u\|_W$ and verifies Cauchy-Schwarz inequality $|\langle u, v \rangle_W| \le \|u\|_W \|v\|_W$.
* **Tab 4: Jordan Canonical Form & Derogatory Check**:
  * Computes Jordan Normal Form $J$ and similarity matrix $P$ such that $A = P J P^{-1}$ using SymPy `sp_j.jordan_form()`.
  * Classifies matrix as **Derogatory** if degree of minimal polynomial $\text{deg}(m(\lambda)) < \text{deg}(P(\lambda))$.

---

## 📑 Syllabus Topic Mapping Reference

| Syllabus Topic | File & Function | Key Math / Algorithm |
| :--- | :--- | :--- |
| **Algebra of Matrices** | [`modules/matrix_ops.py`](file:///d:/linear-algebra-webapp/modules/matrix_ops.py) | `np.matmul`, Transpose, Trace, Hadamard |
| **Systems of Linear Equations** | [`modules/linear_equations.py`](file:///d:/linear-algebra-webapp/modules/linear_equations.py) | Gauss-Jordan RREF, `Rank(A)` vs `Rank([A|b])` |
| **Galois Field GF(2)** | [`modules/syllabus_solvers.py`](file:///d:/linear-algebra-webapp/modules/syllabus_solvers.py) | Modulo 2 arithmetic, $\text{GF}(2)$ RREF |
| **Vectors & Projections** | [`modules/vectors_transformations.py`](file:///d:/linear-algebra-webapp/modules/vectors_transformations.py) | Dot/Cross product, $L_1, L_2, L_\infty$ norms, Projection |
| **Vector Spaces & Subspaces** | [`modules/vector_spaces.py`](file:///d:/linear-algebra-webapp/modules/vector_spaces.py) | Rank, Column/Row/Null space bases |
| **Rank-Nullity Theorem** | [`modules/vector_spaces.py`](file:///d:/linear-algebra-webapp/modules/vector_spaces.py) | $\text{Rank}(A) + \text{Nullity}(A) = n$ |
| **Linear Transformations Grid** | [`modules/vectors_transformations.py`](file:///d:/linear-algebra-webapp/modules/vectors_transformations.py) | $T \cdot \text{Shape}_{\text{orig}}$, rotation, scale, shear |
| **Change of Basis & Similarity** | [`modules/syllabus_solvers.py`](file:///d:/linear-algebra-webapp/modules/syllabus_solvers.py) | $P = (B')^{-1} B$, $[T]_{B'} = P^{-1} [T]_B P$ |
| **Gram-Schmidt Process** | [`modules/vector_spaces.py`](file:///d:/linear-algebra-webapp/modules/vector_spaces.py) | Orthogonal projection subtraction, Orthonormal $\vec{e}_i$ |
| **Inner Products & Cauchy-Schwarz** | [`modules/syllabus_solvers.py`](file:///d:/linear-algebra-webapp/modules/syllabus_solvers.py) | $\langle u, v \rangle_W = u^T W v$, $|\langle u, v \rangle| \le \|u\| \|v\|$ |
| **Determinants & Applications** | [`modules/determinants_inverses.py`](file:///d:/linear-algebra-webapp/modules/determinants_inverses.py) | Cofactor expansion, Adjugate, 2D Area / 3D Volume |
| **Eigenvalues & Diagonalization** | [`modules/eigen.py`](file:///d:/linear-algebra-webapp/modules/eigen.py) | $\det(A - \lambda I) = 0$, $A = P D P^{-1}$, Matrix Power $A^k$ |
| **Cayley-Hamilton Theorem** | [`modules/eigen.py`](file:///d:/linear-algebra-webapp/modules/eigen.py) | Evaluation of $P(A) = \mathbf{0}$ |
| **Jordan Canonical Form** | [`modules/syllabus_solvers.py`](file:///d:/linear-algebra-webapp/modules/syllabus_solvers.py) | $A = P J P^{-1}$, Derogatory matrix check |

---
*Created for Linear Algebra Python Web Suite — Complete Working Guide & Explanation Document.*
