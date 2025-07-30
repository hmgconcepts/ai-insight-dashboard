import streamlit as st
import matplotlib.pyplot as plt

def detect_trends(df):
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if not numeric_cols:
        st.warning("No numeric columns available for trend analysis.")
        return

    selected_col = st.selectbox("Select numeric column for trend detection:", numeric_cols)
    rolling_window = st.slider("Select rolling window size:", 2, 30, 7)
    df['rolling_avg'] = df[selected_col].rolling(window=rolling_window).mean()
    st.line_chart(df[['rolling_avg']])
