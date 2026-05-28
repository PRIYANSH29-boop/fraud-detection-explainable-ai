# Fraud Detection System

A fraud detection portfolio project on the ULB Credit Card Fraud dataset, framed
as a real business problem (cost-aware evaluation, label auditing, fraud
archetypes, temporal drift, SHAP explainability) rather than a Kaggle exercise.

See [PROJECT_CONTEXT.md](./project_CONTEXT.md) for the full problem framing,
investigative questions, and success criteria.

> **Status:** scaffolding — not yet a working pipeline.
> **Disclaimer:** educational portfolio piece, not production-ready.

## Quickstart

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

Place the Kaggle `creditcard.csv` in `data/raw/`.

## Layout

```
data/        raw + processed datasets (gitignored)
notebooks/   01_eda → 05_evaluation
src/         reusable Python modules
app/         Streamlit demo
reports/     figures for README/LinkedIn
tests/       pytest
```

## Tasks

All entry points are invoked via `uv run <name>` from the project root, regardless
of current working directory:

| Command         | What it does                                                |
| --------------- | ----------------------------------------------------------- |
| `uv run eda`    | Launch the EDA notebook (`notebooks/01_eda.ipynb`) in Jupyter Lab |
| `uv run test`   | Run the `pytest` test suite                                 |
| `uv run lint`   | Run `ruff check` on `src` and `tests`                       |
| `uv run fmt`    | Run `ruff format` on `src` and `tests`                      |

Dev dependencies (`ruff`, `pytest`) live in the `dev` group in `pyproject.toml`
and are installed automatically by `uv run` / `uv sync`.

## Live demo

_TBD — Streamlit Community Cloud URL goes here once deployed._
