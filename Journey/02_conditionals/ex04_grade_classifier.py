note1 = int(input("Enter your score: "))
if 90 <= note1 <= 100:
    print("Your grade is A.")
elif 80 <= note1 < 90:
    print("Your grade is B.")
elif 70 <= note1 < 80:
    print("Your grade is C.")
elif 60 <= note1 < 70:
    print("Your grade is D.")
elif 0 <= note1 < 60:
    print("Your grade is F.")
else:
    print("Invalid score. Please enter a score between 0 and 100.")