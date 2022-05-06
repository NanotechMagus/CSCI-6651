#!/etc/python-3.9

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: [insert assignment name or number]

# Standard Library Imports
from pathlib import Path

# Third-party Library Imports

# Local Library Imports
from encryptme import filecrypt


class ProjFunc:
    """
        This is the __docs__ reference to the assignment
    """
    def __init__(self, filepath: Path, crypt: filecrypt):
        self.__filepath = filepath
        self.__crypt = crypt
        self.__opts = {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: "",
        }


