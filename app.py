import streamlit as st
import pandas as pd
import json
from csv_profiler.profile import Profiler
from csv_profiler.render import render_markdown


st.set_page_config(page_title="CSV Profiler Tool", layout="wide")

st.title(" CSV Profiler")
st.write("Upload your CSV file to get a detailed analysis.")


uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)
    
   
    st.subheader("Data Preview")
    st.dataframe(df.head())

   
    if st.button("Run Analysis"):
        
        rows = df.to_dict(orient="records")
        
    
        profiler = Profiler(rows)
        report = profiler.get_profile()
        
        st.success("Analysis Complete!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Summary")
            st.write(f"Total Rows: {report['rows']}")
            st.markdown(render_markdown(report))
            
        with col2:
            st.subheader("Export Results")
          
            json_string = json.dumps(report, indent=4)
            st.download_button(
                label="Download JSON Report",
                data=json_string,
                file_name="report.json",
                mime="application/json"
            )
st.info("Built for AI Professionals Bootcamp - Week 1")
