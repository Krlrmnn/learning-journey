num1 = int(input("Enter a number: "))
even_numbers = [num for num in range(1, num1 + 1) if num % 2 == 0]
print(f"The even numbers from 1 to {num1} are: {even_numbers}")