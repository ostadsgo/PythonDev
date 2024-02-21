numbers = [
        [2, 5, 8],
        [3, 7, 4],
        [1, 6, 9],
        [4, 2, 0]
]

row = int(input("Which row would you like to display: "))
print(numbers[row])

col = int(input("Enter the column index: "))

print(numbers[row][col])

response = input("Do you want to change the value(y/n): ")
if response == "y":
    value = int(input("Enter a new value: "))
    numbers[row][col] = value


print(numbers[row])

