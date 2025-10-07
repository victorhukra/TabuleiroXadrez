#função que recebe o tabuleiro, a posição de origem [i][j] e a posição para onde se destina

def movimento_peao(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):

    if tabuleiro[origem_linha][origem_coluna] != "PB":  # verifica se a peça que foi escolhida pelo usuário é o peão
        return False

                                                
    #movimento de 1 casa                               #obs: coluna continua a mesma (o peão só anda pra frente)                         (linha de origem - 1)                  
    if destino_linha == origem_linha - 1 and destino_coluna == origem_coluna:  #se a linha de destino for uma a menos que a linha de origem, anda uma casa 
        if tabuleiro[destino_linha][destino_coluna] == "--":  # se a casa estiver preenchida com (--), o movimento é válido
            return True  # ou seja, se está vazia retorna true  
    #                                                                                                                              
    #condicional para primeira jogada (movimento de até 2 casas)                                  #se a linha de origem for a 7 pode andar duas casas
    if origem_linha == 7 - 1 and destino_linha == origem_linha - 2 and destino_coluna == origem_coluna:     #se a linha de destino for igual a linha de origem - 2
        if tabuleiro[origem_linha - 1][origem_coluna] == "--" and tabuleiro[origem_linha - 2][origem_coluna] == "--":   #e se a casa estiver vazia o movivmento é válido
            return True     #por tanto retorna true

    return False        #se alguma dessas condicionais não forem atendidas o movimento é inválido e retorna falso
