from random import shuffle, choice
from getpass import getuser


class PasswordGenerator:
    LETTER = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i',
              'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'x', 'z', 'k', 'y', 'w']
    NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SYMBOL = ['@', '#', '$', '%', '&', '!', '?']
    CHARS = NUMBER + SYMBOL + LETTER + [i.upper() for i in LETTER]

    def __init__(self):
        self.__password = None

    @property
    def passgen(self):
        value = self.__password
        self.__password = str()
        for char in range(value):
            shuffle(self.CHARS)
            self.__password += str(choice(self.CHARS)[0])
        self.__password = f"pass|{self.__password}=={getuser()}"
        return self.__password

    @passgen.setter
    def passgen(self, value):
        self.__password = value
