import random
import os


def messages(winner: str):
    msg = {
        "Rock": "Rock crushes scissors",
        "Paper": "Paper covers rock",
        "Scissors": "Scissors cuts paper",
    }
    return msg.get(winner)


def get_winner(computer_hand, user_hand):
    """Return 0 if computer and user has the same hand
    Return 1 if user win
    Return -1 if computer win(user lose)
    """
    if computer_hand == user_hand:
        return 0
    elif computer_hand == "Rock" and user_hand == "Scissors":
        return -1
    elif computer_hand == "Paper" and user_hand == "Rock":
        return -1
    elif computer_hand == "Scissors" and user_hand == "Paper":
        return -1
    else:
        return 1


# Determine who is the winner
def play(computer, user):
    if computer == user:
        return "A Draw Play Again", "No One"
    if computer == "Rock" and user == "Scissors":
        return messages(computer), "Computer"
    elif computer == "Paper" and user == "Rock":
        return messages(computer), "Computer"
    elif computer == "Scissors" and user == "Paper":
        return messages(computer), "Computer"
    else:
        return messages(user), "You"


def play2(computer, user):
    result = get_winner(computer, user)
    if result == 0:
        return "A Tie!", ""
    elif result == 1:
        return "You Win", ""
    elif result == -1:
        return "You Lose", ""


def rand_hand(hands):
    """Create random hand form the list."""
    return random.choice(hands)


def main():
    choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    computer_hand = random.choice(list(choices.values()))

    # clear console (teminal) screen before starting th game
    os.system("cls") if os.name == "nt" else os.system("clear")
    # Menu
    for index, choice in choices.items():
        print(f"[{index}] {choice}")

    response = input("Choose your hand: ")
    user_hand = choices.get(response)

    msg, winner = play2(computer_hand, user_hand)
    print("-" * 20)
    # print(f"{winner} Win\n{msg}")
    print(msg)


if __name__ == "__main__":
    main()
