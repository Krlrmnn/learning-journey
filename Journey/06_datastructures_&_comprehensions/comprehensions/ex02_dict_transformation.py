products = {
    "laptop": 1200000,
    "mouse": 25000,
    "keyboard": 70000,
    "monitor": 300000
}

products_usd = {}

for name, price in products.items():
    if price > 100000:
        products_usd[name] = round(price / 4000, 3)
print(products_usd)

products_usd2 = {name: round(price / 4000, 3) for name, price in products.items() if price > 100000}
print(products_usd2)