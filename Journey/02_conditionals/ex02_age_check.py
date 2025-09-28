age = int(input("Enter ur age: "))

if age < 18:
    print("Your are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")