numbers = [4, 8, 2, 4, 5]

file = open("Numbers.txt", 'w')
for number in numbers:
    file.write(str(number) + ",")


