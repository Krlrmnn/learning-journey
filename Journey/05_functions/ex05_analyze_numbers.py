def analyze_numbers(numbers):
    if not numbers:
        return "No numbers provided."
    
    max_num = numbers[0]
    min_num = numbers[0]
    total_sum = 0

    for n in numbers:
        if max_num < n:
            max_num = n
        if min_num > n:
            min_num = n
        total_sum = total_sum + n
    
    average = total_sum / len(numbers)

    return f"Max: {max_num} | Min: {min_num} | Average: {average} | Total: {total_sum}"
        


numbers = input("Enter a list of numbers separated by comas: ").strip()
numbers = [float(n) for n in numbers.split(",")]
print(analyze_numbers(numbers))