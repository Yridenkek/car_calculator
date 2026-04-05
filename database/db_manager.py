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
