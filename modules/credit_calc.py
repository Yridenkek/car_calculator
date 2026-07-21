from database.db_manager import (
    get_credit_rate_geely,
    get_credit_rate_haval,
    get_credit_rate_knewstar
)


def get_credit_config(brand):
    if brand == "Geely":
        return {
            "rate_func": get_credit_rate_geely,
            "terms": [
                (12, "1 год"),
                (24, "2 года"),
                (36, "3 года"),
                (48, "4 года"),
                (60, "5 лет"),
                (72, "6 лет"),
                (84, "7 лет"),
                (96, "8 лет"),
            ]
        }

    elif brand == "Haval":
        return {
            "rate_func": get_credit_rate_haval,
            "terms": [
                (12, "1 год"),
                (24, "2 года"),
                (36, "3 года"),
                (48, "4 года"),
                (60, "5 лет"),
                (72, "6 лет"),
                (84, "7 лет"),
            ]
        }

    elif brand == "Knewstar":
        return {
            "rate_func": get_credit_rate_knewstar,
            "terms": [
                (12, "1 год"),
                (24, "2 года"),
                (36, "3 года"),
                (48, "4 года"),
                (60, "5 лет"),
                (72, "6 лет"),
                (84, "7 лет"),
                (96, "8 лет"),
            ]
        }

    return None


def calculate_payment(amount, rate, months):
    monthly_rate = rate / 100 / 12

    if monthly_rate > 0:
        return (
            amount *
            (monthly_rate * (1 + monthly_rate) ** months)
            /
            ((1 + monthly_rate) ** months - 1)
        )

    return amount / months

import pandas as pd


def build_credit_table(rate_func, percent, loan_amount, terms):
    data = []

    for months, label in terms:
        rate = rate_func(percent, months)

        if rate is not None and loan_amount > 0:
            payment = calculate_payment(
                loan_amount,
                rate,
                months
            )

            data.append({
                "Срок": label,
                "Ставка": f"{rate:.2f}%",
                "Платеж в месяц": f"{payment:,.0f} ₽"
            })

        else:
            data.append({
                "Срок": label,
                "Ставка": "—",
                "Платеж в месяц": "—"
            })

    return pd.DataFrame(data)

def calculate_credit(
    car_data,
    brand,
    manual_discount,
    is_tradein,
    is_loyaltradein,
    order_price,
    pereliv
):
    discount_sum = car_data["pryamaya"] + manual_discount

    if is_tradein:
        if is_loyaltradein:
            discount_sum += car_data["loyaltradein"]
        else:
            discount_sum += car_data["tradein"]


    kasko = 130000 if brand == "Haval" else 170000


    carprice_base = (
        car_data["retailprice"]
        - discount_sum
    )


    pereliv_max = (
        carprice_base
        - 5 * (order_price + kasko)
    ) / 6

    pereliv_max = max(0, pereliv_max)


    carprice = carprice_base - pereliv


    order_price_final = order_price + pereliv


    credit_body = max(
        0,
        carprice
        + order_price_final
        + kasko
    )


    return {
        "kasko": kasko,
        "carprice_base": carprice_base,
        "carprice": carprice,
        "order_price_final": order_price_final,
        "pereliv_max": pereliv_max,
        "credit_body": credit_body,
    }