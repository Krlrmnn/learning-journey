dict1 = dict()
dict2 = {}
print(type(dict1))
print(type(dict2))

dict2 = {"name": "Jonh", "age": 25, "city": "New York", "language": "Python", 1: "one"}

print(dict2)
print(type(dict2))

#dict = dict("name": "Jonh", "age": 25, "city": "New York", "language": "Python", 1: "one") # This will cause an error because dict() expects an iterable of key-value pairs

dict1 = {
    "name": "Jonh",
     "age": 25,
     "city": "New York",
     "languages": {"Python", "AWS", "Azure", "Kubernetes"}, # Nested dictionary
     1: "one"
     }

print(dict1)
print(type(dict1))
print(len(dict1))
print(dict1["name"])
print(dict1["languages"])
dict1["name"] = "Jane" # Update value
print(dict1["name"])
print(dict1[1]) # Accessing value with integer key
dict1["street"] = "5th Avenue" # Adding new key-value pair
print(dict1)

dict1.__delitem__("street") # Deleting key-value pair
print(dict1)
del dict1["age"] # Another way to delete key-value pair
print("age" in dict1) # Check if key exists
print("city" in dict1) # Check if key exists
print("Jane" in dict1.values()) # Check if value exists

print(dict1.keys()) # Get all keys
print(dict1.values()) # Get all values 
print(dict1.items()) # Get all key-value pairs
print(dict1.fromkeys(["name", "age", "city"], "unknown")) # Create a new dictionary from keys with default value
print(dict1.get("name")) # Get value with key
print(dict1.get("age", "N/A")) # Get value with key, return default if key not found
print(dict1.pop("city")) # Remove key-value pair and return value
print(dict1.popitem()) # Remove and return last key-value pair
print(dict1.clear()) # Clear all key-value pairs

# dict3 = dict.fromkeys(["name", "age", "city"], "unknown") # Create a new dictionary from keys with default value
dict3 = ["name", "age", "city"]
dict4 = dict.fromkeys(dict3, "unknown") # Create a new dictionary from keys with default value
print(dict4)

print(dict2.values())
print(list(dict2.values()))
print(list(dict.fromkeys(list(dict2)).values())) # Get unique values from dictionary
dict4 = {"dict1": dict1, "dict2": dict2} # Nested dictionary