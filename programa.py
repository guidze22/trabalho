import random
from funcoes import *

 
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in posicoes:
        l = posicao[0]
        c = posicao[1]

        if l < 0 or l >= 10 or c < 0 or c >= 10:
            return False

        for tipo, navios in frota.items():
            for navio in navios:
                if posicao in navio:
                    return False

    return True
frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

navios = {
    "porta-aviões": [4, 1],
    "navio-tanque": [3, 2],
    "contratorpedeiro": [2, 3],
    "submarino": [1, 4]
}

for nome, dados in navios.items():
    tamanho = dados[0]
    quantidade = dados[1]

    for i in range(quantidade):
        valido = False
        while not valido:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if nome == "submarino":
                orientacao = "vertical"
            else:
                escolha = int(input("[1] Vertical [2] Horizontal >"))
                if escolha == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            posicoes = define_posicoes(
                linha, coluna, orientacao, tamanho
            )

            valido = posicao_valida(
                frota, linha, coluna, orientacao, tamanho
            )

            if valido:
                frota = preenche_frota(
                    frota, nome, linha, coluna, orientacao, tamanho
                )
            else:
                print("Esta posição não está válida!")
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogando = True
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto


jogadas = []
jogada=[]
jogando = True

while jogando == True :
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha = int(input("Informe a linha: "))

    while linha < 0 or linha > 9:
        print("Linha inválida!")
        linha = int(input("Informe a linha: "))

    coluna = int(input("Informe a coluna: "))

    while coluna < 0 or coluna > 9:
        print("Coluna inválida!")
        coluna = int(input("Informe a coluna: "))

    while [linha, coluna] in jogadas:
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")

        linha = int(input("Informe a linha: "))

        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Informe a linha: "))

        coluna = int(input("Informe a coluna: "))

        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Informe a coluna: "))

    jogadas.append([linha, coluna])

    faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False


    if jogando:
        linha2=random.randint(0,9)
        coluna2=random.randint(0,9)
        while [linha2,coluna2] in jogada:
            linha2=random.randint(0,9)
            coluna2=random.randint(0,9)
        jogada.append([linha2, coluna2])
        print(f"Seu oponente está atacando na linha {linha2} e coluna {coluna2}")
        faz_jogada(tabuleiro_jogador,linha2 , coluna2)
        if afundados(frota, tabuleiro_jogador) == 10:
            print("Xi! O oponente derrubou toda a sua frota =( ")
            jogando = False
