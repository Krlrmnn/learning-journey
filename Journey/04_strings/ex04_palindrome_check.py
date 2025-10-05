word1 = input("Enter a word: ")
word1 = word1.lower().replace(" ", "")

if word1 == word1[::-1]:
    print("Its a palindrome")
else:
    print("It isnt a palindrome")