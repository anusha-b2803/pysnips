# PySnips

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**PySnips** is a high-performance, production-quality CLI tool designed to accelerate Python development. It provides a library of **50+ expertly crafted code templates** spanning from core language syntax to advanced Machine Learning and AI Full-Stack architectures.

---

## Key Features

- **50+ Specialized Templates**: Instantly generate boilerplate for Basic Python, ML, Deep Learning, and FastAPI.
- **Dynamic Injection**: Fully customizable snippets using CLI flags (e.g., `--name MyModel --lr 0.01`).
- **Zero Dependencies**: Built entirely on the Python Standard Library for maximum compatibility and minimal footprint.
- **Clean Architecture**: Engineered with a modular registry system, making it easy to extend and maintain.
- **Developer First**: Outputs clean, PEP-8 compliant code directly to your terminal or into a file.

---

## Installation

The easiest way to install PySnips is via **pip**:

```bash
pip install pysnips
```

### Install from Source

For development or local modifications:

```bash
git clone https://github.com/yourusername/pysnips.git
cd py-pkg
pip install -e .
```

---

## Quick Start

### 1. Explore Available Snippets
List all 50+ available commands categorized by domain:
```bash
pysnips list
```

### 2. Generate a Python Function
```bash
pysnips func --name calculate_metrics --args "data, threshold"
```

### 3. Scaffold a FastAPI Application
Generate a complete API boilerplate and save it directly to a file:
```bash
pysnips fastapi-app --title "Predictive Analytics API" > main.py
```

### 4. Build a Machine Learning Pipeline
```bash
pysnips random-forest --n_estimators 200 > train.py
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

---

## Project Architecture

PySnips is built with scalability in mind:

- `pysnips/cli.py`: Advanced argument parsing and UI handling.
- `pysnips/registry.py`: Centralized template management system.
- `pysnips/generator.py`: Regex-powered dynamic template engine.
- `pysnips/utils/`: Enhanced console formatting and color support.

---

## Deployment

To package and distribute PySnips:

1. **Build Distribution**:
   ```bash
   python -m build
   ```
2. **Upload to PyPI**:
   ```bash
   python -m twine upload dist/*
   ```

---

## License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

---

<p align="center">
  Built for the Python Community
</p>
