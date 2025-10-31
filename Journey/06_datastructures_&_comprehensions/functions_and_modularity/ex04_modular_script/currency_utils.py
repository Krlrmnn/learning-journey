def transform_currency(prices, currency: float = None) -> float:
    if currency is None:
        return price
    elif isinstance(prices, dict):
        return {key: round(value / currency, 2) for key, value in prices.items()}
    elif isinstance(prices, list):
        return [round(price / currency, 2) for price in prices]
    elif isinstance(prices, int, float):
        return round(prices / currency, 2)
    else:
        raise TypeError("Invalid data type for prices")