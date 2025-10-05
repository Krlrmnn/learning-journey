word1 = input("Enter a word: ")

single_characters = ""

for chars in word1:
    if chars not in single_characters:
        single_characters += chars
print(single_characters)