def movimento_bispo(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):
    
    if tabuleiro[origem_linha][origem_coluna] != "BB":
        return False

    delta_linha = abs(destino_linha - origem_linha)
    delta_coluna = abs(destino_coluna - origem_coluna)

    if delta_linha == delta_coluna:
        passo_linha = 1 if destino_linha > origem_linha else -1
        passo_coluna = 1 if destino_coluna > origem_coluna else -1

        linha = origem_linha + passo_linha
        coluna = origem_coluna + passo_coluna

        while linha != destino_linha and coluna != destino_coluna:
            if tabuleiro[linha][coluna] != "--":
                return False
            linha += passo_linha
            coluna += passo_coluna

        destino = tabuleiro[destino_linha][destino_coluna]
        return destino == "--" or destino[1] != "B"

    return False
