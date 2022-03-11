#!/etc/python-3.9

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: Test 1

# Standard Library Imports
from sys import exit

# Third-party Library Imports

# Local Library Imports


class Test1:
    """
        This is the first test for CSCI-6651 taught by George Pillar III at University of New Haven

        Usage:
            Program 1: Ingredient Adjuster:
                    Input the number of cookies the user wants to bake, and the program will provide the
                    correct amount of ingredients
            Program 2: Male and Female Percentages:
                    Input the number of males and females in a class.  The program will display the percentage of males
                    and females in the class.
            Program 3: Stock Transaction Program
                    A program that details the transactional data for Joe purchasing Acme Software Inc, stock.

            Please make a selection, or type 0 to exit.
    """
    def __init__(self):
        self.selection = {
            0: exit,
            1: self.ingredientadj,
            2: self.mandfpct,
            3: self.stocktrans
        }

    def ingredientadj(self):
        sugar = 1.5
        butter = float(1)
        flour = 2.75
        batch = 48

        cookies = int(input("Please enter the amount of cookies you want to bake using this recipe:  "))
        newbatch = cookies/batch

        print(f"The amount of ingredients needed is as follows:\n"
              f"Cookies:    {batch}\t\t\t{cookies}\n\n"
              f"Sugar:      {sugar} cups\t{sugar*newbatch:,.2f} cups\n"
              f"Butter:     {butter} cups\t{butter*newbatch:,.2f} cups\n"
              f"Flour:      {flour} cups\t{flour*newbatch:,.2f} cups")

    def mandfpct(self):
        males = int(input("How many males are in the classroom?: "))
        females = int(input("How many females are in the classroom?: "))
        print("\n\n")
        print(f"The number of males in the class are {males} which is {(males/(males+females))*100:,.2f}% of the class")
        print(f"The number of females in the class are {females} which is {(females/(males+females))*100:,.2f}% of the class")

    def stocktrans(self):
        sharesbought = {
            "number": 2000,
            "price": 40,
            "commissionrate": 0.03,
        }
        sharessold = {
            "number": 2000,
            "price": 42.75,
            "commissionrate": .03
        }

        total_bought = sharesbought['number'] * sharesbought['price']
        total_bought_commmission = total_bought * sharesbought['commissionrate']
        total_sold = sharessold['number'] * sharessold['price']
        total_sold_commission = total_sold * sharessold['commissionrate']

        print(f"Joe's stock transaction details:\n\n"
              f"Initial transaction - shares bought\n"
              f"Total paid:\t{total_bought:,.2f}\n"
              f"Total commission paid:\t{total_bought_commmission:,.2f}"
              f"\n\n"
              f"Sold Shares:\n"
              f"Total sold:\t{total_sold}\n"
              f"Total commission paid:\t{total_sold_commission:,.2f}"
              f"\n\n")

        if total_sold - (total_bought + total_bought_commmission + total_sold_commission) > 0:
            print("Joe made profit!")
        else:
            print("Joe lost money!")


    def start(self):
        while True:
            try:
                choice = int(input(self.__doc__))
                self.selection[choice]()
            except Exception as err:
                print("I didn't understand that, please try again")


if __name__ == "__main__":
    runonce = Test1()
    runonce.start()