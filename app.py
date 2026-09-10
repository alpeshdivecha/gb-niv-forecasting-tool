import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="GB NIV Forecasting Tool",
    page_icon="⚡",
    layout="wide"
)

st.title("GB Imbalance Forecasting Decision Support Tool")

st.write(
    """
    This artefact forecasts short-term GB imbalance conditions
    and provides an indicative buy/sell pressure signal.
    """
)

# Load outputs

predictions = pd.read_csv(
    "prediction_results.csv"
)

feature_importance = pd.read_csv(
    "feature_importance.csv"
)

# Latest prediction

latest = predictions.iloc[-1]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Forecast NIV",
    round(latest["predicted_niv"], 1)
)

col2.metric(
    "Direction",
    latest["direction_signal"]
)

col3.metric(
    "Confidence",
    latest["confidence"]
)

st.subheader("Actual vs Predicted NIV")

chart_df = predictions[
    ["actual_niv", "predicted_niv"]
].tail(200)

st.line_chart(chart_df)

st.subheader("Top Model Features")

st.bar_chart(
    feature_importance
    .head(10)
    .set_index("Feature")
)

st.subheader("Recent Forecasts")

st.dataframe(
    predictions.tail(20)
)