import streamlit as st
from pycaret.classification import setup, compare_models, pull

def run_prediction(df):
    target = st.selectbox("Select the target column:", df.columns)
    if target:
        try:
            s = setup(df, target=target, silent=True, html=False, session_id=123)
            best_model = compare_models()
            st.write("Best Model:")
            st.write(best_model)
            results = pull()
            st.dataframe(results)
        except Exception as e:
            st.error(f"Prediction failed: {e}")
