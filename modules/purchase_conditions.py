CASH_DISCOUNT = 400_000


def apply_cash_condition(car_data, model, is_cash):
    """Return purchase data without changing cached database values."""
    if not car_data:
        return car_data
    result = dict(car_data)
    result["cash_discount"] = 0
    if is_cash and str(model).strip().casefold() == "cityray":
        result["cash_discount"] = CASH_DISCOUNT
        result["tradein"] = 0
        result["loyaltradein"] = 0
    return result
