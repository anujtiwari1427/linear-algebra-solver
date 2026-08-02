# Linear Algebra Educational Suite & Production Solver 📐

A full-stack, production-quality educational web application for linear algebra powered by **Python**, **Flask**, **NumPy**, **SciPy**, **SymPy**, **Bootstrap 5**, and **MathJax**.

Designed for college presentation, academic coursework, and GitHub portfolio demonstration.

---

## 🌟 Key Features

### 🧮 1. Matrix Module
- **Matrix Addition & Subtraction**: Dimension validation, step-by-step element-wise calculation ($C_{ij} = A_{ij} \pm B_{ij}$).
- **Matrix Multiplication**: Inner dimension matching check ($\text{Cols}(A) = \text{Rows}(B)$), row $\times$ column step breakdown, `numpy.matmul()`.
- **Scalar Multiplication**: $c \cdot A$ element scaling with detailed steps.
- **Matrix Transpose**: $A^T$ transformation with index mapping.
- **Matrix Trace**: Square matrix restriction, diagonal element highlights ($a_{11} + a_{22} + \dots$).
- **Matrix Rank**: `numpy.linalg.matrix_rank()` with linear dependency/independence explanation.
- **Determinant**: Square matrix restriction, $2 \times 2, 3 \times 3$ cofactor expansion formulas, higher-order LU reduction.
- **Matrix Inverse**: Determinant check. Displays *"Matrix is singular and has no inverse."* if $\det(A) = 0$, otherwise provides $A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$.

### 🏹 2. Vector Module
- **Dot Product**: Dimension matching, scalar product $\vec{u} \cdot \vec{v} = \sum u_i v_i$.
- **Cross Product**: 3D vector restriction, determinant expansion for orthogonal vector $\vec{u} \times \vec{v}$.
- **Magnitude**: Euclidean norm $\|\vec{v}\| = \sqrt{v_1^2 + \dots + v_n^2}$.
- **Unit Vector**: Zero-vector magnitude check, normalization $\hat{v} = \frac{\vec{v}}{\|\vec{v}\|}$.
- **Vector Projection**: Shadow component formula $\text{proj}_{\vec{v}}(\vec{u}) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{v}\|^2} \vec{v}$.
- **Angle**: $\cos\theta = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$ returned in both **Degrees** and **Radians**.
- **Distance**: Euclidean distance $d(\vec{u}, \vec{v}) = \sqrt{\sum (v_i - u_i)^2}$.
- **Interactive Visualizer**: Dynamic Plotly 2D/3D vector plotter.

### ⚖️ 3. Systems of Linear Equations ($Ax = b$)
- **Gaussian Elimination**: Partial pivoting, forward elimination, back substitution.
- **Gauss-Jordan Elimination**: Direct reduction to Reduced Row Echelon Form (RREF).
- **LU Method**: $Ax = b \implies L y = P^T b, U x = y$ triangular system solves.
- **Cramer's Rule**: Determinant ratio $x_i = \frac{\det(A_i)}{\det(A)}$.
- **Consistency Analysis**: Checks Rouché–Capelli theorem ($\text{Rank}(A)$ vs $\text{Rank}([A|b])$) to identify **Unique**, **No Solution**, or **Infinitely Many Solutions**.

### ⚡ 4. Eigenvalues & Eigenvectors
- **Characteristic Polynomial**: $\det(A - \lambda I) = 0$ symbolic derivation.
- **Eigenvalues & Eigenspaces**: Real and complex roots, algebraic multiplicities, eigenspace bases.
- **Diagonalization**: Modal matrix $P$ and diagonal matrix $D$ ($A = P D P^{-1}$), matrix power $A^k = P D^k P^{-1}$.
- **Cayley-Hamilton Theorem**: Symbolic verification that $P(A) = \mathbf{0}$.

### 🧱 5. Matrix Decompositions
- **LU Factorization**: $P \cdot L \cdot U = A$ (`scipy.linalg.lu`).
- **QR Factorization**: $Q \cdot R = A$ (`numpy.linalg.qr`).
- **Singular Value Decomposition (SVD)**: $U \cdot \Sigma \cdot V^T = A$ (`numpy.linalg.svd`).
- **Cholesky Factorization**: $L \cdot L^T = A$ (`numpy.linalg.cholesky`).

### 🎓 6. Advanced Syllabus Topics
- **Galois Field GF(2)**: Binary addition (XOR) and multiplication (AND) modulo 2.
- **Change of Basis**: Transition matrix $P_{B \to B'} = (B')^{-1} B$, transformed matrix representation $[T]_{B'} = P^{-1} [T]_B P$.
- **Weighted Inner Product Spaces**: $\langle u, v \rangle_W = u^T W v$ with symmetric positive-definite weight matrix $W$.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Flask, NumPy, SciPy, SymPy
- **Frontend**: HTML5, Vanilla CSS3 (Dark Theme), JavaScript (ES6+), Bootstrap 5, MathJax 3, Plotly.js
- **Testing**: pytest
- **Production Server**: Gunicorn

---

## 🚀 Installation & Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anujtiwari1427/linear-algebra-solver.git
   cd linear-algebra-solver
   ```

2. **Create a virtual environment & install dependencies**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Flask application**:
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://127.0.0.1:5000`.

4. **Run Unit Tests**:
   ```bash
   pytest
   ```

---

## 🌐 Deployment (Vercel / Render / Railway / Heroku)

This application includes ready-to-use configuration files:
- `vercel.json` for Vercel Serverless deployment
- `render.yaml` for Render Web Service deployment
- `Procfile` for Gunicorn WSGI deployment
