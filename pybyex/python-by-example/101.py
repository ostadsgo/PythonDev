sales = [
    {"John": {"N": 3050, "S": 8463, "E": 8441, "W": 2694},
    {"Tom": {"N": 2342, "S": 32424, "E": 1233, "W": 8787},
    {"Anne": {"N": 9372, "S": 9283, "E": 7473, "W": 1112},
    {"Fiona": {"N": 8378, "S": 1293, "E": 8838, "W": 9993},
]

name = input("Enter a name: ")
region = input("Enter a region: ")
print(sales[name][region])

sales[name][region] = int(input("Enter new sale: ")) 

print(sales[name])
