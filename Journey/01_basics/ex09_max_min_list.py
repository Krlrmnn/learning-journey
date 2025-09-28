nums1 = input("Enter a list of numbers separated by comas: ")
nums_list = [int(num.strip()) for num in nums1.split(",")]

max_num = max(nums_list)
min_num = min(nums_list)

print(f"The maximum number is {max_num}")
print(f"The minimum number is {min_num}")