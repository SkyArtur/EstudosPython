import random
import re


class CPF:
    def __init__(self, number=None):
        self.__number: str = number

    def __check_digit(self, second_digit: int | bool) -> str:
        digit_validator = 0
        while 0 > second_digit or second_digit > 1:
            raise Exception('ErrorSecondDigitInvalid: second_digit: int | bool (0, 1 | False, True);')
        for i, j in enumerate(range(10 if not second_digit else 11, 1, -1)):
            digit_validator += int(self.__number[i]) * j
        digit_validator = 11 - (digit_validator % 11)
        return str(0 if digit_validator > 9 else digit_validator)

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, value: str):
        self.__number = value

    @property
    def mask(self) -> str:
        mask = re.search('^([0-9]{3})\\.?([0-9]{3})\\.?([0-9]{3})-?([0-9]{2})$', self.number).groups()
        return f'{mask[0]}.{mask[1]}.{mask[2]}-{mask[3]}'

    def generate(self) -> str | bool:
        self.__number = f'{random.randint(10 ** 6, 10 ** 9 - 1):0>9}'
        self.__number += self.__check_digit(0)
        self.__number += self.__check_digit(1)
        if self.validate():
            return self.__number

    def validate(self) -> str | bool:
        try:
            if re.search('^[0-9]{3}\\.?[0-9]{3}\\.?[0-9]{3}-?[0-9]{2}$', self.__number) is None:
                return False
            return self.__number[-2:] == self.__check_digit(False) + self.__check_digit(True)
        except TypeError:
            return False
