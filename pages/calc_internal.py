import streamlit as st
import sqlite3
from pathlib import Path



st.set_page_config(page_title="Калькулятор КМ", page_icon="🔧", layout="wide")

st.title("Калькулятор КМ")

DB_PATH = Path("data/cars.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

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
    cursor.execute("SELECT DISTINCT trim FROM cars WHERE brand = ? AND model = ? AND year = ? ORDER BY trim", (brand, model, year))
    trims = [row[0] for row in cursor.fetchall()]
    conn.close()
    return trims

def get_car_data(brand, model, year, trim):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT price, retailprice, pryamaya, finance, tradein, loyaltradein 
        FROM cars 
        WHERE brand = ? AND model = ? AND year = ? AND trim = ?
    """, (brand, model, year, trim))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return {
            'price': result[0],
            'retailprice': result[1],
            'pryamaya': result[2],
            'finance': result[3],
            'tradein': result[4],
            'loyaltradein': result[5]
        }
    return None



col1, col2 = st.columns([1, 3])

with col1:

    
    
    brands = get_brands()
    brand = st.selectbox("Марка", brands, key="brand")
    
    models = get_models(brand) if brand else []
    model = st.selectbox("Модель", models, key="model")
    
    years = get_years(brand, model) if brand and model else []
    year = st.selectbox("Год", years, key="year")
    
    trims = get_trims(brand, model, year) if brand and model and year else []
    trim = st.selectbox("Комплектация", trims, key="trim")

    order_price = st.number_input("Допы", min_value=0, step=10000, value=0)

    manual_discount = st.number_input("Скидка от ДЦ", min_value=0, step=5000, value=0)

     # Галочки
    is_credit = st.checkbox("Кредит")
    is_tradein = st.checkbox("Trade-in")
            
    is_loyaltradein = False
    if is_tradein:
        is_loyaltradein = st.checkbox("Лояльный")
        


with col2:
    if brand and model and year and trim:
        
        car_data = get_car_data(brand, model, year, trim)
        
        if car_data:            
            markup = car_data['retailprice'] - car_data['price'] - manual_discount
            if is_loyaltradein:
                markup -= 30000
          
            st.metric("Железо", f"{markup:,} ₽")
            
            total_discount = car_data['pryamaya'] + manual_discount
            
            if is_tradein:
                if is_loyaltradein:
                    total_discount += car_data['loyaltradein']
                else:
                    total_discount += car_data['tradein']
            
            st.metric("Сумма скидок", f"{total_discount:,} ₽")
            
            vozm = car_data['pryamaya'] 
            if is_tradein:
                if is_loyaltradein:
                    vozm += car_data['loyaltradein']- 30000
                else:
                    vozm += car_data['tradein']
            st.metric("Возмещение", f"{vozm:,} ₽")
            dopoborud = order_price / 2
            st.metric("Доход допы", f"{dopoborud:,} ₽")
         
            insurance_value = 80000 if is_credit else 0
            st.metric("ФИН", f"{insurance_value:,} ₽")

            tradein_value = 100000 if is_tradein else 0
            st.metric("Трейд", f"{tradein_value:,} ₽")

            joc = dopoborud + markup + insurance_value
            st.metric("ЖОК", f"{joc:,}₽")
            
            kum = joc + tradein_value
            st.metric("КУМ", f"{kum:,}₽")

        else:
            st.warning("Нет данных")
    else:
        st.info("Выберите авто")