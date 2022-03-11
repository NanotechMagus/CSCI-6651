#!/etc/python-3.9

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


def load_assignments(exercises):
    try:
        ex = exercises.get_assignments()
        loaded = len(exercises.assignments)
    except FileNotFoundError:
        print(f"Folder structure is missing.  Please verify the location of the assignments folder \n"
              f"Example: ../homework-csci-6651/core/assignments/[assignments.py]")
        loaded, ex = -1, None
    except NotImplementedError:
        print(f"No assignments found in assignments folder.  Continuing...")
        loaded, ex = 0, None
    except Exception as err:
        print(f"Error loading Assignments: {err}")
        loaded, ex = -1, None
    finally:
        return loaded, ex


def main():
    loaded, exercises = load_assignments(core(Path.cwd()))

    if exercises:
        while(True):
            cls()
            print(f"Welcome to Brandon Frostbourne's Homework Program"
                  f"\n\n This program is designed to encapsulate every homework assignment for CSCI-6651 at the \n"
                  f"University of New Haven -- taught by George Pillar III.\n\n")
            print(f"There are currently {loaded} assignments loaded.  Please make a selection below:\n")
            print(f"\n\n"
                  f"1) Reload Assignments. \n"
                  f"2) Print Information about the Author.")

            for keys, values in exercises.assignments:
                print(f"{keys + 3}) Assignment: {values}")
    return 0


if __name__ == "__main__":
    main()
