### 🧠 Mini Project — Text Analyzer

This mini project performs a basic analysis of a user-provided sentence.  
It counts words, letters, vowels, consonants, finds the longest word, and checks if the text is a palindrome.

---

#### ⚙️ How It Works
1. The user enters a sentence.  
2. The program:
   - Splits the sentence to count the total number of words.  
   - Iterates through each character to count only alphabetic letters.  
   - Counts vowels and consonants separately.  
   - Uses `max()` to identify the longest word and its length.  
   - Checks whether the sentence is a palindrome by comparing it to its reverse.  
3. Finally, a formatted report is displayed summarizing all metrics.

---

#### 🧩 Key Concepts Applied
- String manipulation and iteration  
- Conditional logic and loops  
- Use of accumulators for counting  
- String methods: `.split()`, `.replace()`, `.lower()`  
- Palindrome detection using slicing (`[::-1]`)  
- Clean output formatting with `f-strings`  