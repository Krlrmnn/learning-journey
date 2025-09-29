password1 = input("Enter your password: ")
password = "secure123"
attempts = 3

while attempts > 0:
    if password1 == password:
        print("Access granted")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect password. You have {attempts} attempts left.")
            password1 = input("Enter your password: ")
        else:
            print("Access denied. No attempts left.")