word1 = input("Enter a word to reverse: ")
reversed_word = ""

for i in range(len(word1) -1, -1, -1):
    reversed_word = reversed_word + word1[i] # or reversed_word += word1[i]

print(reversed_word)