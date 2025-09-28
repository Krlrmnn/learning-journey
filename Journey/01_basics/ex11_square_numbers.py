nums1 = input("Enter a list of numbers separated by comas: ")
nums_list = [float(num.strip())**2 for num in nums1.split(",")]

print(f"The square of the list is: {nums_list}")