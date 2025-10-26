order = {"laptop": 1200000, "mouse": 25000, "keyboard": 70000}

def calculate_order_total(
        order: dict[str, float],
        discount_rate: float,
        currency_value: float,
        transform_value: bool = False
        ) -> dict[str, float]:
    
    if not transform_value:
        def apply_discount():
            order_discounted = {}
            for product, price in order.items():
                order_discounted[product] = round(price * (1 - discount_rate), 2)
            return order_discounted
        return apply_discount()
    
    else:
        def transform_currency():
            order_discounted = {}
            for product, price in order.items():
                order_discounted[product] = round((price * (1 - discount_rate)) / currency_value, 2)
            return order_discounted
        return transform_currency()
      
print(calculate_order_total(order, 0.1, 4000, transform_value=True))