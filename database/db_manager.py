# database/db_manager.py
import sqlite3
from pathlib import Path
import streamlit as st

DB_PATH = Path("data/cars.db")

def get_connection():
    """Возвращает подключение к базе данных"""
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Создает таблицы, если их нет"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            trim TEXT NOT NULL,
            retailprice INTEGER NOT NULL,
            price INTEGER NOT NULL,
            pryamaya INTEGER NOT NULL,
            finance INTEGER NOT NULL,
            tradein INTEGER NOT NULL,
            loyaltradein INTEGER NOT NULL           
        )
    """)
    conn.commit()
    conn.close()

def get_brands():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT brand FROM cars ORDER BY brand")
    brands = [row[0] for row in cursor.fetchall()]
    conn.close()
    return brands

def get_models(brand):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT model FROM cars WHERE brand = ? ORDER BY model", (brand,))
    models = [row[0] for row in cursor.fetchall()]
    conn.close()
    return models

def get_years(brand, model):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT year FROM cars WHERE brand = ? AND model = ? ORDER BY year DESC", (brand, model))
    years = [row[0] for row in cursor.fetchall()]
    conn.close()
    return years

def get_trims(brand, model, year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT trim FROM cars WHERE brand = ? AND model = ? AND year = ?", (brand, model, year))
    trims = [row[0] for row in cursor.fetchall()]
    conn.close()
    return trims

def get_price(brand, model, year, trim):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM cars WHERE brand = ? AND model = ? AND year = ? AND trim = ?", (brand, model, year, trim))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0


# ========== КРЕДИТНЫЕ СТАВКИ GEELY ==========

def init_rates_table_geely():
    """Создает таблицу кредитных ставок Geely"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credit_rates_geely (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pervak INTEGER NOT NULL,
            rate12 REAL NOT NULL,
            rate24 REAL NOT NULL,
            rate36 REAL NOT NULL,
            rate48 REAL NOT NULL,
            rate60 REAL NOT NULL,
            rate72 REAL NOT NULL,
            rate84 REAL NOT NULL,
            rate96 REAL NOT NULL,
            rate108 REAL NOT NULL,
            rate120 REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_credit_rate_geely(pervak, term_months):
    conn = get_connection()
    cursor = conn.cursor()
    
    if term_months == 12:
        column = "rate12"
    elif term_months == 24:
        column = "rate24"
    elif term_months == 36:
        column = "rate36"
    elif term_months == 48:
        column = "rate48"
    elif term_months == 60:
        column = "rate60"
    elif term_months == 72:
        column = "rate72"
    elif term_months == 84:
        column = "rate84"
    elif term_months == 96:
        column = "rate96"
    elif term_months == 108:
        column = "rate108"
    elif term_months == 120:
        column = "rate120"
    else:
        conn.close()
        return None
    
    cursor.execute(f"""
        SELECT {column} FROM credit_rates_geely
        WHERE pervak = ?
    """, (pervak,))
    
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


# ========== КРЕДИТНЫЕ СТАВКИ HAVAL ==========

def init_rates_table_haval():
    """Создает таблицу кредитных ставок Haval"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credit_rates_haval (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pervak INTEGER NOT NULL,
            rate12 REAL NOT NULL,
            rate24 REAL NOT NULL,
            rate36 REAL NOT NULL,
            rate48 REAL NOT NULL,
            rate60 REAL NOT NULL,
            rate72 REAL NOT NULL,
            rate84 REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_credit_rate_haval(pervak, term_months):
    conn = get_connection()
    cursor = conn.cursor()
    
    if term_months == 12:
        column = "rate12"
    elif term_months == 24:
        column = "rate24"
    elif term_months == 36:
        column = "rate36"
    elif term_months == 48:
        column = "rate48"
    elif term_months == 60:
        column = "rate60"
    elif term_months == 72:
        column = "rate72"
    elif term_months == 84:
        column = "rate84"
    else:
        conn.close()
        return None
    
    cursor.execute(f"""
        SELECT {column} FROM credit_rates_haval
        WHERE pervak = ?
    """, (pervak,))
    
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


# ========== КРЕДИТНЫЕ СТАВКИ KNEWSTAR ==========

def init_rates_table_knewstar():
    """Создает таблицу кредитных ставок Knewstar"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credit_rates_knewstar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pervak INTEGER NOT NULL,
            rate12 REAL NOT NULL,
            rate24 REAL NOT NULL,
            rate36 REAL NOT NULL,
            rate48 REAL NOT NULL,
            rate60 REAL NOT NULL,
            rate72 REAL NOT NULL,
            rate84 REAL NOT NULL,
            rate96 REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_credit_rate_knewstar(pervak, term_months):
    conn = get_connection()
    cursor = conn.cursor()
    
    if term_months == 12:
        column = "rate12"
    elif term_months == 24:
        column = "rate24"
    elif term_months == 36:
        column = "rate36"
    elif term_months == 48:
        column = "rate48"
    elif term_months == 60:
        column = "rate60"
    elif term_months == 72:
        column = "rate72"
    elif term_months == 84:
        column = "rate84"
    elif term_months == 96:
        column = "rate96"        
    else:
        conn.close()
        return None
    
    cursor.execute(f"""
        SELECT {column} FROM credit_rates_knewstar
        WHERE pervak = ?
    """, (pervak,))
    
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None