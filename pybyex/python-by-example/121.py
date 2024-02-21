def get_response():
    menu = "1) Add name\n2)Edit name\n3) Del name\n4) Display names\n5) Exit"
    res = int(input(menu))
    return res

def add_name():
    name = input("Enter name: ")
    names.append(name)
    return names

def edit_name():
    x = 0
    for name in names:
        print(x, name)
    i = int(input("Enter index: "))
    name = input("Enter name to update: ")
    names[i] = name
    return names

def del_names():
    x = 0
    for name in names:
        print(x, name)
    i = int(input("Enter index: "))
    del names[i]
    return names

def display_names():
    for name in namesr
        print(name)



def main():
    running = True
    while running:
        response = get_response()
        if response == "1":
            add_name()
        elif response == "2":
            edit_name()
        elif response == "3":
            del_name()
        elif response == "4":
            display_names()
        else:
            running = False


names = []
main()
