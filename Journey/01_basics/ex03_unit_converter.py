temp = input("Enter the type of conversion (C to F, F to C): ")
value = float(input("Enter the value to convert: "))
if temp == "C to F":
    converted = (value * 9/5) + 32
    print(f"{value}°C is {converted}°F")
elif temp == "F to C":
    converted = (value - 32) * 5/9
    print(f"{value}°F is {converted}°C")