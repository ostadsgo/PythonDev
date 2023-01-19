""" Creating a rock paper sccisors game with python 
    and tkinter 
"""

import random
import tkinter as tk

from PIL import Image, ImageTk
from tkinter import ttk

from rps import get_winner, rand_hand


class Game:
    """ Main class to play the game. Logic part of the game. """
    ties = 0
    comp_wins = 0
    user_wins = 0

    def __init__(self):
        pass

    @staticmethod
    def play(hand):
        """ Play game and return the winner. """
        computer = rand_hand(hand.HANDS)
        user = hand.name
        winner = get_winner(computer, user)
        return winner

    @staticmethod
    def update_score(winner):
        if winner == 0:
            Game.ties += 1
        elif winner == 1:
            Game.user_wins += 1
        elif winner == -1:
            Game.comp_wins += 1
        

class Hand:
    """ Player hand (rock, paper, scissors) """
    HANDS = ["Rock", "Paper", "Scissors"]

    def __init__(self, master, name, img):
        self.master = master
        self.name = name
        self.img = ImageTk.PhotoImage(Image.open(img))
    
    def show(self):
        label = ttk.Label(self.master, image=self.img) 
        label.pack(side=tk.LEFT)
        label.bind("<Button-1>", self.onclick)

    def onclick(self, event):
        res = Game.play(self)
        Game.update_score(res)
        # update dashboard play board
        Dashboard.update([Game.ties, Game.comp_wins, Game.user_wins])


class Dashboard:
    """ Display the result of the game. """
    message = None

    def __init__(self, master):
        self.master = master
        Dashboard.message = ttk.Label(self.master, font="24", foreground="blue")
        Dashboard.message.pack()
        
    
    def show(self):
        Dashboard.message["text"] = "Game Play Board\n" 
        Dashboard.message["text"] += "Ties = 0\n"
        Dashboard.message["text"] += "Computer Wins = 0\n"
        Dashboard.message["text"] += "User Wins = 0"

    @staticmethod
    def update(values):
        """ Update dashboard based on winner. """
        text = "Game Play Board\n"
        text += "Ties: {}\nComputer Wins: {}\nUser Wins: {}".format(*values)
        Dashboard.message["text"] = text 

def main():
    root = tk.Tk()
    root.title("ROCK PAPER SCISSORS")
    mainframe = ttk.Frame(root)
    
    handframe = ttk.Frame(mainframe)
    rock = Hand(handframe, "Rock", "./img/rock.png")
    paper = Hand(handframe, "Paper", "./img/paper.png")
    scissors = Hand(handframe, "Scissors", "./img/scissors.png")
    rock.show()
    paper.show()
    scissors.show()
    handframe.pack()
    
    dashframe = ttk.Frame(mainframe)
    dashboard = Dashboard(mainframe)
    dashboard.show()
    dashframe.pack()
    
    mainframe.pack(fill=tk.BOTH)
    root.mainloop()


if __name__ == "__main__":
    main()

