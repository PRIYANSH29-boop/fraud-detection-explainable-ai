"""Streamlit demo for the fraud detection model.

Planned features:
- Transaction input form
- SHAP waterfall for the prediction
- Precision/recall threshold slider (business-facing)
- Cost calculator (expected £ saved)
"""

import streamlit as st

st.set_page_config(page_title="Fraud Detector", layout="wide")
st.title("Fraud Detection Demo")
st.info("Scaffold only — model and UI not yet wired up.")
