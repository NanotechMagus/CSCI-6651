#!/etc/python-3.9

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: [insert assignment name or number]

# Standard Library Imports


# Third-party Library Imports
import logging

from cryptography.fernet import Fernet
from pathlib import Path

# Local Library Imports


class filecrypt:
    """
        Encrypts and decrypts messages with a generated or loaded key.
    """
    def __init__(self, keyloc=None):
        self.__DEFAULT_KEY_LOC = Path("crypto.token")
        self.__cryptKey = None
        self.__keyloc = None
        logging.info(f"Initializing cryptographic token.")
        self.__initialize(keyloc)

    def __generate_cryptkey(self):
        return Fernet.generate_key()

    def cryptkey_display(self):
        return self.__cryptKey

    def encrypt(self, message):
        encKey = Fernet(self.__cryptKey)
        return encKey.encrypt(message.encode())

    def decrypt(self, encMessage):
        decKey = Fernet(self.__cryptKey)
        return decKey.decrypt(encMessage).decode()

    def __initialize(self, keyloc: Path):
        # If no token is supplied, set a filename for the new token location
        if keyloc and Path.exists(keyloc):
            self.__keyloc = keyloc
            keyflag = True
        elif Path.exists(self.__DEFAULT_KEY_LOC):
            self.__keyloc = self.__DEFAULT_KEY_LOC
            keyflag = True
        else:
            self.__keyloc = self.__DEFAULT_KEY_LOC
            keyflag = False

        # Initialize the token -- if the token exists, load it otherwise generate a new one
        try:
            if not keyflag:
                logging.info(f"No token exists at {self.__keyloc}.")
                self.new_key(self.__keyloc, True)
            else:
                logging.info("Token found, attempting to load key.")
                self.load_key(self.__keyloc)
            logging.info(f"Using key: {self.__cryptKey.decode()}")
        except ValueError or FileNotFoundError:
            self.__initialize(self.__DEFAULT_KEY_LOC)

    def new_key(self, cryptloc=None, save=False):
        logging.info(f"Generating new key")
        self.__cryptKey = self.__generate_cryptkey()
        logging.info(f"New key generated: {self.__cryptKey.decode()}")
        if save:
            logging.info(f"Saving key to {Path.absolute(cryptloc)}")
            self.__write_key(cryptloc, self.__cryptKey)

    def __write_key(self, crypt_loc: Path, key: bytes):
        logging.info(f"Writing key {key.decode()} to {crypt_loc}.")
        with open(crypt_loc, "w") as f:
            f.write(key.decode())

    def __read_key(self, cryptloc: Path):
        logging.info(f"Reading key from {cryptloc}.")
        with open(cryptloc, "r") as f:
            return f.readline().encode()

    def load_key(self, keypath: Path):
        if Path.exists(keypath):
            logging.info(f"File found, attempting to access new key at {Path.absolute(keypath)}.")
            keyline = self.__read_key(keypath)
            if keyline:
                logging.info(f"Key found: {keyline.decode()}. Loading into registry.")
                self.__cryptKey = keyline
            else:
                logging.info("No key found.")
                raise ValueError
        else:
            logging.info("No file found, check the path and try again")
            raise FileNotFoundError

