from Jokenpo.base import verificar_jogada


def spock(computador: str) -> str:
    """Função chamada quando o jogador escolher spock.
    Verifica a jogada do computador e retorna uma
    mensagem adequada.

    :param computador: Jogada do computador.
    :return: str: Mensagem.
    """
    mensagem = [
        'Você venceu! Spock vaporiza a pedra.',
        'Computador venceu! Papel refuta Spock.',
        'Você venceu! Spock amassa tesoura.',
        'Computador venceu! Lagarto envenena Spock.',
        'Cê leu meus pensamentos?!? Empate.'
    ]
    return verificar_jogada(computador, mensagem)
