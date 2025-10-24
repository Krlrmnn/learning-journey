servers = [
    {
        "name": "web01",
        "services": {"nginx": True, "ssh": True, "db": False}
    },
    {
        "name": "app01",
        "services": {"nginx": False, "ssh": True, "redis": True}
    },
    {
        "name": "db01",
        "services": {"mysql": True, "ssh": False}
    }
]

active_services = {
    server["name"]: [
        service.upper()
        for service, status in server["services"].items()
        if status
    ]
    for server in servers
}

print(active_services)