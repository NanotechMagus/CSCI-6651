#!/etc/python

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: Homework 1

# Standard Library Imports
from random import randint
from time import sleep

# Third-party Library Imports

# Local Library Imports

# Constants
pTemplate = {
    "HLGuess": None,
    "isOut": False
}

class hw1:
    """
    Homework 1:
        Part 1: High/Low Minigame -- guess if the next number is higher or lower than the current number.
        Part 2: Musical Chairs -- A silly mini-game with a decreasing number of chairs.  Last one standing wins.
    """
    def __init__(self):
        self.__players = {}
        self.parts = 2
        self.__randNum = randint(0, 10)
        self.__playAgain = True

    def __get_players(self):
        print(f"There are currently {len(self.__players.keys())} players.")
        while(True):
            if input(f"Would you like to add another? y/N:  ") is ("Y" or "y"):
                    self.__set_players()
            else:
                break

    def __set_players(self):
        self.__players[(input("What is your name?: "))] = pTemplate

    def __again(self):
        if input("Would you like to play again? (y/N): ") is ("Y" or "y"):
            self.__players = {}
            self.__playAgain = True
        else:
            self.__playAgain = False

    def __update_number(self):
        newRand = randint(0, 10)
        if newRand != self.__randNum:
            self.__randNum = newRand
            return self.__randNum
        else:
            self.__update_number()

    def __getHLanswer(self):
        for player in self.__players.keys():
            if self.__players[player]["isOut"]:
                pass
            answer = input(f"{player}, would you like to guess High or Low? :")
            self.__players[player]["HLGuess"] = answer.lower()

    def high_low(self):
        print(f"Welcome to the High/Low Guessing game!\n")
        print("Lets get started!")

        if len(self.__players) == 0:
            self.__set_players()
        else:
            self.__get_players()

        while self.__playAgain is True:

            print(f"The number is {self.__randNum}! \n"
                  f"Time to make your guesses!")
            self.__getHLanswer()
            print(f"\nAll guesses are in!\n\n")

            oldNum = self.__randNum
            print(f"The new number is {self.__update_number()}!  Lets see who won.\n")
            answer = "high" if oldNum < self.__randNum else "low"
            print(f"The correct guess is {answer}!")

            for player in self.__players.keys():
                if self.__players[player]["HLGuess"] == answer:
                    print(f"{player} guessed right!")
                else:
                    print(f"{player} guessed wrong!  Sorry, you're out.")
                    self.__players[player]["isOut"] = True

            self.__again()

    def chairs(self):
        # I wrote this part in about 10 minutes because I forgot the homework was in two parts.
        # Trying to make this game work I don't know how it's feasible through CLI, so I'm writing exactly what the
        # HW requires
        if len(self.__players) == 0:
            self.__set_players()
        else:
            self.__get_players()

        order = []
        print("Players Stand")
        sleep(randint(5,20))
        input("Players Sit (input your name): ")
        for x in range(len(self.__players.keys())):
            order.append(input(""))

        print(f"{order.pop()} missed the chair!")

    def start(self):
        while(True):
            print("Welcome to the Homework 1 assignment written by Brandon Frostbourne. \n Please choose an assignment.\n")
            print("1) High/Low Guessing Game")
            print("2) Musical Chairs (a work in progress)")
            print("3) Exit")
            hw1choice = input("\nMake your selection: ")
            if hw1choice == "1":
                self.high_low()
            elif hw1choice == "2":
                self.chairs()
            elif hw1choice == "3":
                return
            else:
                print(f"Selection {hw1choice} is not valid.  Please try again.\n")


if __name__ == "__main__":
    runonce = hw1()
    runonce.start()
