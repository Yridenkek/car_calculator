import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Склад автомобилей",
    layout="wide"
)

SHEET_ID = "1PiF6uLm_aqvXpYToEyfF9xqPGQ8NpQPELD0FagBn50w"
GID = "0"

url = (
    f"https://docs.google.com/spreadsheets/d/{SHEET_ID}"
    f"/export?format=csv&gid={GID}"
)

df = pd.read_csv(url)

st.title("Склад автомобилей")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)