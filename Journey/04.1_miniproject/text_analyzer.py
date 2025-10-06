sentence1 = input("Enter a sentence: ")

# Count the number of words

num_words = len(sentence1.split())

# Count the number of letters

alphabet = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
char_count = 0

for char in sentence1.replace(" ", ""):
    if char in alphabet: char_count += 1

# Count the number of vowels and consonants

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
vowels_count = 0
consonants_count = 0

for char in sentence1.replace(" ", ""):
    if char in vowels: vowels_count += 1
    elif char in consonants: consonants_count += 1

# Identify the larger word and its lenght

larger_word = max(sentence1.lower().split(), key=len)
larger_word_lenght = len(larger_word)

# Determinate if the sentence is a palindrome

palindrome_sentence = sentence1.lower()

if palindrome_sentence == palindrome_sentence[::-1]:
    yes_or_no = "yes"
else:
    yes_or_no = "no"

# Analyis report

print(f"-- Text Analysis Report --\nTotal words: {num_words}\nTotal letters: {char_count}\nVowels: {vowels_count}\nConsonants: {consonants_count}\nLongest_word: {larger_word}\nLongest word lenght: {larger_word_lenght}\nIs palindrome: {yes_or_no}")