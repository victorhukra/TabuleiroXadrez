## Verifica se o movimento do Rei é válido.
## O Rei pode mover uma casa em qualquer direção.

def movimento_rei(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):
    
    if tabuleiro[origem_linha][origem_coluna] != "KB":      #verifica se a peça escolhida é o rei branco
        return False                                        #se não for, retorna falso


    #o delta serve para medir o número de "casas" que o rei está tentando andar

    delta_linha = abs(destino_linha - origem_linha)         #calcula a diferença de linhas entre origem e destino
    delta_coluna = abs(destino_coluna - origem_coluna)      #calcula a diferença de colunas entre origem e destino

    if delta_linha <= 1 and delta_coluna <= 1:              #verifica se o movimento é de no máximo 1 casa na linha e na coluna
        destino = tabuleiro[destino_linha][destino_coluna]  #armazena o valor da casa de destino 

        return destino == "--" or destino[1] != "B"          #retorna true se a casa estiver vazia ou se houver alguma peça diferente de branca(quando tiver)
    
    return False                                             #se alguma das condições não for atendida, retorna falso (movimento inválido)
