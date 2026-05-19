# PROJECT CONTEXT: Fraud Detection System with Investigative EDA

## Who I am
I'm a junior data scientist based in London, building a portfolio project to land an ML/AI role at a UK fintech or bank. I'm following a 10-week roadmap; this is **Project 1 of 3**. I'm not a beginner copying tutorials — I want to build something a senior reviewer respects.

## Project goal (the real one, not the tutorial one)
Build a fraud detection system that treats the problem as a **real business problem**, not a Kaggle exercise. The deliverable is a deployed app + GitHub repo + interview story strong enough to survive senior technical questioning at a London fintech.

**What makes this different from every other Kaggle fraud notebook:**
- Investigative EDA, not descriptive EDA — every chart answers a question worth asking
- Treats the dataset's flaws (PCA-anonymised features, possibly mislabelled data, 2-day window, no cost info) as **things to investigate and document**, not things to ignore
- Cost-aware evaluation (expected £ saved, not just F1)
- Unsupervised anomaly detection run in parallel to find potentially mislabelled fraud
- Cluster analysis of the fraud class itself to identify fraud archetypes
- Temporal drift analysis (Day 1 vs Day 2)
- SHAP explainability with per-prediction reasoning (EU AI Act compliance angle)
- Threshold tuning surfaced as a business tradeoff, not a model knob

## Dataset
**Credit Card Fraud Detection** (Kaggle, ULB)
- 284,807 European cardholder transactions over 2 days
- 492 fraud (0.17%) — extreme class imbalance
- 28 PCA-transformed features (V1–V28), plus `Amount` and `Time`
- `Class`: 0 = legitimate, 1 = fraud
- Known limitations to investigate: anonymised features, short time window, label provenance unclear, no transaction cost beyond Amount

## Five investigative questions driving the EDA
1. **Are the labels trustworthy?** Cross-check with Isolation Forest anomaly scores. Investigate disagreements — could "legitimate" rows actually be undetected fraud?
2. **Is there temporal drift Day 1 vs Day 2?** If yes, a naive train/test split leaks information.
3. **Are there distinct fraud archetypes?** Cluster the fraud class (KMeans on V features). Document the patterns.
4. **What's the cost distribution of fraud?** If 80% of stolen money comes from 5% of frauds, the model should prioritise high-value catches.
5. **Are V features independent within Class=1?** PCA makes them orthogonal globally — does that hold conditionally?

## Tech stack
- **Language:** Python 3.11+
- **Core libs:** pandas, numpy, scikit-learn, xgboost, imbalanced-learn
- **Viz:** matplotlib, seaborn, plotly
- **Explainability:** shap
- **App:** streamlit
- **Env:** venv (not conda), pinned versions in requirements.txt
- **Editor:** VS Code on Windows
- **Version control:** git + GitHub from Day 1
- **Deployment:** Streamlit Community Cloud

## Project structure
```
fraud-detection/
├── data/
│   ├── raw/                              # Original Kaggle CSV — never edit
│   └── processed/                        # Cleaned/engineered versions
├── notebooks/
│   ├── 01_eda.ipynb                      # Investigative EDA (5 questions)
│   ├── 02_label_audit.ipynb              # Isolation Forest vs labels
│   ├── 03_feature_engineering.ipynb      # New features, imbalance strategies
│   ├── 04_modelling.ipynb                # LR baseline + XGBoost
│   └── 05_evaluation.ipynb               # Metrics, SHAP, threshold tuning, cost analysis
├── src/
│   ├── __init__.py
│   ├── data_loader.py                    # Reusable data loading
│   ├── features.py                       # Feature engineering functions
│   ├── models.py                         # Model training/eval functions
│   └── utils.py
├── app/
│   └── streamlit_app.py                  # Deployed demo
├── reports/
│   └── figures/                          # Saved charts for README/LinkedIn
├── tests/                                # Yes, even for a portfolio project
├── .gitignore                            # Excludes data/, venv/, kaggle.json, .env
├── .env.example                          # Template for env vars
├── requirements.txt                      # Pinned versions
├── README.md                             # Full writeup with screenshots
├── PROJECT_CONTEXT.md                    # This file
└── LICENSE
```

## Two-week plan (adaptive — earlier findings reshape what comes after)

**Week 1 — Investigate the data**
- **Mon:** Project scaffolding, sanity check notebook, `load_raw()`. ✓ (done 2026-05-19)
- **Tue:** Investigative EDA Part 1 — class distribution, Amount-by-class (log scale), Time→hour transaction frequency by class. 3–4 hrs.
- **Wed:** Investigative EDA Part 2 — V-feature distributions by class, V-feature correlation heatmap, conditional independence question. 3–4 hrs.
- **Thu:** Label audit (`02_label_audit.ipynb`) — Isolation Forest unsupervised, compare anomaly scores to labels, investigate disagreements. **The differentiator — protect this day.** 4–5 hrs.
- **Fri:** Fraud archetypes + cost analysis — KMeans on 492 fraud rows (k=2..5), profile clusters, compute £-concentration (top X% of frauds = Y% of loss). 3–4 hrs.
- **Sat:** Day 1 vs Day 2 drift — split on Time<86400, compare fraud rate / Amount dist / V dists, frame as ML risk. 2–3 hrs.
- **Sun:** Catch-up + consolidate — "Key insights" section in EDA notebook, update `notes.md` with modelling implications. Buffer.

