print("1) Square: ")
print("2) Triangle: ")

user_input = input("Enter a number: ")

if user_input == "1":
    length = int(input("Enter the length of the square: "))
    area = length * length
    print("Area is", area)
elif user_input == "2":
    base = int(input("Enter base for the triangle: "))
    height = int(input("Enter height of the triangle: "))
    area = base * height / 2
    print("Area is", area)
else:
    print("Error, Incorrect response.")
