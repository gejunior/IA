from collections import deque

class No:
    def __init__(self, valor):
        self.valor = valor
        self.vizinhos = [] 

class Grafo:
    def __init__(self, raiz):
        self.raiz = raiz

    def conectar(self, no_novo, no_alvo = None):
        if no_alvo is None:
            no_alvo = self.raiz
        
        no_novo.vizinhos.append(no_alvo)
        no_alvo.vizinhos.append(no_novo)
        return no_novo
    
    def buscar_em_largura(self, valor_procurado):
        visitados = set()
        fila = deque([self.raiz])
        visitados.add(self.raiz.valor)

        while fila:
            atual = fila.popleft()
            print(f"{atual.valor} -> ", end="")

            if atual.valor == valor_procurado:
                print("Encontrou!!")
                return atual
            
            for vizinho in atual.vizinhos:
                if vizinho.valor not in visitados:
                    visitados.add(vizinho.valor)
                    fila.append(vizinho)
        print("Não encontrado")
        return None

#criando os nós
h = No("H")
grafo = Grafo(h)

e = grafo.conectar(No("E"), h)
f = grafo.conectar(No("F"), h)
j = grafo.conectar(No("J"), h)
k = grafo.conectar(No("K"), h)
i = grafo.conectar(No("I"), e)
grafo.conectar(i, k)

grafo.buscar_em_largura("I")