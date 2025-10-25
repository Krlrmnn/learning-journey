users = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 16, "active": False},
    {"name": "Charlie", "age": 30, "active": True},
    {"name": "Diana", "age": 20, "active": False}
]

def filter_active_adults(users_list):

    result = [
        f"{info['name'].upper()}: (active: True)"
        for info in users_list
        if info["age"] >= 18 and info["active"]
    ]
    return result

my_results = filter_active_adults(users)
print(my_results)