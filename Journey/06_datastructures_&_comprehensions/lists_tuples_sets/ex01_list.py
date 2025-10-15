fav_tools = ["Python", "Docker", "Git", "Linux", "AWS"]
fav_tools.append("Kubernetes")
fav_tools.append("Terraform")
fav_tools.insert(2, "Grafana")

# Remove exact value

fav_tools.remove("Git")

# Uses index for remove

del fav_tools[0] 
fav_tools.pop(2)

# Sort from A to Z

fav_tools.sort()
sorted_tools = sorted(fav_tools)


print(fav_tools)