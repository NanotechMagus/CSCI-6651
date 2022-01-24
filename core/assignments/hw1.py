#!/etc/python

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: Homework 1

# Standard Library Imports
from random import randint

# Third-party Library Imports

# Local Library Imports

class hw1:
    """
        Part 1: High/Low Minigame -- guess if the next number is higher or lower than the current number.
        Part 2: Musical Chairs -- A silly mini-game with a decreasing number of chairs.  Last one standing wins.
    """
    def __init__(self):
        self.__players = {}
        self.parts = 2

    def start(self):
        return

    def high_low(self):
        print(f"Welcome to the High/Low Guessing game!\n")

    def get_players(self):
        print(f"There are currently {len(self.__players)} players.")
        if len(self.__players) is None:
            print("How many players are playing this game? ")
        else:
            print(f"Would you like to add more? Y/n ")