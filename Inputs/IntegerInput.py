class IntegerInput:
    @staticmethod
    def inpint(value) -> int:
        """Verifica a ocorrência de caractere inválido, quando o esperado
        é um numeral inteiro. Haje de maneira recursiva, até que receba
        um valor correto.
        """
        try:
            inp_int = int(input(value))
        except ValueError:
            print('Caractere inválido, apenas números inteiros são aceitos!')
            inp_int = IntegerInput.inpint('>? ')
        return inp_int

    @staticmethod
    def rinpint(value, minn: int, maxx: int) -> int:
        """Verifica a ocorrência de caractere inválido, quando o esperado
        é um numeral inteiro, através da função input_int(). Utiliza um laço
        while para verificar se o parâmetro está dentro no range pré-determinado."""
        inp_int = IntegerInput.inpint(value)
        while inp_int < minn or inp_int > maxx:
            print('Opção errada!')
            inp_int = IntegerInput.inpint('>? ')
        return inp_int
