#!/etc/python-3.9

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: [insert assignment name or number]

# Standard Library Imports
from pathlib import Path
import os, sys
from random import randint

# Third-party Library Imports

# Local Library Imports


class hw6:
    """
        Homework 6:
            1) Line Numbers
                -- Print the lines of a provided file and their line numbers
            2) Item Counter
                -- Count the lines of a provided file and print the number of lines
            3) Number Sum
                -- Sum the values of numbers printed on each line in a provided file
            4) Number Average
                -- Average the values of numbers printed on each line in a provided file
            5) Random Number Writer
                -- Write a user-specified amount of random integers to a file
            6) Golf Scores
                -- Golf Score Program designed to write a file of golfers and scores, and read it back
    """
    def __init__(self):
        self.__file_path = None
        self.__selection = {
            0: sys.exit,
            1: self.file_lines,
            2: self.name_count,
            3: self.num_sum,
            4: self.num_avg,
            5: self.num_wrt,
            6: self.golf_scores,
            9: self.__doc__
        }

    def start(self):
        print(f"{self.__doc__}")
        try:
            while True:
                choice = int(input("Please make a selection:"))
                if int(choice) in self.__selection.keys():
                    self.__selection[choice]()
                else:
                    print("I didn't understand that value, please try again.")
        except FileNotFoundError as err:
            self.__fnf(err)
        except IOError as err:
            print(f"Unable to access file.  Exiting with error {err}.")
        except ValueError as err:
            print(f"Invalid input type.  Exiting with error: {err}")
        except Exception:
            self.__canceled()
        finally:
            self.__clearFile()

    def __setFilePath(self):
        cancel = ["q", "Q"]
        while not self.__file_path:
            file_path = Path(input("Input File Location or Q to cancel: (eg: c:\\users\\My Documents\\file.txt): "))
            if file_path not in cancel and Path.is_file(file_path):
                self.__file_path = file_path
            elif file_path not in cancel:
                raise FileNotFoundError
            else:
                self.__clearFile()
                raise Exception

    def __clearFile(self):
        self.__file_path = None

    def __fnf(self, err):
        print(f"Error! {err}")

    def __canceled(self):
        print(f"Input Cancelled by User!")

    def file_lines(self):
        self.__setFilePath()
        with open(self.__file_path, 'r') as f:
            readlines = f.readlines()
            for index, lines in enumerate(readlines):
                print(f"{index + 1}: {lines}")

    def name_count(self):
        self.__setFilePath()
        with open(self.__file_path, 'r') as f:
            readlines = f.readlines()
            linecounter = 0
            for lines in readlines:
                if lines is not "":
                    linecounter += 1
            print(f"There are {linecounter} lines in this file!")

    def num_sum(self, flag=False):
        self.__setFilePath()
        line_sum = 0
        with open(self.__file_path, 'r') as f:
            readlines = f.readlines()
            for index, lines in readlines:
                line_sum += int(lines)
            if not flag:
                print(f"The total sum of {index + 1} lines is {line_sum} ")
            else:
                return line_sum, index + 1

    def num_avg(self):
        line_sum, index = self.num_sum(True)
        if index is not 0:
            print(f"The average of {index} numbers in {self.__file_path} is {line_sum / index}")
        else:
            print("There are no numbers to count here!")

    def num_wrt(self):
        self.__setFilePath()
        minVal = int(input("What is the lowest value to use?: "))
        maxVal = int(input("What is the highest value to use?: "))
        cntVal = int(input("How many values to generate?: "))
        while cntVal > 0 and maxVal > minVal:
            try:
                with open(self.__file_path, 'w+') as f:
                    for x in range(cntVal):
                        f.write(str(randint(minVal, maxVal)))
            except Exception as err:
                print(f"There was an error!: {err}")
            finally:
                return

    def golf_scores(self):
        self.__setFilePath()
        try:
            with open(self.__file_path, 'w+') as f:
                while True:
                    name = input(f"Input the golfer's name (or hit enter to continue): ")
                    if name:
                        score = input(f"Input {name}'s score: ")
                        f.write(f"{name}, {score}\n")
                    else:
                        break
            with open(self.__file_path, 'r') as f:
                for x in f.readlines():
                    print(f"{x}")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    runonce = hw6()
    runonce.start()