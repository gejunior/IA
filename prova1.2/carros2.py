import random
import time
import os

TAMANHO_LINHAS = 10
TAMANHO_COLUNAS = 10

#campo 10x10
def gerar_campo(): return [
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
]

class Carro:
    def __init__(self, nome, caracter, pos_x, pos_y):
        self.nome = nome
        self.caracter = caracter
        self.pos_x = pos_x
        self.pos_y = pos_y

    def mover_esquerda(self):
        if self.pos_x > 0: self.pos_x -= 1
    def mover_direita(self):
        if self.pos_x < TAMANHO_COLUNAS - 1: self.pos_x += 1

    def mover_cima(self):
        if self.pos_y > 0: self.pos_y -= 1
    def mover_baixo(self):
        if self.pos_y < TAMANHO_LINHAS - 1: self.pos_y += 1
        
    def pos_linha(self):
        return self.pos_x
    def pos_coluna(self):
        return self.pos_y
    def __str__(self):
        return f"nome:{self.nome}, caracter: {self.caracter} posicao x: {self.pos_x} posicao y: {self.pos_y}"

class Objetivo:
    def __init__(self, nome, caracter, pos_x, pos_y):
        self.nome = nome
        self.caracter = caracter
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def pos_linha(self):
        return self.pos_x
    def pos_coluna(self):
        return self.pos_y
    
    def __str__(self):
        return f"nome:{self.nome}, caracter: {self.caracter} posicao x: {self.pos_x} posicao y: {self.pos_y}"

    

def iniciar_campo(matriz):
    # Carro 1
    c1 = Carro("carro 1", "c1", 9, 0)
    # Carro 2
    c2 = Carro("carro 2", "c2", 9, 9)
    #objetivo
    ob = Objetivo("Objetivo", "O", random.randint(0, 9), random.randint(0, 9))

    matriz[c1.pos_x][c1.pos_y] = c1.caracter
    matriz[c2.pos_x][c2.pos_y] = c2.caracter
    matriz[ob.pos_x][ob.pos_y] = ob.caracter

    return c1, c2, ob

def mostrar_matriz(matriz):
    os.system('cls' if os.name == 'nt' else 'clear')
    for linha in matriz:
        print(" ".join(linha))

def rodar_jogo(campo):
    c1, c2, ob = iniciar_campo(campo)
    carros = [c1, c2]
    matriz = campo

    while True:
        mostrar_matriz(matriz)
        for c in carros:
            matriz[c.pos_x][c.pos_y] = '-'
            # Regra 1 - Prioridade 7
            if c.pos_x == ob.pos_x and c.pos_y == ob.pos_y: 
                mostrar_matriz(matriz)
                print(f"Fim de jogo! {c.nome} chegou ao fim")
                return
            
            # Regra 2 -  Prioridade 2
            if matriz[c.pos_x][c.pos_y] == "p1" and c. caracter == "c1":
                if(c.pos_x + 1 < TAMANHO_COLUNAS - 1):
                    c.mover_direita()
                else: print(f"Não é possível mover {c.nome}")
            
            # Regra 3 - Prioridade 2
            elif matriz[c.pos_x][c.pos_y] == "p2" and c.caracter == "c2":
                if(c.pos_x - 1 > 0):
                    c.mover_esquerda()
                else: print(f"Não é possível mover {c.nome}")
            
            # Regra 4 - Prioridade 3
            if c.pos_x > ob.pos_x: c.mover_esquerda()
            
            # Regra 5 - Prioridade 3
            elif c.pos_x < ob.pos_x: c.mover_direita()
            
            # Regra 6 - Prioridade 4
            if c.pos_y > ob.pos_y: c.mover_cima()
            
            # Regra 7 - Prioridade 4
            elif c.pos_y < ob.pos_y: c.mover_baixo()
            #atualiza a matriz
            matriz[c.pos_x][c.pos_y] = c.caracter

        time.sleep(0.5)

def menu():
    print("[1] iniciar jogo")
    print("[0] sair do jogo")
    return int(input("Digite a opcao: "))

if __name__ == "__main__":
    while menu() != 0:
        campo_novo = gerar_campo()
        rodar_jogo(campo_novo)
    print("Até a proxima!")