# While

condition1 = 0
while condition1 < 10:
    print(condition1)
    condition1 += 1 # condition1 = condition1 + 1
    # It is important to change the condition in some way, otherwise the loop will never end
else: # This else is optional
    print("My condition is higher or equal to 10") # This else is for the while, not for the if
if condition1 == 10:
    print("The loop is over") # This if is not related to the while loop
elif condition1 > 10: # This elif is not related to the while loop
    print("The condition is greater than 10")
else:
    print("The condition is less than 10")

print("The execution continues here.")

while condition1 < 20:
    condition1 += 1
    if condition1 == 15:
        print("The execution stops")
        break # It breaks the loop
        print("condition1 is 15, but we will continue")
        #continue # It goes back to the beginning of the loop
    print(condition1)

# For

list1 = [35, 24, 62, 52, 12]

for element in list1:
    print(element)

set1 = {"Prisma", "is", "learning", "Python"}

for element in set1:
    print(element)

tuple1 = (23, 45, 67, 89, 12)

for element in tuple1:
    print(element)

dict1 = {"name": "Prisma", "age": 29, "city": "Madrid"}

for element in dict1:
    print(element)
    if element == "age":
        break # It breaks the loop
    print("It isnt age")    
else:
    print("The for loop is over")

for element in dict1.values(): # It iterates over the values
    print(element) # It prints the values

# The "element" variable can be named as you want

for element in dict1:
    print(element)
    if element == "age":
        continue # It goes back to the beginning of the loop
    print("It executes")
else:
        print("It isnt age")