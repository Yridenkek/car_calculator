import streamlit as st

from modules.credit_calc import (
    calculate_credit,
    get_credit_config,
    build_credit_table
)


def show_credit_calculator(
    car_data,
    brand,
    manual_discount,
    is_tradein,
    is_loyaltradein,
    order_price,
    pereliv
):

    if not car_data:
        st.info("👈 Выберите автомобиль для расчета кредита")
        return {}


    credit = calculate_credit(
        car_data,
        brand,
        manual_discount,
        is_tradein,
        is_loyaltradein,
        order_price,
        pereliv
    )


    kasko = credit["kasko"]
    carprice = credit["carprice"]
    order_price_final = credit["order_price_final"]
    pereliv_max = credit["pereliv_max"]
    credit_body = credit["credit_body"]


    st.markdown(
        f"""
        <div class="info-block">
            Железо: {carprice:,.0f} ₽<br>
            <small>Допы (с переливом)</small> {order_price_final:,.0f} ₽<br>
            <small>Перелив макс</small> {pereliv_max:,.0f} ₽<br>
            <small>КАСКО</small> {kasko:,.0f} ₽
        </div>
        """,
        unsafe_allow_html=True
    )


    if credit_body <= 0:
        st.info("Кредит не требуется")
        return credit



    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


    if (
        "last_carprice" not in st.session_state
        or st.session_state.last_carprice != carprice
    ):
        st.session_state.down_rub = int(carprice * 0.2)
        st.session_state.down_percent = 20.0
        st.session_state.last_carprice = carprice


    def sync_rub():
        st.session_state.down_percent = round(
            st.session_state.down_rub / carprice * 100,
            1
        )


    def sync_percent():
        st.session_state.down_rub = int(
            st.session_state.down_percent / 100 * carprice
        )



    col1, col2 = st.columns([1,2])


    with col1:

        st.markdown("**💵 Первоначальный взнос**")


        st.number_input(
            "Сумма ₽",
            min_value=0,
            max_value=int(carprice),
            step=1000,
            key="down_rub",
            on_change=sync_rub
        )


        st.number_input(
            "% от стоимости",
            min_value=0.0,
            max_value=100.0,
            step=0.5,
            key="down_percent",
            on_change=sync_percent
        )


    with col2:

        loan_amount = max(
            0,
            credit_body - st.session_state.down_rub
        )

        st.metric(
            "🏦 Тело кредита",
            f"{loan_amount:,.0f} ₽"
        )



    percent_rounded = (
        int(st.session_state.down_percent) // 10
    ) * 10



    if st.button(
        "📊 РАССЧИТАТЬ СТАВКИ И ПЛАТЕЖИ",
        type="primary",
        use_container_width=True
    ):

        st.session_state.credit_ready = True
        st.session_state.loan_amount = loan_amount
        st.session_state.credit_percent = percent_rounded
        st.session_state.credit_brand = brand



    if st.session_state.get("credit_ready"):

        config = get_credit_config(
            st.session_state.credit_brand
        )


        if config:

            df = build_credit_table(
                config["rate_func"],
                st.session_state.credit_percent,
                st.session_state.loan_amount,
                config["terms"]
            )


            st.markdown(
                '<div class="section-header">📊 Ставки и платежи</div>',
                unsafe_allow_html=True
            )


            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )



    return credit