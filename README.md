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

## Live demo

_TBD — Streamlit Community Cloud URL goes here once deployed._
