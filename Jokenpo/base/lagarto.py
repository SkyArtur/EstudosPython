from Jokenpo.base import verificar_jogada


def lagarto(computador: str) -> str:
    """Função chamada quando o jogador escolher lagarto.
    Verifica a jogada do computador e retorna uma
    mensagem adequada.

    :param computador: Jogada do computador.
    :return: str: Mensagem.
    """
    mensagem = [
        'Computador venceu! Pedra esmaga lagarto.',
        'Você venceu! Lagarto come papel.',
        'Computador venceu! Tesoura decapita lagarto.',
        'Que coincidência! Empate.',
        'Você venceu! Lagarto envenena Spock.'
    ]
    return verificar_jogada(computador, mensagem)
