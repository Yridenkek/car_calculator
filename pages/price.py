# pages/08_show_cars.py
import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="База автомобилей", page_icon="📋", layout="wide")

st.title("📋 База автомобилей")
st.caption("Все машины в системе")

# Путь к базе данных
DB_PATH = Path("data/cars.db")

# Подключение и загрузка данных
@st.cache_data(ttl=60)  # кэш на 60 секунд
def load_cars_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM cars ORDER BY brand, model, year", conn)
    conn.close()
    return df

df = load_cars_data()

# Показываем таблицу
st.dataframe(df, use_container_width=True)

