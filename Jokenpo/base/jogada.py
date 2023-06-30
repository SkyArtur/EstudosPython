from Jokenpo.base import *


def jogada(usuario: str, computador: str) -> str:
    """Função que representa a jogada principal do jogo
    recebe a jogada de ambos os "players" e devolve o vencedor.

    :param usuario: "String" referente a escolha do jogador.
    :param computador: "String" referente a escolha do computador.
    :return: str: Mensagem.
    """
    exibir_jogadas = '''
    O jogador escolheu: {}
    O computador escolheu: {}
    '''.format(usuario, computador)
    print(exibir_jogadas)
    mensagem = None
    if usuario == ITENS[0]:
        mensagem = pedra(computador)
    elif usuario == ITENS[1]:
        mensagem = papel(computador)
    elif usuario == ITENS[2]:
        mensagem = tesoura(computador)
    elif usuario == ITENS[3]:
        mensagem = lagarto(computador)
    elif usuario == ITENS[4]:
        mensagem = spock(computador)
    return mensagem
