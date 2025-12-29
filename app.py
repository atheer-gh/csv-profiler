import streamlit as st
import pandas as pd
from io import StringIO
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown

st.set_page_config(page_title="CSV Profiler", layout="wide")

st.title(" CSV Profiler - Web Version")
st.write("Upload your CSV file to get a detailed profile report.")


uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    rows = df.to_dict('records')
    
    st.success("File uploaded successfully!")
    
    st.subheader("Data Preview (Top 5 rows)")
    st.dataframe(df.head())
    
    report = profile_rows(rows)
    markdown_report = render_markdown(report)
    st.markdown("---")
    st.markdown(markdown_report)
    
    st.sidebar.header("Export Options")
    
    st.sidebar.download_button(
        label="Download Report as Markdown",
        data=markdown_report,
        file_name="report.md",
        mime="text/markdown"
    )
    
    