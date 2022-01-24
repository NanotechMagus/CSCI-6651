#!/etc/python

# Standard Library Imports
from pathlib import Path
import os
from importlib import import_module

# Third-party Library Imports

# Local Library Imports


class core:
    def __init__(self, incpath: Path):
        self.__path = incpath if not None else Path.cwd()
        self.assignments = {}

    def get_assignments(self):
        # TODO: test if path returns current level of directory or top level
        # TODO: We need to go into the assignments directory -- syntax with a windows filepath is:
        #       filelist = os.listdir(self.path / "assignments") or "core/assignments" if from top level

        # Filepath validation
        if os.path.exists(self.__path) and os.path.split(self.__path)[1] == "assignments":
            filelist = os.listdir(self.__path)
        elif os.path.exists(self.__path / "assignments"):
            filelist = os.listdir(self.__path / "assignments")
        else:
            # TODO: log error
            raise FileNotFoundError

        # Filelist verification -- if there are no files from the scrape, raise an exception, but don't exit
        if len(filelist) <= 0:
            raise NotImplementedError

        for f in filelist:
            # For each file in assignments, add the file name and object as a key:value pair via __create_obj()
            exercisepath = os.path.splitext(f)[0]

            # Ignore init.py
            if exercisepath is not "init":
                self.__create_obj(exercisepath)

    def __create_obj(self, objname):
        # Create a method to import the object path, create a key/value pair with the exercise name and object
        cog = "assignments." + objname
        try:
            self.assignments[objname] = import_module(cog)
        except Exception as err:
            print(f"Cannot import {objname}: {err}")
