numbers = [10, 20, 30, 20, 10, 40, 30]
unique_numbers = set(numbers)

print("Original:", numbers)
print("Unique:", unique_numbers)

numbers_no_duplicates = list(unique_numbers)
print(numbers_no_duplicates)

# We can use this for eliminate duplicates in a list transforming it to a set and after transform to list again