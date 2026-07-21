import sqlite3
from pathlib import Path
import streamlit as st


DB_PATH = Path("data/cars.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


@st.cache_data(ttl=3600)
def get_brands():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT DISTINCT brand FROM cars ORDER BY brand"
    )

    result = [row[0] for row in cursor.fetchall()]
    conn.close()

    return result


@st.cache_data(ttl=3600)
def get_models(brand):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT DISTINCT model 
        FROM cars 
        WHERE brand = ?
        ORDER BY model
        """,
        (brand,)
    )

    result = [row[0] for row in cursor.fetchall()]
    conn.close()

    return result


@st.cache_data(ttl=3600)
def get_years(brand, model):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT DISTINCT year 
        FROM cars
        WHERE brand = ?
        AND model = ?
        ORDER BY year DESC
        """,
        (brand, model)
    )

    result = [row[0] for row in cursor.fetchall()]
    conn.close()

    return result


@st.cache_data(ttl=3600)
def get_trims(brand, model, year):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT DISTINCT trim
        FROM cars
        WHERE brand = ?
        AND model = ?
        AND year = ?
        ORDER BY trim
        """,
        (brand, model, year)
    )

    result = [row[0] for row in cursor.fetchall()]
    conn.close()

    return result 

@st.cache_data(ttl=3600)
def get_car_data(brand, model, year, trim):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            price,
            retailprice,
            pryamaya,
            finance,
            tradein,
            loyaltradein
        FROM cars
        WHERE brand = ?
        AND model = ?
        AND year = ?
        AND trim = ?
    """,
    (brand, model, year, trim))

    result = cursor.fetchone()
    conn.close()

    if result:
        return {
            "price": result[0],
            "retailprice": result[1],
            "pryamaya": result[2],
            "finance": result[3],
            "tradein": result[4],
            "loyaltradein": result[5],
        }

    return None