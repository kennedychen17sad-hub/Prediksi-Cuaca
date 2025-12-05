import streamlit as st
import pandas as pd

st.title("Prediksi Cuaca")
st.write("Aplikasi Streamlit untuk analisis cuaca")

df = pd.read_csv("cuaca_kemayoran_bmkg_1997_2023.csv")
st.write(df.head())
