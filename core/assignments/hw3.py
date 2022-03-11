#!/etc/python

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: Homework 3

# Standard Library Imports
from sys import exit

# Third-party Library Imports

# Local Library Imports

class hw3:
    """

    """

    def __init__(self):
        self.__doweek = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
        self.__choice = {
            0: exit,
            1: self.days,
            2: self.compRec,
            3: self.age,
            4: self.romanNumerals
        }

    def days(self):
        num_day = int(input("Input a number 1-7, and I will tell you the day of the week it is!"))
        for index, days in enumerate(self.__doweek, start=1):
            if num_day == index:
                print(f"You selected {num_day}, which is {days}")

    def compRec(self):
        recNum = int(input("How many rectangles are we comparing today to find the largest area?: "))
        recvals = []
        for x in range(recNum):
            self.__getCompRec(recvals)
        L, W, A = self.__calcLargest(recvals)
        print(f"The largest rectangle is {L}x{W} with an area of {A}")

    def __getCompRec(self, recvals):
        rec1x = int(input("What is the length of the rectangle?: "))
        rec1y = int(input("What is the width of the rectangle?: "))
        recvals.append((rec1x, rec1y, (rec1x*rec1y)))

    def __calcLargest(self, recvals:list):
        largest = 0
        highest = ()
        for rectangles in recvals:
            if rectangles[2] > largest:
                highest = rectangles
                largest = rectangles[2]
        return highest[0], highest[1], highest[2]

    def age(self):
        ageclassifier = [
            (0,1,"baby"),
            (1,13, "child"),
            (13, 20, "teenager"),
            (20, 5000, "adult")
        ]
        age = int(input("What is your age?"))
        for ages in ageclassifier:
            if ages[0] < age <= ages[1]:
                print(f"Aha!  Based on your age of {age}, you are a(n) {ages[2]}")
            else:
                print("I don't think I caught that age correctly.")

    def romanNumerals(self):
        romnum = {
            1: ("I", "V"),
            2: ("X", "L"),
            3: ("C", "D"),
            4: ("M", "V̅"),
            5: ("X̅", None)
        }
        roman = ""
        arabicnum = int(input("Write in a whole number less than 10,000 and I will convert it to roman numerals!: "))
        index = len(str(arabicnum))
        for digit in str(arabicnum):
            if 5 <= int(digit) <= 9:
                if int(digit) != 9:
                    roman += romnum[index][1]
                    for x in range(0, (int(digit)-5)):
                        roman += romnum[index][0]
                elif int(digit) == 9:
                    roman += romnum[index][0] + romnum[index][1]
            else:
                if int(digit) != 4:
                    for x in range(0, (int(digit))):
                        roman += romnum[index][0]
                else:
                    roman += romnum[index][0] + romnum[index][1]
            index -= 1
        print(f"{arabicnum} is {roman} in Roman Numerals!")

    def start(self):

        return


if __name__ == "__main__":
    runonce = hw3()
    runonce.start()
