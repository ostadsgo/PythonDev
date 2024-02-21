foods = {1: "Kola", 2: "Chips", 3: "A food", 4: "Burgeer"}

print(foods)

index = int(input("Enter the number of the food you want to remove? "))

del foods[index]

foods = sorted(foods.values())
print(foods)
