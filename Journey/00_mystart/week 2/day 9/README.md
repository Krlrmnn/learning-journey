# Documentation
## Personal note: I'm starting to like the software, more than I already did.
'''python
## Description
This script demonstrates the use of while and for loops, as well as conditional statements (if, elif, else) in Python. It also shows how to iterate over different data structures: lists, sets, tuples, and dictionaries.

# How it works
## While Loop
1. First while loop:
condition1 = 0
while condition1 < 10:
    print(condition1)
    condition1 += 1
else:
    print("My condition is higher or equal to 10")

- Prints numbers from 0 to 9.
- The else block runs after the loop ends.
2. Conditional statements after the loop:
if condition1 == 10:
    print("The loop is over")
elif condition1 > 10:
    print("The condition is greater than 10")
else:
    print("The condition is less than 10")

- Checks the value of "condition1" and prints a message accordingly.
3. Second while loop with break:
while condition1 < 20:
    condition1 += 1
    if condition1 == 15:
        print("The execution stops")
        break
    print(condition1)

- Increments condition1 until it reaches 15, then prints a message and breaks the loop.
## For Loops
1. Iterating over a list:
list1 = [35, 24, 62, 52, 12]
for element in list1:
    print(element)

- Prints each element in the list.
2. Iterating over a set:
set1 = {"Prisma", "is", "learning", "Python"}
for element in set1:
    print(element)

- Prints each element in the set (order is not guaranteed).
3. Iterating over a tuple:
tuple1 = (23, 45, 67, 89, 12)
for element in tuple1:
    print(element)

- Prints each element in the tuple.
4. Iterating over a dictionary (keys):
dict1 = {"name": "Prisma", "age": 29, "city": "Madrid"}
for element in dict1:
    print(element)
    if element == "age":
        break
    print("It isnt age")
else:
    print("The for loop is over")

- Prints each key in the dictionary.
- If the key is "age", breaks the loop.
- The else block runs if the loop is not broken.
5. Iterating over dictionary values:
for element in dict1.values():
    print(element)

- Prints each value in the dictionary.
6. For loop with continue:
for element in dict1:
    print(element)
    if element == "age":
        continue
    print("It executes")
else:
    print("It isnt age")

- Prints each key.
- If the key is "age", skips the next print statement and continues with the next iteration.
- The else block runs after the loop ends.
## Notes
- The break statement exits the loop immediately.
- The continue statement skips the rest of the current iteration and moves to the next.
- The else block after a loop runs only if the loop was not terminated by a break.
- The variable name element can be changed to any valid identifier.