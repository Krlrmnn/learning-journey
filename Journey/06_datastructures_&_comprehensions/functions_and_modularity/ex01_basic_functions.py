products = {
    "laptop": 1200000,
    "mouse": 25000,
    "keyboard": 70000,
    "monitor": 300000
}

def convert_prices_to_usd(dictionary, rate):

    result = {}

    for key, value in dictionary.items():
        if value > 50000:
            result[key] = round(value / rate, 2)
    return result

converted = convert_prices_to_usd(products, 4000)
print(converted)

# ---

def convert_prices_to_usd(dictionary, rate):

    result = {key: round(value / rate, 2) for key, value in dictionary.items() if value > 50000}

    return result

converted = convert_prices_to_usd(products, 4000)
print(converted)