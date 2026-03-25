import random
import time

TAMANHO_LINHAS = 10
TAMANHO_COLUNAS = 10

#campo 10x10
campo = ([
    ['-', '-', '-', '-', 'p1', '-', '-', '-', '-', '-'],
    ['-', 'p2', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', 'p2', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', 'p1', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', 'p1', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', 'p2', '-', '-']
])

class Carro:
    def __init__(self, nome, caracter, pos_x, pos_y):
        self.nome = nome
        self.caracter = caracter
        self.pos_x = pos_x
        self.pos_y = pos_y

    def mover_esquerda(self):
        if self.pos_x > 0: self.pos_x -= 1
    def mover_direita(self):
        if self.pos_x > TAMANHO_LINHAS - 1: self.pos_x += 1
    def mover_cima(self):
        if self.pos_y > 0: self.pos_y -= 1
    def mover_baixo(self):
        if self.pos_y < TAMANHO_LINHAS - 1: self.pos_y += 1
    def pos_x(self):
        return self.pos_x
    def pos_y(self):
        return self.pos_y
    def __str__(self):
        return f"nome:{self.nome}, caracter: {self.caracter} posicao x: {self.pos_x} posicao y: {self.pos_y}"


def iniciar_campo(matriz): #heroi, vilao, e bonus recebem posições aleatórias (NÃO IGUAIS)
    # Carro 1
    c1 = Carro("carro 1", "c1", 9, 0)
    c1.__str__()
    # Carro 2
    c2 = Carro("carro 2", "c2", 9, 9)
    c1.str()

    #objetivo
    # ob_linha = random.randint(0, 9)
    # ob_coluna = random.randint(0, 9)

    # matriz[c1.pos_x][c1.pos_y] = c1.caracter
    # matriz[c2.pos_x][c2.pos_y] = c2.caracter
    # matriz[ob_linha][ob_coluna] = 'o'

    # return c1, c2

def localizar_carro1(matriz): #Retorna (linha e coluna) de localização carro 1
    for i in range(TAMANHO_LINHAS):
        for j in range(TAMANHO_COLUNAS):
            if(matriz[i][j] == 'c1'):
                print(f"carro 1 Linha:{i}")
                print(f"carro 1 Coluna:{j}")
                return i, j
            
def localizar_carro2(matriz): #Retorna (linha e coluna) de localização carro 2
    for i in range(TAMANHO_LINHAS):
        for j in range(TAMANHO_COLUNAS):
            if(matriz[i][j] == 'c2'):
                print(f"carro 2 Linha:{i}")
                print(f"carro 2 Coluna:{j}")
                return i, j

def localizar_objetivo(matriz): #Retorna (linha e coluna) de localização objetivo
    for i in range(TAMANHO_LINHAS):
        for j in range(TAMANHO_COLUNAS):
            if(matriz[i][j] == 'o'):
                print(f"Objetivo Linha:{i}")
                print(f"Objetivo Coluna:{j}")
                return i, j
            
def localizar_bonus_p1(matriz): #Retorna (linha e coluna) de localização bonus P1
    for i in range(TAMANHO_LINHAS):
        for j in range(TAMANHO_COLUNAS):
            if(matriz[i][j] == 'p1'):
                print(f"Bonus 1 Linha:{i}")
                print(f"Bonus 1 Coluna:{j}")
                return i, j
            
def localizar_bonus_p2(matriz): #Retorna (linha e coluna) de localização bonus P2
    for i in range(TAMANHO_LINHAS):
        for j in range(TAMANHO_COLUNAS):
            if(matriz[i][j] == 'p2'):
                print(f"Bonus 2 Linha:{i}")
                print(f"Bonus 2 Coluna:{j}")
                return i, j
            
# Mover carro 1 e 2
def mover_carro1(matriz, i, j): #Move o heroi para nova posição
    i_h, j_h = localizar_carro1(matriz)
    matriz[i_h][j_h] = '-'
    matriz[i+1][j+1] = 'c1'

def mover_carro2(matriz, i, j): #Move o heroi para nova posição
    i_h, j_h = localizar_carro2(matriz)
    matriz[i_h][j_h] = '-'
    matriz[i+1][j+1] = 'c2'

def mover_objetivo(matriz, i, j): #Move o objetivo para nova posição (esquerda/direita)
    i_h, j_h = localizar_objetivo(matriz)
    matriz[i_h][j_h] = '-'
    matriz[i][j] = 'o'

def teleportar_bonus_p1(matriz):
    """Teleporta bonus para nova posição vazia"""
    while True:
        i_b = random.randint(0, 9)
        j_b = random.randint(0, 9)
        # Só teleporta para posição vazia ('-')
        if matriz[i_b][j_b] == '-':
            # Limpa posição anterior do bonus
            for i in range(TAMANHO_LINHAS):
                for j in range(TAMANHO_COLUNAS):
                    if matriz[i][j] == 'p1':
                        matriz[i][j] = '-'
            # Coloca bonus na nova posição
            matriz[i_b][j_b] = 'p1'
            break

def teleportar_bonus_p2(matriz):
    """Teleporta bonus para nova posição vazia"""
    while True:
        i_b = random.randint(0, 9)
        j_b = random.randint(0, 9)
        # Só teleporta para posição vazia ('-')
        if matriz[i_b][j_b] == '-':
            # Limpa posição anterior do bonus
            for i in range(TAMANHO_LINHAS):
                for j in range(TAMANHO_COLUNAS):
                    if matriz[i][j] == 'p2':
                        matriz[i][j] = '-'
            # Coloca bonus na nova posição
            matriz[i_b][j_b] = 'p2'
            break


