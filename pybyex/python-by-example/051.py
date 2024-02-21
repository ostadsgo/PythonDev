bottle_num = 10

while bottle_num > 0:
    print("There are", bottle_num, "green bottle hanging on the wall if 1 green bottle should accidentally fall.")
    ans = int(input("how many green bottles will be hanging on the wall? "))

    bottle_num -= 1

    if ans == bottle_num:
        print("There will be", bottle_num, "hanging on the wall.")
    else:
        while ans != bottle_num:
            ans = int(input("No, try again: "))

print("There are no more green bottle on the wall.")
