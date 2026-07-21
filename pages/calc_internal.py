import streamlit as st
from modules.database import (get_brands, get_models, get_years, get_trims, get_car_data)
from modules.styles import load_styles
from modules.constants import get_loyal_tooltip
from modules.report import (create_report_data, generate_client_report)
from modules.credit_ui import show_credit_calculator
from modules.km_ui import show_km_calculator

st.set_page_config(page_title="Калькулятор КМ", page_icon="🔧", layout="wide")

st.markdown(
    load_styles(),
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    st.markdown('<div class="section-header">📋 Автомобиль</div>', unsafe_allow_html=True)
    
    brands = get_brands()
    brand = st.selectbox("Марка", brands, key="brand")
    
    models = get_models(brand) if brand else []
    model = st.selectbox("Модель", models, key="model")
    
    years = get_years(brand, model) if brand and model else []
    year = st.selectbox("Год", years, key="year")
    
    trims = get_trims(brand, model, year) if brand and model and year else []
    trim = st.selectbox("Комплектация", trims, key="trim")
    
    car_data = None

    if brand and model and year and trim:
        car_data = get_car_data(
            brand,
            model,
            year,
            trim
        )

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    if "order_price" not in st.session_state:
        st.session_state.order_price = 0

    order_price = st.number_input(
        "Допы (заказ-наряд)",
        min_value=0,
        step=10000,
        key="order_price"
    )    

    if "manual_discount" not in st.session_state:
        st.session_state.manual_discount = 0

    manual_discount = st.number_input(
        "Скидка от ДЦ",
        min_value=0,
        step=5000,
        key="manual_discount"
    )    

    pereliv_max = 0

    if "pereliv" not in st.session_state:
        st.session_state.pereliv = 0

    pereliv = st.number_input(
        f"Перелив в допы",
        min_value=0,
        step=10000,
        key="pereliv"
    )

    st.markdown('<div class="section-header">✅ Условия покупки</div>', unsafe_allow_html=True)
    
    is_credit = st.checkbox("💳 Кредит") 
    is_tradein = st.checkbox("🔄 Trade-in")
    
    is_loyaltradein = False
    if is_tradein:
        if car_data and car_data.get('loyaltradein', 0) > 0:
            col_chk, col_tip = st.columns([0.85, 0.15])
            with col_chk:
                is_loyaltradein = st.checkbox("Лояльный")
            with col_tip:
                tip_text = get_loyal_tooltip(model)
                st.markdown(
                    f'<span title="{tip_text}" style="cursor: help; font-size: 1.2rem;">❔</span>',
                    unsafe_allow_html=True
                )
        else:
            st.info("Лояльный трейд-ин не доступен для этого автомобиля")
    

with col2:

    km_data = show_km_calculator(
        car_data=car_data,
        manual_discount=manual_discount,
        pereliv=pereliv,
        order_price=order_price,
        is_credit=is_credit,
        is_tradein=is_tradein,
        is_loyaltradein=is_loyaltradein
    )


with col3:
    st.markdown('<div class="section-header">💳 Кредитный калькулятор</div>', unsafe_allow_html=True)
    
    show_credit_calculator(
        car_data=car_data,
        brand=brand,
        manual_discount=manual_discount,
        is_tradein=is_tradein,
        is_loyaltradein=is_loyaltradein,
        order_price=order_price,
        pereliv=pereliv
    )
    vin = km_data.get("vin", "")
    trade_value = km_data.get("trade_value", 0)
    pre_order = km_data.get("pre_order", 0)
    qr_payment = km_data.get("qr_payment", 0)
    card_payment = km_data.get("card_payment", 0)
    cash = km_data.get("cash", 0)
    client_name = km_data.get("client_name", "")

    if st.button("📄 Сформировать расчётный лист", use_container_width=True):

        if car_data is None:
            st.error(
                "Сначала выберите марку, модель, год и комплектацию"
            )

        else:

            report_dict = create_report_data(
                car_data,
                brand,
                model,
                year,
                trim,
                vin,
                is_loyaltradein,
                is_tradein,
                is_credit,
                manual_discount,
                pereliv,
                trade_value,
                pre_order,
                qr_payment,
                card_payment,
                cash,
                order_price,
                client_name
            )

            html_content = generate_client_report(
                report_dict
            )

            st.components.v1.html(
                html_content,
                height=900,
                scrolling=True
            )