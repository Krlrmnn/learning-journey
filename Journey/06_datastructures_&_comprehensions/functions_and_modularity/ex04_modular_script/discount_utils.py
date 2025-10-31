def apply_discount(prices, discount_rate: float):
    if isinstance(prices, dict):
        return {key: round(value * (1 - discount_rate), 2) for key, value in prices.items()}
    elif isinstance(prices, list):
        return [round(value * (1 - discount_rate), 2) for value in prices]
    elif isinstance(prices, int, float):
        return round(prices * (1 - discount_rate), 2)
    else:
        raise TypeError("Invalid data type for prices")