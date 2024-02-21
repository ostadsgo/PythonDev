import csv
import os
import string


# save to a csv file
def _save(filename, row):
    with open(filename, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row)
    return True

def _write(filename, rows):
    fields = ["userid", "password"]
    with open(filename, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writerows(rows)

# read from csv file
def _read(filename):
    with open(filename) as csv_file:
        fieldnames = ["userid", "password"]
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)
        data = list(reader)
    return data


def validate_password(password):
    save_pass = False   # if true password with the userid will be saved
    validators = [
        len(password) >= 8,
        any(True for ch in password if ch.isupper()),
        any(True for ch in password if ch.islower()),
        any(True for ch in password if ch.isdigit()),
        any(True for ch in password if ch in string.punctuation),    ]

    score = validators.count(True)
    if 1 <= score <= 2:
        print("Week password.")
        save_pass = False
    elif 3 <= score < 5:
        print("This passwrod could be improved.")
        save_pass = False
    elif score >= 5:
        print("Strong password; good job.")
        save_pass = True

    return save_pass


def create_new_user_id():
    user_id = input("Enter user id: ")
    all_ids = [item.get("userid") for item in _read("users.csv")]
    if user_id not in all_ids:
        password = input("Enter a password: ")
        is_password_strong = validate_password(password)
        if is_password_strong:
            # save userid and password if it is strong
            _save("users.csv", row=(user_id, password))
            print("userid and password saved successfuly.")
    else:
        print(f"The id {user_id} is exist try to use another id.")

def display_all_user_id():
    all_ids = [item.get("userid") for item in _read("users.csv")]
    for userid in all_ids:
        print(userid)

def _find_user(userid):
    """ Search users to find the user.
        If user found return the user index in the users list.
        If user not found return None.
    """
    users = _read("users.csv")
    for index, user in enumerate(users):
        if user.get("userid") == userid:
            return index
    return None


def change_password(userid):
    users = _read("users.csv")
    save_data = False
    # first I need to find the user from users
    index = _find_user(userid)
    if index is not None:
        new_paswd = input("New password: ")
        if validate_password(new_paswd):
            users[index]["password"] = new_paswd
            save_data = True
    else:
        print("user not found!")

    if save_data:
        _write("users.csv", users)



menu = """
1) Create an new User ID
2) Change a password
3) Display all User ID
4) Quit
Enter Selection: 
"""


while True:
    os.system('clear') if os.name == "posix" else os.system('cls')
    print(menu)
    response = input("> ")
    if response == "1":
        create_new_user_id()
    elif response == "2":
        userid = input("Enter a userid: ")
        change_password(userid)
    elif response == "3":
        display_all_user_id()
    elif response == "4":
        break
    else:
        print("Wrong choice!!!")

    input("Press any key to continue ...")
