num1 = int(input("Enter a number: "))

while num1 != 0:
    if num1 == 0:
        print("The number is zero.")
    elif num1 > 0:
        print("The number is positive.")
    else:
        print("The number is negative.")
    break
# NOTE: This version uses a while loop instead of a simple if/elif/else.
# Because of the condition (while num1 != 0), it doesn't handle the "zero" case correctly.
# I kept it this way to document my own approach and learning process.