import streamlit as st
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

def generate_eda_report(df):
    profile = df.profile_report(title="Pandas Profiling Report")
    st_profile_report(profile)
