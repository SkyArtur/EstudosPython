from Jokenpo.base import *


def verificar_jogada(computador: str, mensagem: list) -> str:
    """Testa a condicional para definir vencedor.

    :param computador: Jogada do computador.
    :param mensagem: Lista de mensagens.
    :return: str: Mensagem.
    """
    if computador == ITENS[0]:  # Computador escolheu Pedra
        mensagem = mensagem[0]
    elif computador == ITENS[1]:  # Computador escolheu Papel
        mensagem = mensagem[1]
    elif computador == ITENS[2]:  # Computador escolheu Tesoura
        mensagem = mensagem[2]
    elif computador == ITENS[3]:  # Computador escolheu Lagarto
        mensagem = mensagem[3]
    elif computador == ITENS[4]:  # Computador escolheu Spock
        mensagem = mensagem[4]
    return mensagem
