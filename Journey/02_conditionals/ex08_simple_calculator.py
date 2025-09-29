num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
operation = operation.strip()

if operation not in ["+", "-", "*", "/"]:
    print("Error: Invalid operation.")
elif operation == "+":
    print(f"The result is {num1 + num2}")
elif operation == "-":
    print(f"The result is {num1 - num2}")
elif operation == "*":
     print(f"The result is {num1 * num2}")
elif operation == "/":
     if num2 == 0:
         print("Error: Division by zero is not allowed.")
     else:
         print(f"The result is {num1 / num2}")