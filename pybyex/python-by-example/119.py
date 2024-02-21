import random


def get_random():
    low = int(input("Enter a number: "))
    high = int(input("Enter a number bigger than the last number: "))
    comp_num = random.randrange(low, high)
    return comp_num

def guess_num():
    print("I'm thinking of an number ... ")
    guess = int(input("guess me > "))
    return guess

def main():
    comp_num = get_random()
    running = True
    while running:
        guess = guess_num()
        if comp_num == guess:
            print("You win.")
            running = False
        elif comp_num > guess:
            print("Guess high.")
        else:
            print("Guess low.")
        

main()



