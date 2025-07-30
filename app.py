import streamlit as st
import pandas as pd
from utils.eda import generate_eda_report
from utils.ai_summary import generate_ai_summary
from utils.trends import detect_trends
from utils.predict import run_prediction

st.set_page_config(page_title="AI Insight Dashboard", layout="wide")
st.title("📊 AI-Powered Data Analysis Dashboard")

uploaded_file = st.file_uploader("Upload your dataset (CSV only)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    with st.expander("🔍 Exploratory Data Analysis"):
        generate_eda_report(df)

    with st.expander("🤖 AI Summary Generator"):
        summary = generate_ai_summary(df)
        st.write(summary)

    with st.expander("📈 Trend Detection"):
        detect_trends(df)

    with st.expander("🔮 Predictive Analytics"):
        run_prediction(df)

else:
    st.info("Please upload a CSV file to begin analysis.")
