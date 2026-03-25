import random
import time

TAMANHO_LINHAS = 10
TAMANHO_COLUNAS = 10

VIDA_VILAO = 1

#campo 10x10
campo = ([
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', 'b', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', 'b', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', 'b', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', 'b', '-', '-', '-', '-', '-', '-', '-']
])

def iniciar_campo(matriz): #heroi, vilao, e bonus recebem posições aleatórias (NÃO IGUAIS)
    linha_heroi = random.randint(0, 9)
    coluna_heroi = random.randint(0, 9)
    linha_vilao = random.randint(0, 9)
    coluna_vilao = random.randint(0, 9)
    linha_bonus = random.randint(0, 9)
    coluna_bonus = random.randint(0, 9)

    heroi_pos = (linha_heroi, coluna_heroi)
    vilao_pos = (linha_vilao, coluna_vilao)
    bonus_pos = (linha_bonus, coluna_bonus)

    while vilao_pos == heroi_pos:
        linha_vilao = random.randint(0, 9)
        coluna_vilao = random.randint(0, 9)
        vilao_pos = (linha_vilao, coluna_vilao)

    while bonus_pos == heroi_pos or bonus_pos == vilao_pos:
        linha_bonus = random.randint(0, 9)
        coluna_bonus = random.randint(0, 9)
        bonus_pos = (linha_bonus, coluna_bonus)

        linha_bonus = random.randint(0, 9)
        coluna_bonus = random.randint(0, 9)
    

    matriz[linha_heroi][coluna_heroi] = 'h'
    matriz[linha_vilao][coluna_vilao] = 'v'
    matriz[linha_bonus][coluna_bonus] = 'b'

def localizar_heroi(matriz): #Retorna (linha e coluna) de localização heroi
    for i in range(TAMANHO_LINHAS):
        for j in range(TAMANHO_COLUNAS):
            if(matriz[i][j] == 'h'):
                print(f"Heroi Linha:{i}")
                print(f"Heroi Coluna:{j}")
                return i, j

def localizar_vilao(matriz): #Retorna (linha e coluna) de localização vilão
    for i in range(TAMANHO_LINHAS):
        for j in range(TAMANHO_COLUNAS):
            if(matriz[i][j] == 'v'):
                print(f"Vilão Linha:{i}")
                print(f"Vilão Coluna:{j}")
                return i, j
            
def localizar_bonus(matriz): #Retorna (linha e coluna) de localização bonus
    for i in range(TAMANHO_LINHAS):
        for j in range(TAMANHO_COLUNAS):
            if(matriz[i][j] == 'b'):
                print(f"Bonus Linha:{i}")
                print(f"Bonus Coluna:{j}")
                return i, j
            
def mover_heroi(matriz, i, j): #Move o heroi para nova posição
    i_h, j_h = localizar_heroi(matriz)
    matriz[i_h][j_h] = '-'
    matriz[i+1][j+1] = 'h'

def mover_vilao(matriz, i, j): #Move o heroi para nova posição
    i_h, j_h = localizar_heroi(matriz)
    matriz[i_h][j_h] = '-'
    matriz[i][j] = 'h'

def teleportar_vilao(matriz):
    """Teleporta vilão para nova posição vazia"""
    while True:
        i_v = random.randint(0, 9)
        j_v = random.randint(0, 9)
        # Só teleporta para posição vazia ('-')
        if matriz[i_v][j_v] == '-':
            # Limpa posição anterior do vilão
            for i in range(TAMANHO_LINHAS):
                for j in range(TAMANHO_COLUNAS):
                    if matriz[i][j] == 'v':
                        matriz[i][j] = '-'
            # Coloca vilão na nova posição
            matriz[i_v][j_v] = 'v'
            break

