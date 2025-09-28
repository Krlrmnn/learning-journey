nums1 = input("Enter 3 numbers: ")
nums2 = [int(i.strip()) for i in nums1.split(",")]
print("The maximum number is:", max(nums2))

# Alternative approach using conditional statements

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("The maximum number is:", a)
elif b >= a and b >= c:
    print("The maximum number is:", b)
else:
    print("The maximum number is:", c)

# NOTE: I used both the built-in max function and conditional statements to find the maximum of three numbers.