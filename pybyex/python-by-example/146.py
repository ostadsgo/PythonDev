def encode(s, shift):
    # s[(index_ch - len(ch)) + 1]
    letters = 'abcdefghijklmnopqrstuvwxyz '
    res = "" 
    for ch in s:
        index = letters.find(ch)
        if index != -1:
            e_index = index + shift

        if ch == 'z':
            e_index = shift - 1

        res += letters[e_index]
    return res


def decode(s, shift):
    letters = 'abcdefghijklmnopqrstuvwxyz '
    res = "" 
    for ch in s:
        index = letters.find(ch)
        res += letters[index-shift]

    return res
    


def main():
    menu = """
    1) Make a code
    2) Decode a message
    3) Quit
    """
    import os
    while True: 
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print(menu)
        response = input("> ")
        shift = 1
        if response == '1':
            s = input("Enter somthing to encode: ")
            res = encode(s, shift)
            print(res)
            input("Press any key...")
        elif response == '2':
            s = input("Enter somthing to decode: ")
            res = decode(s, shift)
            print(res)
            input("Press any key...")
        elif response == '3':
            break
        else:
            print("Error! Wrong choice.")

if __name__ == "__main__":
    main()