def teleportar_bonus(matriz):
    """Teleporta bonus para nova posição vazia"""
    while True:
        i_b = random.randint(0, 9)
        j_b = random.randint(0, 9)
        # Só teleporta para posição vazia ('-')
        if matriz[i_b][j_b] == '-':
            # Limpa posição anterior do bonus
            for i in range(TAMANHO_LINHAS):
                for j in range(TAMANHO_COLUNAS):
                    if matriz[i][j] == 'b':
                        matriz[i][j] = '-'
            # Coloca bonus na nova posição
            matriz[i_b][j_b] = 'b'
            break

def decidir(lista_condicoes, lista_prioridades): #Analisa as condiçoes e prioridades e retorna a posicao (ação)
    maior_prioridade = 0
    posicao = 0

    for i in range(len(lista_condicoes)):
        if(lista_condicoes[i] == True):
            if(lista_prioridades[i] > maior_prioridade):
                maior_prioridade = lista_prioridades[i]
                posicao = i

    return posicao

def mostrar_matriz(matriz):
    for i in range(TAMANHO_LINHAS):
        print() #Quebra de linha para cada linha da matriz
        for j in range(TAMANHO_COLUNAS):
            print(matriz[i][j], end=" ")
    print()     #Quebra de linha para o final da matriz

def rodar_jogo(campo):
    iniciar_campo(campo)
    heroi_movimentou = 1
    bonus = 0
    ataque = 0               #No 1° ataque vilao morre
    matriz = campo
    prioridades = [20, 16, 16, 15, 15]      #Prioridade segue a ordem das condições abaixo (condicoes.append)
    
    vilao_linha, vilao_coluna = localizar_vilao(matriz) #Localiza vilão pois ele não se move até atacar
    bonus_linha, bonus_coluna = localizar_bonus(matriz) #Localiza bonus pois ele não se move até ser pego
    
    while(ataque < VIDA_VILAO): #Loop até a morte do vilão
        time.sleep(1)

        if(heroi_movimentou == 0):
            heroi_movimentou = 1
        elif(heroi_movimentou == 1):
            heroi_movimentou = 0

        condicoes = []      #Zera a lista de condições

        mostrar_matriz(matriz)
        print(f"Valor Ataque: {ataque}")
        heroi_linha, heroi_coluna = localizar_heroi(matriz)

        #Movimentos de ataque
        condicoes.append(heroi_coluna == vilao_coluna and heroi_linha == vilao_linha) #Ataca (20)

        #Movimentos em relação ao vilão
        condicoes.append(vilao_coluna < heroi_coluna)   #Esquerda
        condicoes.append(vilao_coluna > heroi_coluna)   #Direita
        condicoes.append(vilao_linha < heroi_linha)     #Cima
        condicoes.append(vilao_linha > heroi_linha)     #Baixo

        posicao = decidir(condicoes, prioridades)

        #Ataques
        if(posicao == 1):
            ataque += 1
            print("Ataque Normal")
            teleportar_vilao(matriz)
            vilao_linha, vilao_coluna = localizar_vilao(matriz) #Já localiza o vilão na nova posição

        #movimento Heroi
        elif(posicao == 2 and heroi_movimentou == 0):
            mover_heroi(matriz, heroi_linha, heroi_coluna-1)
            print("Ir para Esquerda Vilão")
        elif(posicao == 3 and heroi_movimentou == 0):
            mover_heroi(matriz, heroi_linha, heroi_coluna+1)
            print("Ir para Direita Vilão")
        elif(posicao == 4 and heroi_movimentou == 0):
            mover_heroi(matriz, heroi_linha-1, heroi_coluna)
            print("Ir para Cima Vilão")
        elif(posicao == 5 and heroi_movimentou == 0):
            mover_heroi(matriz, heroi_linha+1, heroi_coluna)
            print("Ir para Baixo Vilão")

        #movimento vilao
        if(heroi_movimentou == 1):
            linha = random.randint(vilao_linha-1, vilao_linha+1)
            coluna = random.randint(vilao_coluna-1, vilao_coluna+1)
            mover_vilao(matriz, linha, coluna)

        if(ataque == VIDA_VILAO):
            print("\n\nVilão Morto")
            print("Heroi Venceu")
            break

rodar_jogo(campo)