#### ========================================================
def decidir(lista_condicoes, lista_prioridades): #Analisa as condiçoes e prioridades e retorna a posicao (ação)
    maior_prioridade = 0
    posicao = 0

    for i in range(len(lista_condicoes)):
        if(lista_condicoes[i] == True):
            if(lista_prioridades[i] > maior_prioridade):
                maior_prioridade = lista_prioridades[i]
                posicao = i

    return posicao
#### ========================================================

def mostrar_matriz(matriz):
    for i in range(TAMANHO_LINHAS):
        print() #Quebra de linha para cada linha da matriz
        for j in range(TAMANHO_COLUNAS):
            print(matriz[i][j], end=" ")
    print()     #Quebra de linha para o final da matriz

def rodar_jogo(campo):
    iniciar_campo(campo)
    matriz = campo
    Objetivo = 1 #definir se o carro chegou ao objetivo
    carro1_movimentou = 1
    carro2_movimentou = 1

    p1 = 0
    p2 = 0

    prioridades = [20, 16, 16, 15, 15]      #Prioridade segue a ordem das condições abaixo (condicoes.append)
    
    ob_linha, ob_coluna = localizar_objetivo(matriz) #Localiza vilão pois ele não se move até atacar
    p1_linha, p1_coluna = localizar_bonus_p1(matriz)
    p2_linha, p2_coluna = localizar_bonus_p2(matriz)
    
    while (Objetivo): #Loop até a chegada de um dos carros
        time.sleep(1)

        if(carro1_movimentou == 0):
            carro1_movimentou = 1
        elif(carro1_movimentou == 1):
            carro1_movimentou = 0
        
        if(carro2_movimentou == 0):
            carro2_movimentou = 1
        elif(carro2_movimentou == 1):
            carro2_movimentou = 0

        condicoes1 = []
        condicoes2 = []      #Zera a lista de condições

        mostrar_matriz(matriz)
        c1_linha, c1_coluna = localizar_carro1(matriz)
        c2_linha, c2_coluna = localizar_carro2(matriz)

        condicoes1.append(c1_coluna == ob_coluna and c1_linha == ob_linha) #Ataca (20)
        #Movimentos carro 1
        condicoes1.append(ob_coluna < c1_coluna)   #Esquerda
        condicoes1.append(ob_coluna > c1_coluna)   #Direita
        condicoes1.append(ob_linha < c1_linha)     #Cima
        condicoes1.append(ob_linha > c1_linha)     #Baixo

        condicoes2.append(c2_coluna == ob_coluna and c2_linha == ob_linha) #Ataca (20)
        #Movimentos carro 2
        condicoes2.append(ob_coluna < c2_coluna)   #Esquerda
        condicoes2.append(ob_coluna > c2_coluna)   #Direita
        condicoes2.append(ob_linha < c2_linha)     #Cima
        condicoes2.append(ob_linha > c2_linha)     #Baixo

        posicao1 = decidir(condicoes1, prioridades)
        posicao2 = decidir(condicoes2, prioridades)

        if(posicao1 == 1): # Regra 1 - Prioridade 10
            print("Carro 1 Venceu!")
            Objetivo = True

    #     #movimento carro1
        elif(posicao1 == 2 and carro1_movimentou == 0): # Regra 2 - Prioridade 1
            mover_carro1(matriz, c1_linha, c1_coluna-1)
            print("Ir para Esquerda C1")
        elif(posicao1 == 3 and carro1_movimentou == 0): # Regra 3 - Prioridade 2
            mover_carro1(matriz, c1_linha, c1_coluna+1)
            print("Ir para Direita C1")
        elif(posicao1 == 4 and carro1_movimentou == 0): # Regra 4 - Prioridade 3
            mover_carro1(matriz, c1_linha-1, c1_coluna)
            print("Ir para Cima C1")
        elif(posicao1 == 5 and carro1_movimentou == 0): # Regra 5 - Prioridade 4
            mover_carro1(matriz, c1_linha+1, c1_coluna)
            print("Ir para Baixo C1")

        if(posicao2 == 1): # Regra 6 - Prioridade 9
            print("Carro 2 Venceu!")
            Objetivo = True

    #     #movimento carro1
        elif(posicao2 == 2 and carro2_movimentou == 0): # Regra 7 - Prioridade 5 
            mover_carro1(matriz, c2_linha, c2_coluna-1)
            print("Ir para Esquerda C2")
        elif(posicao2 == 3 and carro2_movimentou == 0): # Regra 8 - Prioridade 6
            mover_carro1(matriz, c2_linha, c2_coluna+1)
            print("Ir para Direita C2")
        elif(posicao2 == 4 and carro2_movimentou == 0): # Regra 9 - Prioridade 7
            mover_carro1(matriz, c2_linha-1, c2_coluna)
            print("Ir para Cima C2")
        elif(posicao2 == 5 and carro2_movimentou == 0): # Regra 10 - Prioridade 8
            mover_carro1(matriz, c2_linha+1, c2_coluna)
            print("Ir para Baixo C2")


        if(c1_coluna == p1_coluna and c1_linha == p1_linha): # Regra 11 - Prioridade 8
            if(p1 < 6):
                mover_objetivo(matriz, ob_linha-1, ob_coluna)
                p1+= 1
            else:
                print("Limite p1 atingido")
        if(c2_coluna == p2_coluna and c2_linha == p2_linha): # Regra 12 - Prioridade 8
            if(p1 < 6):
                mover_objetivo(matriz, ob_linha+1, ob_coluna)
                p2+= 1
            else:
                print("Limite p2 atingido")


    print("Corrida Finalizada")
if __name__ == "__main__":
    # rodar_jogo(campo)
    iniciar_campo(campo)