from currency_utils import transform_currency
from discount_utils import apply_discount

def process_prices(data, discount_rate, currency_value=None):
    
    discounted_data = apply_discount(data, discount_rate)

    if currency_value is not None:
        transformed_data = transform_currency(discounted_data, currency_value)
        return transformed_data
    else:
        return discounted_data