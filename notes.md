# Project Notes

Running log of what got done, decisions made, and open questions. Newest session at the top.

---

## Session 2 — 2026-05-19 — Data sanity check notebook

### What was done
- Implemented `src/data_loader.py:load_raw()` — resolves to `data/raw/creditcard.csv` by default, accepts a path override, raises `FileNotFoundError` with a Kaggle hint if missing.
- Populated `notebooks/00_data_sanity_check.ipynb` (file was created empty by the user). Sections:
  - Header (purpose / pass criteria / source / expected shape & fraud count)
  - Setup — adds project root to `sys.path`, imports `load_raw`, loads df, `.head()`
  - Shape & schema — prints `df.shape` and dtypes
  - Class distribution — counts and fraud %
  - Missing values & column set — total nulls + check that columns equal `Time, V1..V28, Amount, Class` in order
  - Final assertions — shape `(284807, 31)`, fraud count `492`, zero nulls, column order

### Decisions made
- **Implemented `load_raw()` directly** (boilerplate `pd.read_csv` with path resolver) rather than asking first, since it's not analytical logic — flag if you'd rather have written it yourself.
- **`sys.path` hack in the notebook** to import `src.data_loader` without installing the project. Cleaner long-term alternative: `pip install -e .` with a minimal `pyproject.toml`. Skipped for now — flag if you want it.
- **Assertions use `int(...)` casts** on pandas sums to avoid numpy scalar comparisons biting later.

### Open / TODO
- [ ] Run `00_data_sanity_check.ipynb` end-to-end and confirm all four assertions pass.
- [ ] Decide on the `pip install -e .` approach vs the `sys.path` shim for `src/` imports.

---

## Session 1 — 2026-05-19 — Project scaffolding

### What was done
- Read `project_CONTEXT.md` to understand goals, dataset, and differentiators.
- Created the full directory tree per spec:
  - `data/raw/`, `data/processed/`
  - `notebooks/`, `src/`, `app/`, `reports/figures/`, `tests/`
- Created stub files (intentionally empty bodies — to be filled in by hand):
  - `src/__init__.py`, `data_loader.py`, `features.py`, `models.py`, `utils.py`
  - `app/streamlit_app.py` (minimal Streamlit boilerplate)
  - `tests/__init__.py`
  - `reports/figures/.gitkeep`
- Created the 5 notebooks with a single markdown header cell each:
  - `01_eda.ipynb`, `02_label_audit.ipynb`, `03_feature_engineering.ipynb`, `04_modelling.ipynb`, `05_evaluation.ipynb`
- Created top-level config files:
  - `requirements.txt` — pinned versions for pandas, numpy, scikit-learn, xgboost, imbalanced-learn, matplotlib, seaborn, plotly, shap, streamlit, jupyter, ipykernel
  - `.env.example` — template with `KAGGLE_USERNAME` / `KAGGLE_KEY`
  - `LICENSE` — MIT
  - `README.md` — quickstart skeleton, points readers at `project_CONTEXT.md`
- Updated `.gitignore` — added `kaggle.json`, `.vscode/`, `.DS_Store` on top of what was already there.

### Decisions made (call out if you want any changed)
- **LICENSE = MIT.** Most common for portfolio repos. Easy to swap.
- **`requirements.txt` includes `jupyter` + `ipykernel`** even though spec didn't list them — they're needed to actually run the notebooks.
- **Notebooks intentionally blank below the title cell.** Per the "I think, you code" rule — no pre-baked analysis.
- **`src/` modules empty with one-line docstrings.** Same reason. Logic to be added by hand as each notebook produces reusable pieces.
- **`tests/__init__.py` instead of `.gitkeep`** so it's a real Python package.
- **`reports/figures/.gitkeep`** so the empty dir is tracked.

### Open / TODO
- [x] Move `data/creditcard.csv` → `data/raw/creditcard.csv`.
- [x] Delete the empty `data/project_CONTEXT.md`.
- [ ] `test_setup.py` at repo root — keep, move into `tests/`, or delete? Not clear what it does yet.
- [ ] Start the Monday EDA (target: ≥2 surprising findings).
EDA question: how many transactions share the exact same Time value? Are clustered same-second transactions correlated with fraud?