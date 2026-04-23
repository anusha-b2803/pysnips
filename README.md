# PySnips

[![PyPI Version](https://img.shields.io/pypi/v/pysnips.svg)](https://pypi.org/project/pysnips/)
[![Python Version](https://img.shields.io/pypi/pyversions/pysnips.svg)](https://pypi.org/project/pysnips/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**PySnips** is a high-performance, production-quality CLI tool designed to accelerate Python development. It provides a library of **50+ expertly crafted code templates** spanning from core language syntax to advanced Machine Learning and AI Full-Stack architectures.

---

## Project Information

- **Author**: DevTools Engineer
- **GitHub**: [anusha-b2803/pysnips](https://github.com/anusha-b2803/pysnips)
- **PyPI**: [pypi.org/project/pysnips](https://pypi.org/project/pysnips/)
- **Bug Tracker**: [GitHub Issues](https://github.com/anusha-b2803/pysnips/issues)

---

## Key Features

- **50+ Specialized Templates**: Instantly generate boilerplate for Basic Python, ML, Deep Learning, and FastAPI.
- **Dynamic Injection**: Fully customizable snippets using CLI flags (e.g., `--name MyModel --lr 0.01`).
- **IDE Integration**: Install snippets natively into VS Code for "type and enter" expansion.
- **Jupyter Magic**: Type keywords in notebooks and expand them instantly with `%load_ext pysnips`.
- **Zero Dependencies**: Core CLI is built entirely on the Python Standard Library.
- **Clean Architecture**: Engineered with a modular registry system, making it easy to extend and maintain.

---

## Installation

The easiest way to install PySnips is via **pip**:

```bash
pip install pysnips
```

To enable Jupyter Notebook support:
```bash
pip install "pysnips[notebook]"
```

---

## 🚀 Usage & Integration

### 1. VS Code Integration (Native Snippets)
Install all templates into VS Code to enable "type and enter" expansion:
```bash
pysnips install --vscode
```
**Example**: In any `.py` file, type `linear-reg` and press **Enter** to expand the full template.

### 2. Jupyter & Notebook Magic
Enable auto-expansion in your Jupyter cells:
```python
%load_ext pysnips

# Type the keyword and run the cell to expand!
linear-reg
```

### 3. CLI Command Line
Explore and generate snippets directly:
```bash
pysnips list
pysnips for --item i --iterable "range(10)"
```

### 4. Python Library API
Use `pysnips` in your own scripts:
```python
import pysnips
snippet = pysnips.get("for", item="idx")
snippet.show() # Renders beautifully in Notebooks
```

---

## Category Overview

| Category | Description | Examples |
| :--- | :--- | :--- |
| **BASIC** | Core Python syntax & control flow | `for`, `tryfull`, `listcomp` |
| **MACHINE LEARNING** | Scikit-learn model boilerplates | `svm`, `random-forest`, `pca` |
| **DEEP LEARNING** | Keras/TensorFlow architectures | `cnn-image`, `lstm`, `nn-train` |
| **ML PIPELINE** | Data engineering & preprocessing | `scaler`, `train-test`, `pipeline` |
| **AI FULL-STACK** | FastAPI, DB connections & Logging | `fastapi-app`, `db-connect`, `ml-api` |

<details>
<summary><b>Click to see all 50+ templates</b></summary>

### BASIC
- `for`, `while`, `if`, `ifelse`, `elif`, `try`, `tryfull`, `func`, `rfunc`, `listcomp`, `dictcomp`, `setcomp`, `lambda`, `maincheck`, `printfmt`

### MACHINE LEARNING
- `linear-reg`, `logistic-reg`, `knn`, `svm`, `decision-tree`, `random-forest`, `naive-bayes`, `kmeans`, `pca`, `model-eval`

### DEEP LEARNING
- `nn-basic`, `nn-compile`, `nn-train`, `cnn-basic`, `cnn-image`, `rnn-basic`, `lstm`, `dropout`, `predict`, `save-load-dl`

### ML PIPELINE
- `data-load`, `data-clean`, `train-test`, `scaler`, `pipeline`

### AI FULL-STACK
- `fastapi-app`, `route-get`, `route-post`, `ml-api`, `file-upload`, `json-response`, `async-api`, `db-connect`, `save-predict`, `logger`

</details>

---

## License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

---

<p align="center">
  Built for the Python Community
</p>
