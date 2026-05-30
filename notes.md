# Project Notes

Running log of what got done, decisions made, and open questions. Newest session at the top.

---

## W1 Retrospective — 2026-05-30 (the 2026-05-24 checkpoint, written late)

Draft from the git timeline. The bracketed lines were the judgement calls only I could make — filled 2026-05-30, with repo facts folded in where they bore on the call.

### What the timeline actually shows
- 2026-05-19: scaffolding + sanity-check notebook + two-week plan all committed (Sessions 1–3).
- 2026-05-21: EDA findings landed (`0c9d8c1d`) — roughly on the W1-Tue/Wed slot. Good.
- 2026-05-21 → 2026-05-28: **7-day gap**, then a package refactor (`c5be0b03`, flat `src/` → installable `src/fraud/`).
- 2026-05-30 (today): mid feature-engineering, uncommitted.
- Planned W1 close was 2026-05-24. Today is 2026-05-30, so W2 is starting **~6 days behind the original 2-week plan** — but inside the 3-week budget set in Session 3. Not a crisis; a planned-for slip.

### Where the time went
- The package refactor (`c5be0b03`) and a **label-audit overrun**, plus genuine time off-project (life). Notably *not* the archetypes: `02b_fraud_archetypes.ipynb` is still a 0-byte stub — that work never started, so it can't have eaten the week. The honest read is three sinks, none of them the thing the renumbering-today makes it look like was in flight.
- The refactor **needed to happen then** — the `sys.path` shims were actively biting and going installable (`src/fraud/`) unblocked clean imports across the notebooks. It ate real time, but it wasn't avoidable yak-shaving; the cost was justified, not a detour. (Flag for W2: don't let "justified" become a habit of refactoring mid-investigation.)

### Re-evaluating the five rejected pushbacks (now with real velocity data)
1. **Cut Wed EDA to half a day.** Hold the original call — but with an asterisk. The V-feature plots *did* land (`01_eda.ipynb`, 191 KB) and they're good. But the justification for keeping Wed full was "they feed Fri's archetype work" — and archetype work (`02b`) is still an empty stub, so the plots are **sitting unused so far**. The call wasn't wrong, but the payoff is *owed*, not yet banked. Don't re-litigate; do cash it in early W2.
2. **Sun batched write-ups vs per-day.** Unrelated. The 7-day gap was the refactor + label-audit overrun + time off-project — not the batched-write-up cadence. Batching isn't implicated, so leave that call alone. (If anything, per-day write-ups wouldn't have closed a gap that was mostly off-project time.)
3. **Streamlit + streamlit-shap pinning underestimate.** STILL THE BIGGEST UNMITIGATED RISK — W2 ship phase hasn't started and this was flagged as the standard trap. Decision: **yes — prototype the SHAP-in-Streamlit piece early in W2, before the polish day**, exactly as the Session-3 plan said. Holding W2 scope (see below) means this risk stays live, so de-risking it first is the whole point of keeping the buffer. Concretely: a throwaway "does `streamlit-shap` even import + render one force plot against pinned versions" spike before any real app work.
4. **5 notebooks = cleanup tax.** Now effectively 6 (archetypes split out, renumbered 02b today). Hold the separate-notebooks call — narrative clarity over cleanup tax, same as Session 3. Caveat: the "6th" is nominal — `02b` is an empty stub, so there's no real tax there yet. Revisit folding (likely 04+05) only if the W2-Sat polish day actually overruns.
5. **Label audit is the strongest interview story.** Largely done — `02_label_audit.ipynb` has 4 executed code cells with outputs, real work on disk. It *overran* its W1-Thu slot (that's one of the three time-sinks above) — which actually **validates the original prediction**: it was the thing to defend, and defend it I did, by letting it overrun rather than dropping it. Still agree, and the evidence now backs it.

### Decision out of this retro
- **Hold W2 scope; spend the 3rd-week buffer budgeted in Session 3.** No scope cut. W2 opens ~6 days behind the original 2-week line but inside the 3-week budget — a planned-for slip, not a crisis. "Quality > speed" stands. The one hard commitment that comes out of this: **SHAP-in-Streamlit spike first** (point 3) — that's what the buffer is for; don't spend it on polish.
- **Confirmed 2026-05-30: keep all 6 differentiators, accept this runs past one week. Soft finish target ~2026-06-20** (a pacing date, not a hard deadline).
- **Build in priority order so the project is ALWAYS shippable:** model -> cost-based (£) evaluation + threshold slider -> Streamlit app FIRST; then SHAP; **fraud archetypes (`02b`) LAST.** Rationale: at every point there's a complete working app, not 6 half-built notebooks. If interrupted, a finished core beats a pile of stubs.

---

## Session 3 — 2026-05-19 — Two-week plan committed

### What was done
- Wrote out a full 2-week day-by-day plan (Week 1 = investigative EDA, Week 2 = build + ship). Now lives in `PROJECT_CONTEXT.md` under "Two-week plan" (replaces the old 1-week sketch).
- Got pushback from Claude on five points before committing.

### Pushback considered and rejected (keep visible so future-me can re-evaluate)
1. **EDA too long.** Cutting Wed (V-feature dists + correlation heatmap) to half a day was suggested as recoverable buffer. Rejected — those plots feed the fraud archetype work on Fri and the feature drops on Mon-W2.
2. **Sun is not real buffer if it has work in it.** Suggestion: move write-ups into each day, leave Sun empty. Rejected — prefer batched consolidation; will revisit if Sat overruns.
3. **Streamlit + deploy in 2 days is the standard underestimate.** Specifically: `streamlit-shap` has version-pinning headaches. Noted. Mitigation: prototype the SHAP-in-Streamlit piece on Thu (W2) while already in SHAP-land if Fri starts looking thin.
4. **5 notebooks = hidden cleanup tax on W2 Sat.** Suggestion: collapse 01+02 (EDA + label audit) and 04+05 (modelling + evaluation) into 2 notebooks. Rejected for now — separate notebooks help the narrative; revisit if Sat polish day blows up.
5. **Label audit (Thu, W1) is the strongest interview story — flip it earlier.** Suggestion: do label audit Tue, then EDA, since audit findings change what to look for. Rejected — want grounding in normal EDA first before running the unsupervised cross-check. **But: if Tue–Wed overrun, the label audit is the thing to defend, not the thing to drop.**

### Added to scope
- README will include a "what didn't work" section. UK fintech interviewers ask about failed experiments more than successful ones. Cheap if a one-line log is kept as work progresses.

### Decisions made
- **Schedule committed as-written.** Risks listed in `PROJECT_CONTEXT.md` for end-of-W1 retrospective.
- **Mentally budget 3 weeks**, not 2. Quality > speed.

### Open / TODO
- [x] End of Week 1 (2026-05-24): retrospective on velocity. Re-evaluate the five rejected pushbacks with real data. → written 2026-05-30 (top of file).
- [ ] Start keeping a one-line "what didn't work" log as W1 progresses, so the README section writes itself.

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