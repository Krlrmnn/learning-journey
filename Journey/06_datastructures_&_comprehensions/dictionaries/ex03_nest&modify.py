servers = {
    "web01": {"status": "active", "ip": "10.0.0.1"},
    "db01": {"status": "inactive", "ip": "10.0.0.2"},
    "cache01": {"status": "active", "ip": "10.0.0.3"}
}

servers["worker01"] = {"status": "active", "ip": "10.0.0.4"}
servers["db01"]["status"] = "active"

print("Active servers:")
for name, info in servers.items():
    if info["status"] == "active":
        print(f"{name}: {info['ip']}")

del servers["cache01"]
print("\nFinal dictionary structure:", servers)