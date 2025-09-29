## 📂 Conditionals

This folder contains beginner-friendly exercises to practice conditional statements (`if`, `elif`, `else`).  
The focus is on learning how to control program flow and apply logical checks.

### Exercises
- **ex01_number_sign.py**  
  Ask the user for a number and determine if it is positive, negative, or zero.

- **ex02_age_group.py**  
  Classify a person as minor, adult, or senior citizen based on their age.  
  Practiced **chained comparisons** for ranges.

- **ex03_max_of_three.py**  
  Determine the largest of three numbers.  
  - Solution 1: Using conditionals (`if/elif/else`).  
  - Solution 2: Using Python’s built-in `max()` function.  
  *Note: Both solutions are kept to show different approaches.*

- **ex04_grade_classifier.py**  
  Assign a grade (A–F) based on the user’s score. Practiced **ranges with chained comparisons**.

- **ex05_even_or_odd.py**  
  Check whether a given number is even or odd using the modulus operator `%`.

- **ex07_leap_year.py**  
  Determines if a given year is a leap year based on the rules:  
  - Divisible by 4 → candidate.  
  - Divisible by 100 → not leap, unless divisible by 400.  

- **ex08_calculator.py**  
  A simple calculator that takes two numbers and an operation (`+`, `-`, `*`, `/`).  
  - Includes error handling for invalid operations and division by zero.  

- **ex09_triangle_type.py**  
  Classifies a triangle given the lengths of its sides:  
  - Checks validity (positive sides + triangle inequality).  
  - Equilateral / Isosceles / Scalene.  

- **ex10_voting_eligibility.py**  
  Verifies if the user is eligible to vote in Colombia:  
  - Must be 18 or older.  
  - Must be a Colombian citizen (`yes`).  
  - Input normalized with `.strip().lower()`.

---

### Notes
This block introduced:
- How to build conditions with `if/elif/else`.  
- Chained comparisons for cleaner range checks.  
- Two different approaches to solving the same problem (manual logic vs. built-ins).  
- Basic application of the modulus operator `%`.