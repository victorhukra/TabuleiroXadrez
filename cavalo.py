def movimento_cavalo(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):
    # Todas as possíveis posições em L
    movimentos_possiveis = [
        (origem_linha - 2, origem_coluna - 1),
        (origem_linha - 2, origem_coluna + 1),
        (origem_linha - 1, origem_coluna - 2),
        (origem_linha - 1, origem_coluna + 2),
        (origem_linha + 1, origem_coluna - 2),
        (origem_linha + 1, origem_coluna + 2),
        (origem_linha + 2, origem_coluna - 1),
        (origem_linha + 2, origem_coluna + 1),
    ]

    # Verificar se destino está dentro do tabuleiro
    if 0 <= destino_linha < 8 and 0 <= destino_coluna < 8:
        # Verificar se o movimento está entre os possíveis
        if (destino_linha, destino_coluna) in movimentos_possiveis:
            peca_destino = tabuleiro[destino_linha][destino_coluna]

            # Verificar se tem uma peça amiga (por exemplo, terminando com "B" para peças brancas)
            if len(peca_destino) == 2 and peca_destino[1] == "B":
                return False  # Não pode mover para cima de outra peça branca
            else:
                return True  # Casa vazia

    return False  # Movimento inválido
