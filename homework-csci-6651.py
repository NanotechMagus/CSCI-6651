#!/etc/python

'''
    This code was authored by Brandon Frostbourne
    Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
    This program incorporates as many assignments as possible into a single python program by adding each assignment
    as a standalone class.
'''

# Standard Library Imports
import sys
from subprocess import call
from os import name
from pathlib import Path

# Third-party Library Imports

# Local Library Imports
from core.core import core


def cls():
    _ = call('clear' if name == 'posix' else 'cls')


def main():
    try:
        exercises = core(Path.cwd())
    except Exception as err:
        print(f"Error loading Assignments: {err}")
        sys.exit()

    loaded = len(exercises.assignments)

    while(True):
        cls()
        print(f"Welcome to Brandon Frostbourne's Homework Program"
              f"\n\n This program is designed to encapsulate every homework assignment for CSCI-6651 at the \n"
              f"University of New Haven -- taught by George Pillar III.\n\n")
        print(f"There are currently {loaded} assignments loaded.  Please make a selection below:\n")

    return


if __name__ == "__main__":
    main()
