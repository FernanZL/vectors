# Vectors: A Modular Manim-Slides Presentation

![Manim](https://img.shields.io/badge/Manim-Community-blue?style=for-the-badge&logo=python)
![Python](https://img.shields.io/badge/Python-3.12+-yellow?style=for-the-badge&logo=python)
![uv](https://img.shields.io/badge/managed%20by-uv-purple?style=for-the-badge)

A comprehensive, "self-readable" Manim-Slides presentation covering vector theory from basics to linear independence. This project was designed to be modular, pedagological, and visually engaging.

## 🚀 Features

- **Modular Design**: Organized into four logical sections: Introduction, Equality, Algebra, and Scalar Operations.
- **Self-Readable**: Integrated theoretical text synchronized with animations, eliminating the need for external notes.
- **2D & 3D Interactive Slides**: Seamless transitions between flat 2D planes and interactive 3D spaces using `Manim-Slides`.
- **Modern Infrastructure**: Managed with `uv` for lightning-fast dependency resolution and reproducibility.

## 🎓 Curriculum Walkthrough

1.  **Introduction**: Vector definitions, geometric characteristics (direction, sense, magnitude), coordinate systems (R2 & R3), and Pythagoras-based module calculation.
2.  **Equality**: Geometric equipollence, analytic equality, and the concept of opposite vectors.
3.  **Vector Algebra**: Addition and subtraction via the polygonal and parallelogram rules, algebraic properties, and point-to-point vector calculation.
4.  **Scalar Operations**: Multiplication by a scalar (strech/compress/flip), parallelism conditions, basis vectors ($\hat{i}, \hat{j}$), linear combinations, and dependence/independence theory.

## 🛠️ Setup & Installation

This project uses **[uv](https://docs.astral.sh/uv/)** for dependency management.

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd vectors
    ```

2.  **Install dependencies**:
    ```bash
    uv sync
    ```

## 🎥 Rendering and Presenting

### 1. Render the lecture
To generate the Manim animations, run:
```bash
uv run manim -ql main.py CompleteVectorLecture
```
*Note: Use `-qh` for high quality, or `-ql` for fast low-quality testing.*

### 2. Convert to Slides
Convert the rendered animations into an interactive HTML presentation:
```bash
uv run manim-slides convert CompleteVectorLecture vectors_full_lecture.html
```

### 3. Present
Open the generated `vectors_full_lecture.html` in any browser, or use the live presenter:
```bash
uv run manim-slides present CompleteVectorLecture
```

## 📂 Project Structure

- `main.py`: The entry point that composes all sections into a single master lecture.
- `sections/`: contains modular python scripts for each lecture part.
- `shared_helpers.py`: centralized styles, color palettes, and common UI components.
- `vectors.tex` & `vectors-pdf.pdf`: Original theoretical source material.
- `vectors_full_lecture.html`: Pre-rendered version (ready to view).

## 📄 License

This project is for educational purposes. All theory content is based on the provided Vector Lecture materials.
