nums1 = input("Enter a list of numbers separated by comas: ")
nums_list = [int(num.strip()) for num in nums1.split(",")]

sum_nums = sum(nums_list)
count_nums = len(nums_list)

average = sum_nums / count_nums if count_nums > 0 else 0

print(f"The average of the list is: {average}")