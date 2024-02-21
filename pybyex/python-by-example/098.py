numbers = [
        [2, 5, 8],
        [3, 7, 4],
        [1, 6, 9],
        [4, 2, 0]
]

row = int(input("Enter the row index: "))
print(numbers[row])

value = int(input("Enter a new number: "))
numbers[row].append(value)
