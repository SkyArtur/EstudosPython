"""
Validador Simple de CPF
"""
import re


class ValidadorCPF:
    mensagem = 'ErroValidador: Falha na validação ou cpf inválido.'

    def __init__(self, numero: str):
        try:
            self.__cpf = re.search('^([0-9]{3})\\.?([0-9]{3})\\.?([0-9]{3})-?([0-9]{2})$', numero)
        except TypeError:
            pass

    def __str__(self):
        mascara = self.__validacao_primaria()
        if mascara:
            return f'{mascara[0]}.{mascara[1]}.{mascara[2]}-{mascara[3]}'
        else:
            return self.mensagem

    def __validacao_primaria(self):
        try:
            if self.__cpf is not None:
                return self.__cpf.groups()
        except AttributeError:
            return None

    def __checar_digito(self):
        checagem, digito_validado = True, str()
        while checagem:
            checagem, digito = True if len(digito_validado) < 1 else False, 0
            for i, j in enumerate(range(10 if checagem else 11, 1, -1)):
                digito += int(str().join(self.__validacao_primaria())[i]) * j
            digito = 11 - (digito % 11)
            digito = 0 if digito > 9 else digito
            digito_validado += str(digito)
        return digito_validado

    def validar(self):
        try:
            return self.__checar_digito() == str().join(self.__validacao_primaria())[-2:]
        except (AttributeError, TypeError):
            return self.mensagem
