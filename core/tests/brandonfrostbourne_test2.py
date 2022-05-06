#!/etc/python-3.9

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: [insert assignment name or number]

# Standard Library Imports
from pathlib import Path
import os

# Third-party Library Imports

# Local Library Imports


# TODO: Change class hw: to the correct homework name and change __name__ == "__main__".  Remove this todo when done
class hw:
    """
        Average Steps Taken Program

        A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories
        burned, heart rate, sleeping patterns, and so on. One common physical activity that most
        of these devices track is the number of steps you take each day.

        Download the file named steps.txt from Canvas. The steps.txt file contains:

        The number of steps a person has taken each day for a year. There are 365 lines in the
        file, and each line contains the number of steps taken during a day. (The first line is the
        number of steps taken on January 1st; the second line is the number of steps taken on
        January 2nd, and so forth.)

        Write a Python program that accomplishes the following tasks:

            1. Read the steps.txt file and calculate the average number of steps taken for each
        month. (The data is from a year that was not a leap year, so February has 28 days.)

            2. Store the calculated average data with each month’s name in a new file called "Avg
        Steps.txt" then close the files.

            3. Print the Average data in a nicely formatted table by month, then close the file.

            4. Add your name to the Avg Steps file.
    """
    def __init__(self):
        self.__fileLines = []
        self.__months = {
            "January": {
                "days": 31,
                "avg": 0.0,
                "steps": []
            },
            "February": {
                "days": 28,
                "avg": 0.0,
                "steps": []
            },
            "March": {
                "days": 31,
                "avg": 0.0,
                "steps": []
            },
            "April": {
                "days": 30,
                "avg": 0.0,
                "steps": []
            },
            "May": {
                "days": 31,
                "avg": 0.0,
                "steps": []
            },
            "June": {
                "days": 30,
                "avg": 0.0,
                "steps": []
            },
            "July": {
                "days": 31,
                "avg": 0.0,
                "steps": []
            },
            "August": {
                "days": 31,
                "avg": 0.0,
                "steps": []
            },
            "September": {
                "days": 30,
                "avg": 0.0,
                "steps": []
            },
            "October": {
                "days": 31,
                "avg": 0.0,
                "steps": []
            },
            "November": {
                "days": 30,
                "avg": 0.0,
                "steps": []
            },
            "December": {
                "days": 31,
                "avg": 0.0,
                "steps": []
            },
        }

    def ingest(self, loc: Path):
        if loc and Path.exists(loc):
            with open(loc, "r") as f:
                self.__fileLines = f.readlines()
        else:
            raise FileNotFoundError

    def stepcalc(self):
        for month in self.__months.keys():
            stepcount = 0
            for x in range(self.__months[month]["days"]):
                stepval = int(self.__fileLines.pop(0))
                self.__months[month]["steps"].append(stepval)
                stepcount += stepval
            self.__months[month]["avg"] = (stepcount / int(self.__months[month]["days"]))

    def file_out(self, outfile: Path):
        with open(outfile, "w") as f:
            f.write("Average Monthly Steps Taken:\n")
            tabular = ("\t\t", "\t\t\t")
            for months in self.__months:
                f.write(f"{months}:{tabular[1] if len(months) <= 6 else tabular[0]}{self.__months[months]['avg']: 0.2f}\n")
            f.write("\n\nThis assignment was brought to you by Brandon Frostbourne")

    def start(self):
        infile = Path(input("Please input the name of the file to ingest for steps calculation: (ex. steps.txt) "))
        outfile = Path(input("And now enter the name of the file to output to: (ex: Avg Steps.txt) "))
        try:
            self.ingest(infile)
            if not len(self.__fileLines) == 0:
                self.stepcalc()
            self.file_out(outfile)
        except FileNotFoundError as err:
            print(f"Cannot find file. {err}")
        return


# TODO: Change hw() to the correct class name.  Remove this todo when done
if __name__ == "__main__":
    runonce = hw()
    runonce.start()