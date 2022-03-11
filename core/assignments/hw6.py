#!/etc/python-3.9

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: [insert assignment name or number]

# Standard Library Imports
from pathlib import Path
import os, sys

# Third-party Library Imports

# Local Library Imports


class hw6:
    """
        This is the __docs__ reference to the assignment
    """
    def __init__(self):
        self.__file_path = None
        self.__selection = {
            0: sys.exit,
            1: self.file_lines,
            2: self.name_count,
            3: self.num_sum,
            4: self.num_avg,
            9: self.__doc__
        }

    def start(self):
        try:
            while True:
                return
        except FileNotFoundError as err:
            self.__fnf(err)
        except IOError as err:
            print(f"Unable to access file.  Exiting with error {err}.")
        except ValueError as err:
            print(f"Typing error.  Exiting with error: {err}")
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


if __name__ == "__main__":
    runonce = hw6()
    runonce.start()