 # database/db_manager.py
import sqlite3
from pathlib import Path
import streamlit as st

DB_PATH = Path("data/cars.db")

def get_connection():
    """Возвращает подключение к базе данных"""
    # Убеждаемся, что папка data существует
    DB_PATH.parent.mkdir(exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Чтобы результаты были как словари
    return conn

def init_db():
    """Создает таблицы, если их нет"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Таблица автомобилей
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
    """Возвращает список всех марок"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT brand FROM cars ORDER BY brand")
    brands = [row[0] for row in cursor.fetchall()]
    conn.close()
    return brands

def get_models(brand):
    """Возвращает модели для выбранной марки"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT model FROM cars WHERE brand = ? ORDER BY model", (brand,))
    models = [row[0] for row in cursor.fetchall()]
    conn.close()
    return models

def get_years(brand, model):
    """Возвращает доступные годы для марки и модели"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT year FROM cars WHERE brand = ? AND model = ? ORDER BY year DESC", (brand, model))
    years = [row[0] for row in cursor.fetchall()]
    conn.close()
    return years

def get_trims(brand, model, year):
    """Возвращает комплектации для выбранной марки, модели и года"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT trim FROM cars WHERE brand = ? AND model = ? AND year = ?", (brand, model, year))
    trims = [row[0] for row in cursor.fetchall()]
    conn.close()
    return trims

def get_price(brand, model, year, trim):
    """Возвращает цену для выбранной конфигурации"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM cars WHERE brand = ? AND model = ? AND year = ? AND trim = ?", (brand, model, year, trim))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0
# Кредитные ставки
def init_rates_table():
    """Создает таблицу кредитных ставок"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credit_rates (
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

def get_credit_rate(pervak, term_months):
    """
    Получает ставку по первоначальному взносу и сроку
    pervak - первоначальный взнос в процентах (0, 10, 20...)
    term_months - срок в месяцах (12, 24, 36...)
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Выбираем нужную колонку в зависимости от срока
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
        SELECT {column} FROM credit_rates 
        WHERE pervak = ?
    """, (pervak,))
    
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Дополнительные удобные функции
def get_rate12(pervak):
    return get_credit_rate(pervak, 12)

def get_rate24(pervak):
    return get_credit_rate(pervak, 24)

def get_rate36(pervak):
    return get_credit_rate(pervak, 36)

def get_rate48(pervak):
    return get_credit_rate(pervak, 48)

def get_rate60(pervak):
    return get_credit_rate(pervak, 60)

def get_rate72(pervak):
    return get_credit_rate(pervak, 72)

def get_rate84(pervak):
    return get_credit_rate(pervak, 84)

def get_rate96(pervak):
    return get_credit_rate(pervak, 96)