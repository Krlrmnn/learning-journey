age = int(input("Enter your age: "))
citizenship = input("Are you a colombian citizen? (yes/no): ")
citizenship = citizenship.strip().lower()

if age >= 18 and citizenship == "yes":
    print("You can vote")
elif age < 18:
    print("You are too young to vote")
elif citizenship != "yes":
    print("You must be a colombian citizen to vote")