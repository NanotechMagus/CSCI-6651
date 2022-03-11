#!/etc/python-3.9

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: [insert assignment name or number]

# Standard Library Imports
from random import randint

# Third-party Library Imports

# Local Library Imports


class hw5:
    """
        1. odd/even Counter
            A program that generates 100 random numbers and keeps a count of how many of those random numbers
            are even and how many of them are odd.
        2. prime numbers
            A function that tests whether an inputted number is a prime
        3. prime number  List
            Print all of the prime numbers between 1 and an inputted number
        4. Future  Value
            Suppose  you  have  a  certain  amount  of  money  in  a  savings  account  that  earns  compound  monthly  interest,  and  you
            want to calculate the amount that you will have after a specific number of months. The formula is as follows:
            F = P x (1 + i)t

            The terms in the formula are:
            • F is  the  future  value  of  the  account  after  the  specified  time  period.
            • P is  the  present  value  of  the  account.
            • i is  the  monthly  interest  rate.
            • t is  the  number  of  months.

            Write a program that prompts the user to enter the account’s present value, monthly interest rate, and the number of
            months that the money will be left in the account. The program should pass these values to a function that returns the
            future value of the account, after the specified number of months. The program should display the account’s future
            value.
        5. Random number Guessing Game
            Write a program that generates a random number in the range of 1 through 100 and asks the user to guess what the
            number is. If the user’s guess is higher than the random number, the program should display “Too high, try again.” If
            the user’s guess is lower than the random number, the program should display “Too low, try again.” If the user guesses
            the number, the application should congratulate the user and then generate a new random number so the game can
            start over.
            Optional Enhancement: Enhance the game so it keeps count of the number of guesses that the user makes. When the
            user correctly guesses the random number, the program should display the number of guesses.
    """
    def __init__(self):
        return

    def odd_even(self):
        numcount = int(input("Input the number of random numbers generated (must be positive, non-zero): "))
        llimit = int(input("What is the lower limit?: "))
        hlimit = int(input("What is the upper limit?: "))
        evencount = 0
        while llimit > 0:
            for x in range(numcount):
                randcount = randint(llimit, hlimit)
                print(f"{randcount} is ", end="")
                if self.__isEven(randcount):
                    print("even!")
                    evencount += 1
                else:
                    print("odd!")
            print(f"In the data set of {numcount} values, {evencount} were even, and {numcount - evencount} were odd.")
            return

    def prime(self):
        testval = int(input("Input a whole number you want to test if it's a prime: "))
        is_prime = self.__isprime(testval)
        if is_prime == 1:
            print(f"{testval} is a prime number!")
        else:
            print(f"{testval} is not a prime number!")

    def print_primes(self):
        count = 0
        testrange = int(input("What is the highest value you want to iterate over?: "))
        for x in range(2, testrange):
            if self.__isprime(x) == 1:
                print(x)
                count += 1
        print(f"{count} number of prime numbers were counted from 1 to {testrange}")

    def interest(self):
        futures = {}
        print(f"Please input the following: ")
        futures["present"] = float(input("What is the present value of the account?: "))
        futures["interest"] = (float(input("What is the interest rate?: %")) / 100)


    def __isprime(self, val: int):
        if val >= 3 and val != 1:
            for x in range(2, val):
                if val % x == 0:
                    return 0
            return 1
        elif val == 1:
            return 0
        else:
            return 1

    def __isEven(self, val: int):
        return val % 2

    def __futures(self, futures: dict):
        return futures["present"] * (1 + futures["interest"]) * futures["time"]

    def start(self):
        return


if __name__ == "__main__":
    runonce = hw5()
    runonce.start()
