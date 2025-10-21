users = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 19, "active": False},
    {"name": "Charlie", "age": 30, "active": True},
    {"name": "Diana", "age": 17, "active": False}
]

active_users_olders_than_20 = [f"{user['name'].upper()}: {user['active']}" for user in users if user["active"] and user["age"] > 20]

print(active_users_olders_than_20)

users2 = []

for user in users:
    if user['active'] and user['age'] > 20:
        users2.append(f"{user['name'].upper()}")

print(users2)