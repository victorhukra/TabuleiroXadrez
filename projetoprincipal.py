#importa os módulos com as regras de movimento de cada peça

import peao
import cavalo
import torre
import bispo
import rainha
import rei

#função que exibe o tabuleiro 

def matriz_tabuleiro(tabuleiro):
    print("\n  1  2  3  4  5  6  7  8")  #colunas representas visualmente atráves de um print
    for i in range(8):      # for percorre as linhas                                      
        linha = str(i + 1) + " "  #usado para numerar cada linha a partir de 1  (+ " " é para dar espaçamento a cada caractere)
        for j in range(8):     #for percorre as colunas
            linha += tabuleiro[i][j] + " "      #adiciona a peça ou -- na linha
        print(linha)                            #imprime a linha 

#tabuleiro

tabuleiro = [
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["PB", "PB", "PB", "PB", "PB", "PB", "PB", "PB"],
    ["TB", "CB", "BB", "KB", "QB", "BB", "CB", "TB"]
]

#entradas e condicionais

while True:
    matriz_tabuleiro(tabuleiro)                                     #chama a função e exibe o tabuleiro 
    peca = input("\nQual peça deseja mover?: ").upper()             #nome da peça
    origem_linha = int(input("Linha de origem (1-8): ")) - 1        # o -1 serve para a conversão do índice
    origem_coluna = int(input("Coluna de origem (1-8): ")) - 1
    destino_linha = int(input("Linha de destino (1-8): ")) - 1
    destino_coluna = int(input("Coluna de destino (1-8): ")) - 1

    if peca == "PB":
        if peao.movimento_peao(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):      #chama a função e faz a verificação
            tabuleiro[destino_linha][destino_coluna] = "PB"     #atualiza e move o peão caso o movimento seja válido
            tabuleiro[origem_linha][origem_coluna] = "--"       #atualiza a linha e a coluna de origem para vazia
        else:
            print("\nMovimento inválido para o Peão!")          #movimento inválido

    elif peca == "TB":      #torre branca
        if torre.movimento_torre(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):        #chama a função e faz a verificação       
            tabuleiro[destino_linha][destino_coluna] = "TB"       #atualiza e move a torre caso o movimento seja válido
            tabuleiro[origem_linha][origem_coluna] = "--"        #atualiza a linha e a coluna de origem para vazia   
        else:
            print("\nMovimento inválido para a Torre!")         #movimento inválido

    elif peca == "CB":      #cavalo branco
        if cavalo.movimento_cavalo(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):      #chama a função e faz a verificação      
            tabuleiro[destino_linha][destino_coluna] = "CB"     #atualiza e move o cavalo caso o movimento seja válido
            tabuleiro[origem_linha][origem_coluna] = "--"       #atualiza a linha e a coluna de origem para vazia   
        else:
            print("\nMovimento inválido para o Cavalo!")

    elif peca == "BB":      #bispo branco
        if bispo.movimento_bispo(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):        #chama a função e faz a verificação        
            tabuleiro[destino_linha][destino_coluna] = 'BB'     #atualiza e move o bispo caso o movimento seja válido
            tabuleiro[origem_linha][origem_coluna] = '--'       #atualiza a linha e a coluna de origem para vazia   
        else:
            print('\nMovimento inválido para o Bispo!')         #movimento inválido

    elif peca == "KB":      #rei branco
        if rei.movimento_rei(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):        #chama a função e faz a verificação        
            tabuleiro[destino_linha][destino_coluna] = 'KB'     #atualiza e move o rei caso o movimento seja válido
            tabuleiro[origem_linha][origem_coluna] = '--'       #atualiza a linha e a coluna de origem para vazia   
        else:
            print('\nMovimento inválido para o Rei!')           #movimento inválido

    elif peca == "QB":       #rainha branca
        if rainha.movimento_rainha(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):      #chama a função e faz a verificação     
            tabuleiro[destino_linha][destino_coluna] = 'QB'     #atualiza e move a rainha caso o movimento seja válido
            tabuleiro[origem_linha][origem_coluna] = '--'       #atualiza a linha e a coluna de origem para vazia
        else:
            print('\nMovimento inválido para a Rainha!')        #movimento inválido

    else:
        print("\nPeça não encontrada")      #se a peça não for reconhecida printa que a peça não foi encontrada
