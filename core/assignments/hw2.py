#!/etc/python

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: Homework 2

# Standard Library Import
import sys

# Third-party Library Imports

# Local Library Imports

class hw2:
    """
    Homework 2:
        1) Sales Prediction     - Predict profits based on 23% of input sales
        2) Land Calculation     - Calculate Acreage from sq ft. input.
        3) Total Purchase       - Calculate total value of up to 5 items with assumed 7% sales tax
        4) Distance Travelled   - Calculate the distance a car travelling at 70mph at various intervals
        5) Sales Tax            - Deconstruct a purchase's value and each tax bracket given 5% state and 2.5% county
        6) Miles Per Gallon     - Calculate the MPG of a car given the miles travelled and gallons of gas used
        7) Tip, Tax, and Total  - Calculate the Tip, Tax, and Total of a meal given the initial cost of food
        8) C to F Temp Converter- Convert C to F given temperature in C
    """

    def __init__(self):
        self.choice = {
            0: sys.exit,
            1: self.__salesPred,
            2: self.__landCalc,
            3: self.__totPurch,
            4: self.__disTrav,
            5: self.__salesTax,
            6: self.__mpg,
            7: self.__tipTaxTot,
            8: self.__c2f,
            "help": self.selection
        }

    def help(self):
        print(self.__doc__)

    def selection(self):
        self.help()
        return input("\nPlease make a selection (0 to quit, help to show this again): ")

    def __continue(self):
        return input('Press enter to continue...')

    def __salesPred(self):
        sales = input('Please enter your current sales: ')
        print(f"Your profits are ${float(sales) * 0.23:.2f}.")
        self.__continue()

    def __landCalc(self):
        sqft = input('Please enter the total number of square feet: ')
        print(f"You have {float(sqft)/43560:.4f} acres.")
        self.__continue()

    def __totPurch(self):
        counting = [
            "first",
            "second",
            "third",
            "fourth",
            "fifth"
        ]
        price = 0
        for term in counting:
            price += float(input(f"Input your {term} item's price: $"))
        print(f"Subtotal: ${price:.2f}"
              f"\nTotal Sales Tax: ${price*0.07:.2f}"
              f"\nTotal cost: ${price*1.07:.2f}")
        self.__continue()

    def __disTrav(self):
        speed = float(input("What's your average speed on the interstate?"))
        print(f"At your current speed of {speed}mph, you will travel:\n"
              f"{speed*6:.2f} miles in 6 hours.\n"
              f"{speed*10:.2f} miles in 10 hours.\n"
              f"{speed*15:.2f} miles in 15 hours.\n")
        self.__continue()

    def __salesTax(self):
        purchase = float(input("Enter the total purchase amount in USD: "))
        print("With state sales tax being 5% and county sales tax at 2.5%: \n")
        print(f"Purchase amount: {purchase:.2f}"
              f"\nState Tax: ${purchase*0.05:.2f}"
              f"\nCounty Tax: ${purchase*0.025:.2f}"
              f"\nTotal Sales Tax: ${purchase*0.075:.2f}"
              f"\nTotal Sale before Tax: ${purchase*(1-0.075):.2f}")
        self.__continue()

    def __mpg(self):
        miles = float(input("Please input how many miles driven: "))
        gal = float(input("Please input the number of gallons used: "))
        print(f"Your average MPG is {miles/gal:.2f}")
        self.__continue()

    def __tipTaxTot(self):
        cost = float(input("Please input the cost of the meal (before tax): "))
        print(f"Meal cost: ${cost:.2f}"
              f"\nTip (18%): ${cost*.18:.2f}"
              f"\nSales Tax: ${cost*0.07:.2f}"
              f"\nTotal cost: ${cost*(1+0.18+0.07):.2f}")
        self.__continue()

    def __c2f(self):
        celsius = input("Please input a temperature value in Celsius: ")
        print(f"The Farenheit conversion is: {((9/5)*float(celsius))+32:.2f}")
        self.__continue()

    def start(self):
        while True:
            self.choice[int(self.selection())]()


if __name__ == "__main__":
    runonce = hw2()
    runonce.start()