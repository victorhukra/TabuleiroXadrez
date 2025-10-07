def movimento_rainha (tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):
    if tabuleiro[origem_linha][origem_coluna] != "QB": #verifica se é a rainha que está sendo chamada 
        return False
#---------------------------------CRUZ DA RAINHA--------------------------------------------------------------------------
    if tabuleiro [destino_linha][destino_coluna] == "--": #confirma que o destino está livre
        if destino_linha == origem_linha or destino_coluna == origem_coluna:   # limita formato de cruz
            if destino_linha == origem_linha:    #limita linha
                if destino_coluna == origem_coluna + 1:
                    return True
                if destino_coluna == origem_coluna - 1:
                    return True
                if origem_coluna < destino_coluna:    # origem é menor que destino (colunas)   -->
                   for i in range (origem_coluna + 1,destino_coluna - 1,+ 1):    # varre colunas na mesma linha
                       if tabuleiro[destino_linha][i] != "--":  
                           return False
                       else:
                           return True
                if origem_coluna > destino_coluna: #destino é menor que origem              <--
                    for i in range (origem_coluna - 1,destino_coluna + 1,- 1):
                        if tabuleiro[destino_linha][i] != "--":
                            return False
                        else:
                            return True                   
            if destino_coluna == origem_coluna: #limita coluna
                if destino_linha == origem_linha + 1:
                    return True
                if destino_linha == origem_linha - 1:
                    return True
                if origem_linha < destino_linha: #origem menor que destino (linhas)      (abaixo)
                    for i in range (origem_linha + 1,destino_linha,+ 1):
                        if tabuleiro[i][destino_coluna] != "--":
                            return False
                        else:
                            return True
                if origem_linha > destino_linha: #destino menor que origem   acima
                    for i in range (origem_linha - 1,destino_linha,- 1):
                        if tabuleiro[i][destino_coluna] != "--":
                            return False
                        else:
                            return True
# --------------------------------DIAGONAIS DA RAINHA------------------------------------------------------------------------
        if origem_linha > destino_linha and origem_coluna > destino_coluna: # diagonal superior esquerda 
            if destino_linha == origem_linha - 1 and destino_coluna == origem_coluna - 1:
                return True
            for i in range (origem_linha - 1,destino_linha,-1): #subtrai 1 da linha por iteração
                for k in range (origem_coluna - 1,destino_coluna,-1): #subtrai 1 da coluna por iteração
                    if tabuleiro[i][k] != "--":
                        return False
                    else:
                        return True     
        if origem_linha > destino_linha and origem_coluna < destino_coluna: # diagonal superior direita
            if destino_linha == origem_linha - 1 and destino_coluna == origem_coluna + 1:
                return True
            for i in range (origem_linha - 1,destino_linha,-1):
                for k in range (origem_coluna + 1,destino_coluna,+1):
                    if tabuleiro[i][k] != "--":
                        return False
                    else:
                        return True
        if origem_linha < destino_linha and origem_coluna > destino_coluna: # diagonal inferior esquerda
            if destino_linha == origem_linha + 1 and destino_coluna == origem_coluna - 1:
                return True
            for i in range (origem_linha + 1,destino_linha,+1): 
                for k in range (origem_coluna - 1,destino_coluna,-1):
                    if tabuleiro[i][k] != "--":
                        return False
                    else:
                        return True
        if origem_linha < destino_linha and origem_coluna < destino_coluna: # diagonal inferior direita
            if destino_linha == origem_linha + 1 and destino_coluna == origem_coluna + 1:
                return True
            for i in range (origem_linha + 1,destino_linha,+1): #subtrai 1 da linha por iteração
                for k in range (origem_coluna + 1,destino_coluna,+1): #subtrai 1 da coluna por iteração
                    if tabuleiro[i][k] != "--":
                        return False
                    else:
                        return True
# ------------------------------------FIM DO CÓDIGO-----------------------------------------------------------------------------
        

