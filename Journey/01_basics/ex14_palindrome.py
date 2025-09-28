palindrome1 = input("Enter a word: ")
if palindrome1 == palindrome1[::-1]:
    print(f"{palindrome1} is a palindrome.")
else:
    print(f"{palindrome1} is not a palindrome.")