from random import randint
from Inputs import IntegerInput
from Jokenpo.base import jogada, ITENS

MENU_JOGADA = '''Faça sua Jogada:
    [0]: {};
    [1]: {};
    [2]: {};
    [3]: {}:
    [4]: {};
~$ '''.format(ITENS[0], ITENS[1], ITENS[2], ITENS[3], ITENS[4])

MENU_FINAL = '''
    [0]: Continuar;
    [1]: Sair;
~$ '''


def executar_programa() -> None:
    """Função que executa o programa.

    :return: None.
    """
    while True:
        computador = randint(0, 4)
        usuario = IntegerInput.rinpint(value=MENU_JOGADA, minn=0, maxx=4)
        _jogada = jogada(ITENS[usuario], ITENS[computador])
        print(_jogada)
        if IntegerInput.rinpint(value=MENU_FINAL, minn=0, maxx=1):
            break
