server_status = {
    "web01": "active",
    "db01": "inactive",
    "cache01": "active",
    "worker01": "active",
    "backup01": "inactive"
}

for key, value in server_status.items():
    if value == "active":
        print(key)

active_servers = " | ".join({key: value for key, value in server_status.items() if value == "active"})
print(f"Active servers:\n{active_servers}")