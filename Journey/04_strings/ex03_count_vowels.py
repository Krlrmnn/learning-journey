word1 = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0

for char in word1:
    if char in vowels: count += 1
print(f"The number of vowels is {count}")