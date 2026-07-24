from pages.report_generator import generate_report


def create_report_data(
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
):

    mcp = car_data['retailprice']

    pryamaya = car_data['pryamaya']

    loyaltd = (
        car_data['loyaltradein']
        if is_loyaltradein
        else 0
    )

    td = (
        car_data['tradein']
        if (is_tradein and not is_loyaltradein)
        else 0
    )

    finance = (
        car_data['finance']
        if is_credit
        else 0
    )

    manual = manual_discount + pereliv

    order_price_final = order_price + pereliv

    total_discount = (
        pryamaya +
        loyaltd +
        td +
        finance +
        manual
    )

    total_price = mcp - total_discount

    total_payment = (
        trade_value +
        pre_order +
        qr_payment +
        card_payment +
        cash
    )

    credit_payment = total_price - total_payment


    return {
        "brand": brand,
        "model": model,
        "year": year,
        "trim": trim,
        "vin": vin,

        "mcp": f"{mcp:,.0f}",
        "pryamaya": f"{pryamaya:,.0f}",
        "loyaltd": f"{loyaltd:,.0f}",
        "td": f"{td:,.0f}",
        "finance": f"{finance:,.0f}",
        "manual": f"{manual:,.0f}",

        "total_discount": f"{total_discount:,.0f}",
        "total_price": f"{total_price:,.0f}",

        "trade_value": f"{trade_value:,.0f}",
        "total_payment": f"{total_payment:,.0f}",

        "qr_payment": f"{qr_payment:,.0f}",
        "card_payment": f"{card_payment:,.0f}",
        "cash": f"{cash:,.0f}",
        "pre_order": f"{pre_order:,.0f}",

        "credit_payment": f"{credit_payment:,.0f}",

        "tatal_value": "0",

        "dop_oborud": f"{order_price_final:,.0f}",

        "client_name": client_name,
    }



def generate_client_report(data):

    return generate_report(data)