**Week 2 — Build, evaluate, ship**
- **Mon:** Feature engineering (`03_feature_engineering.ipynb`) — drop weak features (EDA-justified), engineer hour-of-day / amount bins / freq, test SMOTE vs scale_pos_weight vs undersampling, stratified split. 5 hrs.
- **Tue:** Modelling (`04_modelling.ipynb`) — LR baseline (`class_weight='balanced'`), XGBoost (`scale_pos_weight` tuned), GridSearchCV on `max_depth`/`n_estimators`/`learning_rate`, compare on PR-AUC + F1 + custom £-cost. 5–6 hrs.
- **Wed:** Evaluation (`05_evaluation.ipynb`) — PR curve, confusion matrix at 0.5, **headline chart**: precision-recall-cost vs threshold, pick a business-recommended threshold. 4 hrs.
- **Thu:** SHAP — summary plot, waterfall for 3 fraud predictions, waterfall for 1 false positive (why did it get it wrong?). 3–4 hrs.
- **Fri:** Streamlit app (`app/streamlit_app.py`) — transaction input form + sample selector, predict button → probability + decision, SHAP waterfall, threshold slider with live P/R/cost, "sample a real fraud / real legit" buttons. 6 hrs.
- **Sat:** Deploy to Streamlit Community Cloud, write README properly (problem, findings, architecture diagram, screenshots, how-to-run, known limitations), clean commits, 3-min Loom. 5 hrs.
- **Sun:** LinkedIn post (focus on findings, not features), reflection in `notes.md` for Project 2. 2 hrs.

**Total: ~60–70 hours over 14 days (~4 hrs/day avg).** Mentally budget 3 weeks if life intrudes — project quality > speed.

**Schedule risks flagged but not adopted (2026-05-19 planning convo):**
- EDA front-loaded (6 days before any model) — if Week 1 slips, Week 2 collapses.
- Sun "catch-up + consolidate" is work, not real buffer.
- Streamlit + deploy in 2 days is the standard underestimate; SHAP-in-Streamlit specifically has version-pinning fiddliness.
- 5 notebooks = hidden cleanup tax in Week 2 Sat (consider collapsing 01+02 and 04+05 if pressed for time).
- Label audit on Thu (day 4 of 7) is the strongest interview story — first thing to drop if Tue–Wed overrun. Revisit on Wed whether to defend it or pull it earlier.

Decision: keep schedule as-written, revisit risks at end of Week 1 with real data on velocity.

## How I work with AI (read this carefully)
- **I think, you code.** Don't hand me solutions before I've reasoned about the problem. Ask me what I'd try first.
- **Push back on me.** If my approach is wrong or shallow, tell me — don't just be agreeable.
- **No tutorial-speak.** Explain things like I'm a future colleague, not a student.
- **Surface tradeoffs.** Every decision has an alternative — tell me what we're NOT doing and why.
- **Be honest about limitations.** If something I'm building is generic, say so and suggest how to differentiate.

## The interview story this project needs to support
"I built a fraud detection system on an extreme-imbalance dataset (0.17% positive class). Beyond the standard pipeline, I audited the labels themselves using unsupervised anomaly detection — and found N transactions that the labels called legitimate but every signal said were fraud. I clustered the fraud class and identified three distinct archetypes, two of which the model handles well and one it struggles with — which mirrors how real fraud rings evolve. I evaluated using cost-weighted metrics in £, not just F1, because a £5 false negative and a £5,000 false negative aren't the same thing. The Streamlit app exposes the precision/recall tradeoff as a business slider, because that's a product decision, not a model decision. SHAP provides per-transaction explanations — required under the EU AI Act for automated financial decisions."

## What this project is NOT
- Not a tutorial reproduction
- Not optimising for Kaggle leaderboard scores
- Not deep learning (that's Project 2 — Stock Predictor with LSTMs)
- Not a multi-agent system (that's Project 3)
- Not production-ready (educational portfolio piece — README must say so)

## Success criteria
1. ≥2 genuinely surprising findings from EDA that aren't in any public notebook
2. Deployed live app on Streamlit Cloud with public URL
3. README that a senior DS would read and think "this person thinks like a colleague, not a student"
4. At least one finding I can defend rigorously in an interview when pushed back on
5. Repo passes `git clone → pip install → run` on a fresh machine