from Jokenpo.base import verificar_jogada


def pedra(computador: str) -> str:
    """Função chamada quando o jogador escolher pedra.
    Verifica a jogada do computador e retorna uma
    mensagem adequada.

    :param computador: Jogada do computador.
    :return: str: Mensagem.
    """
    mensagem = [
        'Eeeita! Jogamos iguais kkk.',
        'Computador venceu! Papel enrola pedra.',
        'Você venceu! Pedra esmaga tesoura.',
        'Você venceu! Pedra esmaga lagarto.',
        'Computador venceu! Spock vaporiza pedra.'
    ]
    return verificar_jogada(computador, mensagem)
