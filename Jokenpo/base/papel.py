from Jokenpo.base import verificar_jogada


def papel(computador: str) -> str:
    """Função chamada quando o jogador escolher papel.
    Verifica a jogada do computador e retorna uma
    mensagem adequada.

    :param computador: Jogada do computador.
    :return: str: Mensagem.
    """
    mensagem = [
        'Você venceu! Papel enrola pedra.',
        'Deu zebra! Empatou.',
        'Computador venceu! Tesoura corta papel.',
        'Computador venceu! Lagarto come papel.',
        'Você venceu! Papel refuta Spock.'
    ]
    return verificar_jogada(computador, mensagem)
