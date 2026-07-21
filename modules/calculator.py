LOYAL_DISCOUNT = 30_000
DOP_MARGIN = 0.6

INSURANCE_VALUE = 80_000
TRADEIN_VALUE = 100_000

def calculate_km(
    car_data,
    manual_discount,
    pereliv,
    order_price,
    is_credit,
    is_tradein,
    is_loyaltradein
    ):
    markup = (
        car_data['retailprice']
        - car_data['price']
        - manual_discount
        - pereliv
    )

    if is_loyaltradein:
        markup -= LOYAL_DISCOUNT

    total_discount = car_data['pryamaya'] + manual_discount

    if is_tradein:
        if is_loyaltradein:
            total_discount += car_data['loyaltradein']
        else:
            total_discount += car_data['tradein']

    vozm = car_data['pryamaya']

    if is_tradein:
        if is_loyaltradein:
            vozm += car_data['loyaltradein'] - LOYAL_DISCOUNT
        else:
            vozm += car_data['tradein']

    dopoborud = (
        order_price * DOP_MARGIN
    ) + pereliv

    insurance_value = INSURANCE_VALUE if is_credit else 0
    tradein_value = TRADEIN_VALUE if is_tradein else 0

    joc = (
        dopoborud
        + markup
        + insurance_value
    )

    kum = joc + tradein_value

    iron = markup + pereliv

    return {
        "markup": markup,
        "total_discount": total_discount,
        "vozm": vozm,
        "dopoborud": dopoborud,
        "insurance_value": insurance_value,
        "tradein_value": tradein_value,
        "joc": joc,
        "kum": kum,
        "iron": iron,
    }

def calculate_km(
    car_data,
    manual_discount,
    pereliv,
    order_price,
    is_credit,
    is_tradein,
    is_loyaltradein
):
    markup = (
        car_data["retailprice"]
        - car_data["price"]
        - manual_discount
        - pereliv
    )

    if is_loyaltradein:
        markup -= 30000


    total_discount = car_data["pryamaya"] + manual_discount


    if is_tradein:
        if is_loyaltradein:
            total_discount += car_data["loyaltradein"]
        else:
            total_discount += car_data["tradein"]


    vozm = car_data["pryamaya"]

    if is_tradein:
        if is_loyaltradein:
            vozm += car_data["loyaltradein"] - 30000
        else:
            vozm += car_data["tradein"]


    dopoborud = (
        order_price * 0.6
        + pereliv
    )


    insurance_value = 80000 if is_credit else 0

    tradein_value = 100000 if is_tradein else 0


    joc = (
        dopoborud
        + markup
        + insurance_value
    )


    kum = joc + tradein_value


    iron = markup + pereliv


    return {
        "markup": markup,
        "total_discount": total_discount,
        "vozm": vozm,
        "dopoborud": dopoborud,
        "insurance_value": insurance_value,
        "tradein_value": tradein_value,
        "joc": joc,
        "kum": kum,
        "iron": iron,
    }