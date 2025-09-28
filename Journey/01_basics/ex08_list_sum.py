nums = input("Enter a list of numbers separated by comas: ")
num_list = nums.split(",")
total = 0

for num in num_list:
    total = total + int(num.strip())
print(f"The sum of your numbers is {total}")