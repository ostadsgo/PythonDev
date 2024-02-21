import csv

from random import randrange

rows = []
i = 0
name = input("Enter your name: ")
while i < 2:
    value1 = randrange(1, 100)
    value2 = randrange(1, 100)
    answer = value1 + value2

    question = str(value1) + " + " + str(value2)
    print(question)
    user_answer = int(input("Enter your answer: "))

    score = 0
    if answer == user_answer:
        score += 1
    row = (name, question, user_answer, score)
    rows.append(row)
    i += 1

file = open("Score.csv", "a")
csv_writer = csv.writer(file)

for row in rows:
    csv_writer.writerow(row)
file.close()




