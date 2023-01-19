import os
import brain_stretch as brain

os.system("clear")


def menu():
    operator = input("Choice +, -, *, /: ")
    correct_response = 0
    n = counter = 3
    start_range, end_range = (100, 900)
    total_response_time = 0
    check_mark = "✅"
    cross_mark = "❌"
    equations = []

    while n > 0:
        # create random numbers
        number1 = brain.get_random_number(start_range, end_range)
        number2 = brain.get_random_number(start_range, end_range)
        equation = f"{number1} {operator} {number2}"

        # get response and set start and end time
        start_time = brain.current_time()
        response = int(input(f"{equation} = "))
        end_time = brain.current_time()

        # calculate response and total response time
        response_time = brain.get_time_diff(start_time, end_time)
        total_response_time += response_time
        # get answer of a equation
        answer = brain.calculate(equation)
        if brain.compare(answer, response):
            equation = f"{check_mark} {equation} = {answer}"
            correct_response += 1
        else:
            equation = f"{cross_mark} {equation} = {answer}"
        equations.append(equation)

        # clear everything and print each equation that formated
        os.system("clear")
        for equation in equations:
            print(equation)

        n -= 1

    print(f"Total Time {round(total_response_time, 2)}")
    if correct_response == counter:
        scores = brain.get_socres()
        score = round(total_response_time, 2)
        scores = brain.compare_scores(score, scores)
        brain.save_score(scores)
        print("Score Saved!")


if __name__ == "__main__":
    menu()
