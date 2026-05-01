import streamlit as st
from streamlit_gsheets import GSheetsConnection



# Вариант 1: используем secrets.toml (рекомендуется)
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()   # теперь ошибки не будет

# Вариант 2: явно передаём ссылку (если secrets.toml не создан)
# conn = st.connection("gsheets", type=GSheetsConnection)
# df = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1ABC123.../edit")

st.dataframe(df)