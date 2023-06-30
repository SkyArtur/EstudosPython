from Jokenpo.base import verificar_jogada


def tesoura(computador: str) -> str:
    """Função chamada quando o jogador escolher tesoura.
    Verifica a jogada do computador e retorna uma
    mensagem adequada.

    :param computador: Jogada do computador.
    :return: str: Mensagem.
    """
    mensagem = [
        'Computador venceu! Pedra esmaga tesoura.',
        'Você venceu! Tesoura corta papel.',
        'Poxa! Empatou.',
        'Você venceu! Tesoura decapita lagarto.',
        'Computador venceu! Spock esmaga tesoura.'
    ]
    return verificar_jogada(computador, mensagem)
