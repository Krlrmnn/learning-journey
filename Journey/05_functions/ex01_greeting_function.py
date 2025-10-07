# Show something to the user or interact without returning anything

def greet_user(name):
    print(f"Hello, {name}!")
user_name = input("Enter your name: ")
greet_user(user_name)

# Save a result for later use

def greet(name):
    return f"Hello {name}"
salute1 = greet("Jonhson")
print(salute1)