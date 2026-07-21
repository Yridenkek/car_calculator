import streamlit as st

from modules.calculator import calculate_km


def show_km_calculator(
    car_data,
    manual_discount,
    pereliv,
    order_price,
    is_credit,
    is_tradein,
    is_loyaltradein
):

    st.markdown(
        '<div class="section-header">📊 Расчет КМ</div>',
        unsafe_allow_html=True
    )

    if car_data:

        km = calculate_km(
            car_data,
            manual_discount,
            pereliv,
            order_price,
            is_credit,
            is_tradein,
            is_loyaltradein
        )

        total_discount = km["total_discount"]
        vozm = km["vozm"]
        dopoborud = km["dopoborud"]
        insurance_value = km["insurance_value"]
        tradein_value = km["tradein_value"]
        joc = km["joc"]
        kum = km["kum"]
        iron = km["iron"]

        st.markdown(f"""
            <div class="total-margin">
                <div class="label">КУМ</div>
                <div class="value">{kum:,.0f} ₽</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(
            '<div class="divider"></div>',
            unsafe_allow_html=True
        )

        col_m1, col_m2 = st.columns(2)

        with col_m1:

            st.markdown(f"""
                <div class="accent-metric">
                    <div style="font-size:0.8rem;">Железо</div>
                    <div style="font-size:1.2rem;font-weight:600;">
                    {iron:,.0f} ₽</div>
                </div>
            """, unsafe_allow_html=True)


            st.markdown(f"""
                <div class="accent-metric">
                    <div style="font-size:0.8rem;">Сумма скидок</div>
                    <div style="font-size:1.2rem;font-weight:600;">
                    {total_discount:,.0f} ₽</div>
                </div>
            """, unsafe_allow_html=True)


            st.markdown(f"""
                <div class="accent-metric">
                    <div style="font-size:0.8rem;">ФИН</div>
                    <div style="font-size:1.2rem;font-weight:600;">
                    {insurance_value:,.0f} ₽</div>
                </div>
            """, unsafe_allow_html=True)


        with col_m2:

            st.markdown(f"""
                <div class="accent-metric">
                    <div style="font-size:0.8rem;">Доход допы</div>
                    <div style="font-size:1.2rem;font-weight:600;">
                    {dopoborud:,.0f} ₽</div>
                </div>
            """, unsafe_allow_html=True)


            st.markdown(f"""
                <div class="accent-metric">
                    <div style="font-size:0.8rem;">Возмещение</div>
                    <div style="font-size:1.2rem;font-weight:600;">
                    {vozm:,.0f} ₽</div>
                </div>
            """, unsafe_allow_html=True)


            st.markdown(f"""
                <div class="accent-metric">
                    <div style="font-size:0.8rem;">Трейд</div>
                    <div style="font-size:1.2rem;font-weight:600;">
                    {tradein_value:,.0f} ₽</div>
                </div>
            """, unsafe_allow_html=True)


        st.markdown(f"""
            <div class="info-block">
                📈 ЖОК = {joc:,.0f} ₽
            </div>
        """, unsafe_allow_html=True)


    st.markdown(
        '<div class="section-header">Данные</div>',
        unsafe_allow_html=True
    )


    vin = st.text_input("VIN", value="")
    trade_value = st.number_input(
        "Сумма трейд ин",
        min_value=0,
        step=10000
    )

    pre_order = st.number_input(
        "Предоплата",
        min_value=0,
        step=10000
    )

    qr_payment = st.number_input(
        "Оплата QR",
        min_value=0,
        step=5000
    )

    card_payment = st.number_input(
        "Оплата картой",
        min_value=0,
        step=5000
    )

    cash = st.number_input(
        "Оплата наличными",
        min_value=0,
        step=5000
    )

    client_name = st.text_input(
        "Имя клиента",
        value=""
    )


    return {
        "vin": vin,
        "trade_value": trade_value,
        "pre_order": pre_order,
        "qr_payment": qr_payment,
        "card_payment": card_payment,
        "cash": cash,
        "client_name": client_name
    }