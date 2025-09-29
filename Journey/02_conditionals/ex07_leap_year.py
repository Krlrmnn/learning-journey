year1 = int(input("Enter a year: "))
if year1 % 4 == 0:
    if year1 % 100 == 0:
        if year1 % 400 == 0:
            print(f"{year1} is a leap year")
        else:
            print(f"{year1} is not a leap year")
    else:
        print(f"{year1} is a leap year")
else:
    print(f"{year1} is not a leap year")