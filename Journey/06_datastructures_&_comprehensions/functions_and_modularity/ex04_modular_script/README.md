# Exercise 04 – Price Processor

This module demonstrates how to build a clean, reusable system that processes product prices by:
1. Applying discounts.
2. Optionally converting prices to another currency.

It introduces **utility modularization**, **explicit parameter validation**, and **data-type flexibility**.

---

## Overview

We split the logic into three layers:

| File | Description |
|------|--------------|
| `discount_utils.py` | Handles percentage-based discounts. |
| `currency_utils.py` | Converts prices to another currency if a rate is provided. |
| `main.py` | Coordinates the process: applies discounts, then converts currency if needed. |

---

## Core Logic

### **1. discount_utils.py**

```python
def apply_discount(price, discount_rate):
    prices_discounted = []
    for p in price:
        prices_discounted.append(round(p * (1 - discount_rate), 2))
    return prices_discounted

Applies a percentage discount to each price in the list and rounds results to 2 decimals.

### **2. currency_utils.py**

def transform_currency(price, currency=None):
    if not currency:
        return price
    elif isinstance(price, list):
        return [round(p / currency, 2) for p in price]
    elif isinstance(price, dict):
        return {k: round(v / currency, 2) for k, v in price.items()}
    elif isinstance(price, (int, float)):
        return round(price / currency, 2)
    else:
        raise TypeError("Unsupported data type for currency conversion")

- Detects if the price is a list, dict, or single value.
- Converts accordingly without breaking the structure.
- Returns the same shape of data received.

### **ex04_modular_script.py**

from currency_utils import transform_currency
from discount_utils import apply_discount

def process_prices(data, discount_rate, currency_value=None):
    discounted_data = apply_discount(data, discount_rate)
    if currency_value is not None:
        transformed_data = transform_currency(discounted_data, currency_value)
        return transformed_data
    else:
        return discounted_data

## Example Usage

from ex04_modular_script.py import process_prices

prices = [10000, 20000, 24000, 10000]
result = process_prices(prices, 0.1, 4200)
print(result)

## Output

[2.14, 4.29, 5.14, 2.14]

### **Key Concepts Learned**

- Modular design (separate utilities for cleaner logic)
- is not None for explicit condition handling
- isinstance() for flexible data operations
- Defensive programming with raise TypeError
- Reusable structure ready for scaling