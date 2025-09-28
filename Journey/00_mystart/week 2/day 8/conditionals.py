condition1 = True
condition2 = 11

if condition1:
    print("Condition 1 is True")

if condition2 == 11:
    print("Condition 2 equals 11")

print("The execution continues here.")

if condition2 >= 10 and condition2 < 20:
    print("Condition 2 is greater than or equal to 10 and less to 20")
elif condition2 == 20:
    print("Condition 2 is equal to 20")
else:
    print("Condition 2 is less than 10 or greater than 20")

print("The execution continues here again.")

if not condition1:
    print("Condition 1 is False")
if condition1 and (condition2 > 10 or condition2 < 5):
    print("Condition 1 is True and Condition 2 is greater than 10 or less than 5")
if condition1 or condition2 < 5:
    print("Condition 1 is True or Condition 2 is less than 5")