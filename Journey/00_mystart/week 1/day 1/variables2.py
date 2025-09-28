# System functions

usuario = "camilo"
print(len(usuario)) # len() counts the number of characters in a string

print("This is my client", usuario)

# variables in a single line

name, surname, alias, age = "Bill", "Gates", "BillG", 65
print("My name is", name, surname, "i am", age, "years old. And my alias is:", alias)

# input function

name = input("Whats your name: ")
age = input("How old are you? ")
print(name)
print(age)

# swapping values

name = 35
age = "Camilo"
print(name)
print(age)

# type hinting

address: str = "My street" 
address = 32
print(address)
# the type hinting is just a hint, it does not enforce the type