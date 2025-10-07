def movimento_torre (tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):
    #verifica se é a torre que está sendo chamada 
    if tabuleiro[origem_linha][origem_coluna] != "TB":
        return False
    
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




