password = input("Enter a password: ")
re_password = input("Enter the passowrd again: ")

if password == re_password:
    print("Thank you.")
elif password.lower() == re_password.lower():
    print("They must be in same case.")
else:
    print("Incorrect.")
