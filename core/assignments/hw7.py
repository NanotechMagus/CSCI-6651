#!/etc/python-3.9

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: [insert assignment name or number]

# Standard Library Imports
from random import randint

# Third-party Library Imports

# Local Library Imports


class hw7:
    """
        1. Lottery number Generator
            Design a program that generates a seven-digit lottery number. The program should
            generate seven random numbers, each in the range of 0 through 9, and assign each
            number to a list element. Then write another loop that displays the contents of the list.
        2. Rainfall statistics
            Design a program that lets the user enter the total rainfall for each of 12 months into a
            list. The program should calculate and display the total rainfall for the year, the average
            monthly rainfall, and the months with the highest and lowest amounts.
        3. number Analysis program
            Design a program that asks the user to enter a series of 20 numbers. The program
            should store the numbers in a list and then display the following data:
                The lowest number in the list
                The highest number in the list
                The total of the numbers in the list
                The average of the numbers in the list
        4. Larger Than n
            In a program, write a function that accepts two arguments: a list, and a number n.
            Assume that the list contains numbers. The function should display all the numbers in
            the list that are greater than the number n.
        5. Lo shu Magic square
            The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown below. The Lo
            Shu Magic Square has the following properties:
            The grid contains the numbers 1 through 9 exactly.
            The sum of each row, each column, and each diagonal all add up to the same number.
            In a program you can simulate a magic square using a two-dimensional list. Write a
            function that accepts a two-dimensional list as an argument and determines whether
            the list is a Lo Shu Magic Square. Test the function in a program
    """
    def __init__(self):
        self.__months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
        return

    def lottery(self):
        win_nums = []
        print("Today's lotto numbers are.... (drumroll please):")

        for x in range(1, 9):
            print(f"The number {self.lotto_gen(1, 9, win_nums)} is drawn!")

        print("Check your tickets, the winning numbers are ", end="")
        for winning in win_nums:
            print(f"{winning}, ", end="")

    def lotto_gen(self, min: int, max: int, win_nums: list):
        lotto_num = randint(min, max)
        if lotto_num not in win_nums:
            win_nums.append(lotto_num)
            return lotto_num
        else:
            self.lotto_gen(min, max, win_nums)

    def start(self):
        return

    def rainfall(self):
        # List comprehension -- Should I use lists or dicts to be more verbose in data
        data = []
        highest = (None, 0)
        lowest = (None, 10000)
        total = 0
        print("Please enter the data for the following months.")
        for month in self.__months:
            data.append((month, input(f"{month}'s Total Rainfall:")))

        for x in data:
            total += x[1]
            if x[1] > highest[1]:
                highest = x
            if x[1] < lowest[1]:
                lowest = x
            print(f"{x[0]}: {x[1]}")

        print(f"Total rainfall: {total}\n"
              f"Highest rainfall: {highest[0]} {highest[1]}\n"
              f"Lowest rainfall: {lowest[0]} {lowest[1]}")
        return

    def listcomp(self):
        return

    def loshu(self):
        return


if __name__ == "__main__":
    runonce = hw7()
    runonce.start()