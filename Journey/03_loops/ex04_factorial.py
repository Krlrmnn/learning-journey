num1 = int(input("Enter a number: "))
total = 1

for n in range(1, num1 + 1):
    total = total * n
    print(total)
print(f"The factorial of {num1} is {total}")