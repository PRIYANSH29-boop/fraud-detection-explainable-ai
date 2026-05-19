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

## Week plan (adaptive — Mon's findings reshape the rest)
- **Mon:** Investigative EDA — find ≥2 surprising things about the data
- **Tue:** Feature engineering + label audit (Isolation Forest parallel track)
- **Wed:** Modelling — Logistic Regression baseline + XGBoost with proper imbalance handling
- **Thu:** Evaluation — PR-AUC, F1, cost-weighted metrics, threshold tuning, SHAP
- **Fri:** Streamlit app — transaction input, SHAP waterfall, threshold slider, cost calculator
- **Sat:** Deploy + README + repo polish
- **Sun:** Loom demo + LinkedIn post

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