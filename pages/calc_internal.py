import streamlit as st
import sqlite3
from pathlib import Path

st.set_page_config(page_title="Калькулятор КМ", page_icon="🔧", layout="wide")

st.markdown("""
    <style>
    /* Главный заголовок */
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Подзаголовки секций */
    .section-header {
        font-size: 1.3rem;
        font-weight: 600;
        color: #2563EB;
        border-left: 4px solid #2563EB;
        padding-left: 12px;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    
    /* Карточка с результатом */
    .result-card {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        border-radius: 12px;
        padding: 1rem;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .result-card h3 {
        margin: 0;
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    .result-card .value {
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0;
    }
    
    /* Выделение итоговой маржи */
    .total-margin {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        border-radius: 12px;
        padding: 1rem;
        color: white;
        text-align: center;
    }
    
    .total-margin .label {
        font-size: 1rem;
        margin: 0;
    }
    
    .total-margin .value {
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
    }
    
    /* Разделители */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #CBD5E1, transparent);
        margin: 1rem 0;
    }
    
    /* Акцентные метрики */
    .accent-metric {
        background: #F0F9FF;
        border-radius: 8px;
        padding: 0.5rem;
        text-align: center;
        border: 1px solid #BAE6FD;
    }
    
    /* Боковая панель */
    [data-testid="stSidebar"] {
        background: #F8FAFC;
    }
    
    /* Кнопки */
    .stButton button {
        border-radius: 8px;
        font-weight: 600;
    }
    
    /* Информационные блоки */
    .info-block {
        background: #EFF6FF;
        border-left: 4px solid #3B82F6;
        padding: 0.75rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)
# Инициализация состояния
if 'show_col2' not in st.session_state:
    st.session_state.show_col2 = True

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

if st.session_state.show_col2:
    col1, col2, col3 = st.columns([1, 1, 2])
else:
    col1, col3 = st.columns([1, 2])
    col2 = None

with col1:
    st.markdown('<div class="section-header">📋 Выбор автомобиля</div>', unsafe_allow_html=True)
    
    brands = get_brands()
    brand = st.selectbox("Марка", brands, key="brand")
    
    models = get_models(brand) if brand else []
    model = st.selectbox("Модель", models, key="model")
    
    years = get_years(brand, model) if brand and model else []
    year = st.selectbox("Год", years, key="year")
    
    trims = get_trims(brand, model, year) if brand and model and year else []
    trim = st.selectbox("Комплектация", trims, key="trim")
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">💰 Дополнительно</div>', unsafe_allow_html=True)
    
    order_price = st.number_input("Допы (заказ-наряд)", min_value=0, step=10000, value=0)
    manual_discount = st.number_input("Скидка от ДЦ", min_value=0, step=5000, value=0)
    
    st.markdown('<div class="section-header">✅ Условия покупки</div>', unsafe_allow_html=True)
    
    is_credit = st.checkbox("💳 Кредит")
    is_tradein = st.checkbox("🔄 Trade-in")
    
    is_loyaltradein = False
    if is_tradein:
        is_loyaltradein = st.checkbox("⭐ Лояльный")


if st.session_state.show_col2 and col2 is not None:
    with col2:
        st.markdown('<div class="section-header">📊 Расчет маржи</div>', unsafe_allow_html=True)
        
        if brand and model and year and trim:
            car_data = get_car_data(brand, model, year, trim)
            
            if car_data:
                markup = car_data['retailprice'] - car_data['price'] - manual_discount
                if is_loyaltradein:
                    markup -= 30000
                
                # Основной показатель - КУМ
                total_discount = car_data['pryamaya'] + manual_discount
                if is_tradein:
                    if is_loyaltradein:
                        total_discount += car_data['loyaltradein']
                    else:
                        total_discount += car_data['tradein']
                
                vozm = car_data['pryamaya'] 
                if is_tradein:
                    if is_loyaltradein:
                        vozm += car_data['loyaltradein'] - 30000
                    else:
                        vozm += car_data['tradein']
                
                dopoborud = order_price / 2
                insurance_value = 80000 if is_credit else 0
                tradein_value = 100000 if is_tradein else 0
                
                joc = dopoborud + markup + insurance_value
                kum = joc + tradein_value
                
                # Итоговая маржа - крупно
                st.markdown(f"""
                    <div class="total-margin">
                        <div class="label">КУМ</div>
                        <div class="value">{kum:,.0f} ₽</div>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
                
                # Остальные показатели в 2 колонки
                col_m1, col_m2 = st.columns(2)
                
                with col_m1:
                    st.markdown(f"""
                        <div class="accent-metric">
                            <div style="font-size:0.8rem; color:#475569;">Железо</div>
                            <div style="font-size:1.2rem; font-weight:600;">{markup:,.0f} ₽</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                        <div class="accent-metric">
                            <div style="font-size:0.8rem; color:#475569;">Сумма скидок</div>
                            <div style="font-size:1.2rem; font-weight:600;">{total_discount:,.0f} ₽</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                        <div class="accent-metric">
                            <div style="font-size:0.8rem; color:#475569;">Возмещение</div>
                            <div style="font-size:1.2rem; font-weight:600;">{vozm:,.0f} ₽</div>
                        </div>
                    """, unsafe_allow_html=True)
                
                with col_m2:
                    st.markdown(f"""
                        <div class="accent-metric">
                            <div style="font-size:0.8rem; color:#475569;">Доход допы</div>
                            <div style="font-size:1.2rem; font-weight:600;">{dopoborud:,.0f} ₽</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                        <div class="accent-metric">
                            <div style="font-size:0.8rem; color:#475569;">ФИН</div>
                            <div style="font-size:1.2rem; font-weight:600;">{insurance_value:,.0f} ₽</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                        <div class="accent-metric">
                            <div style="font-size:0.8rem; color:#475569;">Трейд</div>
                            <div style="font-size:1.2rem; font-weight:600;">{tradein_value:,.0f} ₽</div>
                        </div>
                    """, unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div class="info-block">
                        📈 ЖОК = {joc:,.0f} ₽
                    </div>
                """, unsafe_allow_html=True)
                
            else:
                st.warning("Нет данных")
        else:
            st.info("👈 Выберите автомобиль")

with col3:
    st.markdown('<div class="section-header">💳 Кредитный калькулятор</div>', unsafe_allow_html=True)
    
    # Тело кредита
    if car_data:
        discount_sum = car_data['pryamaya']
        if is_tradein:
            discount_sum += car_data['loyaltradein'] if is_loyaltradein else car_data['tradein']
        
        credit_body = max(0, car_data['retailprice'] - discount_sum + order_price + 170000)
        
        st.markdown(f"""
            <div class="info-block">
                💰 <strong>Тело кредита:</strong> {credit_body:,.0f} ₽<br>
                <span style="font-size:0.8rem;">Цена - скидки + допы + каско(170 000)</span>
            </div>
        """, unsafe_allow_html=True)
    else:
        credit_body = 0
        st.info("👈 Выберите автомобиль для расчета кредита")
    
    if credit_body > 0:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        # Ползунок
        downpayment_percent = st.slider(
            "🎯 Первоначальный взнос (%)",
            min_value=0,
            max_value=100,
            value=20,
            step=1
        )
        
        # Округление в меньшую сторону
        percent_rounded = (downpayment_percent // 10) * 10
        percent_rounded = min(percent_rounded, 80)
        
        downpayment_rub = int(credit_body * downpayment_percent / 100) if credit_body > 0 else 0
        loan_amount = max(0, credit_body - downpayment_rub)
        
        col_rub, col_loan = st.columns(2)
        with col_rub:
            st.metric("💵 Взнос в рублях", f"{downpayment_rub:,.0f} ₽")
        with col_loan:
            st.metric("🏦 Сумма кредита", f"{loan_amount:,.0f} ₽")
        
        st.caption(f"📌 Ваш взнос: {downpayment_percent}% → ставки для {percent_rounded}% (округлено в меньшую сторону)")
        
        # Сохраняем предыдущее значение процента
        if 'prev_percent' not in st.session_state:
            st.session_state.prev_percent = downpayment_percent
        
        if downpayment_percent != st.session_state.prev_percent:
            st.session_state.prev_percent = downpayment_percent
            st.session_state.show_credit = False
        
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        # ========== КНОПКА РАСЧЕТА ==========
        if st.button("📊 РАССЧИТАТЬ СТАВКИ И ПЛАТЕЖИ", type="primary", use_container_width=True):
            if loan_amount > 0:
                st.session_state.show_credit = True
                st.session_state.saved_loan_amount = loan_amount
                st.session_state.saved_percent_rounded = percent_rounded
                st.session_state.saved_brand = brand
            else:
                st.success("✅ Кредит не требуется")
        
        # ========== РЕЗУЛЬТАТЫ (ПОСЛЕ КНОПКИ) ==========
        if st.session_state.get('show_credit', False) and st.session_state.get('saved_loan_amount', 0) > 0:
            
            from database.db_manager import (
                get_credit_rate_geely, 
                get_credit_rate_haval, 
                get_credit_rate_knewstar
            )
            import pandas as pd
            
            saved_brand = st.session_state.get('saved_brand', '')
            
            if saved_brand == "Geely":
                get_credit_rate = get_credit_rate_geely
                terms = [
                    (12, "1 год"), (24, "2 года"), (36, "3 года"),
                    (48, "4 года"), (60, "5 лет"), (72, "6 лет"),
                    (84, "7 лет"), (96, "8 лет"), (108, "9 лет"), (120, "10 лет"),
                ]
            elif saved_brand == "Haval":
                get_credit_rate = get_credit_rate_haval
                terms = [
                    (12, "1 год"), (24, "2 года"), (36, "3 года"),
                    (48, "4 года"), (60, "5 лет"), (72, "6 лет"), (84, "7 лет"),
                ]
            elif saved_brand == "Knewstar":
                get_credit_rate = get_credit_rate_knewstar
                terms = [
                    (12, "1 год"), (24, "2 года"), (36, "3 года"),
                    (48, "4 года"), (60, "5 лет"), (72, "6 лет"),
                    (84, "7 лет"), (96, "8 лет"),
                ]
            else:
                get_credit_rate = None
                terms = []
            
            if get_credit_rate and terms:
                st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
                st.markdown('<div class="section-header">📊 Ставки и платежи</div>', unsafe_allow_html=True)
                
                data = []
                for months, label in terms:
                    rate = get_credit_rate(st.session_state.saved_percent_rounded, months)
                    if rate and st.session_state.saved_loan_amount > 0:
                        monthly_rate = rate / 100 / 12
                        if monthly_rate > 0:
                            payment = st.session_state.saved_loan_amount * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
                        else:
                            payment = st.session_state.saved_loan_amount / months
                        data.append({"Срок": label, "Ставка": f"{rate:.2f}%", "Платеж в месяц": f"{payment:,.0f} ₽"})
                    else:
                        data.append({"Срок": label, "Ставка": "—", "Платеж в месяц": "—"})
                
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True, hide_index=True)
        
        elif st.session_state.get('show_credit', False) and st.session_state.get('saved_loan_amount', 0) <= 0:
            st.success("✅ Кредит не требуется")
            st.session_state.show_credit = False