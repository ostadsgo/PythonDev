subjects = ["Math", "Science", "History", "Music", "Art", "Sport"]

print(subjects)
response = input("Which subject that you don't like? ")
subjects.remove(response.title())

print(subjects)
