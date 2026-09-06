import streamlit as st
import pandas as pd
st.title("Student Scores")
df=pd.read_csv("students_scored.csv")
st.dataframe(df)
