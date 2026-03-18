# Estrutura: cidade, heuristica, vizinho, distancia
grafo = [
    ("Arad", 366, [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)]),
    ("Bucharest", 0, [("Urziceni", 85), ("Pitesti", 101), ("Giurgiu", 90), ("Fagaras", 211)]),
    ("Craiova", 160, [("Dobreta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)]),
    ("Dobreta", 242, [("Mehadia", 75), ("Craiova", 120)]),
    ("Eforie", 161, [("Hirsova", 86)]),
    ("Fagaras", 176, [("Sibiu", 99), ("Bucharest", 211)]),
    ("Giurgiu", 77, [("Bucharest", 90)]),
    ("Hirsova", 151, [("Urziceni", 98), ("Eforie", 86)]),
    ("Iasi", 226, [("Neamt", 87), ("Vaslui", 92)]),
    ("Lugoj", 244, [("Timisoara", 111), ("Mehadia", 70)]),
    ("Mehadia", 241, [("Lugoj", 70), ("Dobreta", 75)]),
    ("Neamt", 234, [("Iasi", 87)]),
    ("Oradea", 380, [("Zerind", 71), ("Sibiu", 151)]),
    ("Pitesti", 100, [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)]),
    ("Rimnicu Vilcea", 193, [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)]),
    ("Sibiu", 253, [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)]),
    ("Timisoara", 329, [("Arad", 118), ("Lugoj", 111)]),
    ("Urziceni", 80, [("Bucharest", 85), ("Vaslui", 142), ("Hirsova", 98)]),
    ("Vaslui", 199, [("Iasi", 92), ("Urziceni", 142)]),
    ("Zerind", 374, [("Oradea", 71), ("Arad", 75)])
]

#adicionando uma cidade
grafo.append(("Prova City", 280, [("Dobreta", 100), ("Mehadia", 110)]))

class Cidade:
    def __init__(self, nome, distancia, vizinhos):
        self.nome = nome
        self.distancia = distancia
        self.vizinhos = vizinhos

    #criando um dicionario para armazenar as cidades e suas distâncias
    @staticmethod
    def dicionario_cidade(dados_grafo):
        return {nome: (distancia, vizinhos) for nome, distancia, vizinhos in dados_grafo}
    
    @staticmethod
    #armazenando a lista do grafo em cidades
    def cidades(dados_grafo):
        return [Cidade(nome, distancia, vizinhos) for nome, distancia, vizinhos in dados_grafo]
        
dicionario = Cidade.dicionario_cidade(grafo)
mapa_cidades = Cidade.cidades(grafo)

# =========== inicio do programa ===============

def busca_a_estrela(origem, destino):
    #inicializa Q com o no de busca
    #formato: (f, g, estado_atual, caminho)
    h_inicial = dicionario[origem][0]
    q = [(h_inicial, 0, origem, [origem])]
    visitados = []

    while q:
        #escolhendo o menor elemento de Q
        q.sort()

        #g -> custo do caminho do nó inicial até o nó n
        #h -> valor da heurística do nó n até um nó objetivo.
        f, g, n, caminho_ate_n = q.pop(0)

        if n == destino:
            print(f"Custo total: {g}")
            print(f"Rota { '->'.join(caminho_ate_n)}")
            print(f"Cidades visitadas { '->'.join(visitados)}\n")
            return
        
        if n not in visitados:
            print(f"Visitando {n} (f: {f})")
            visitados.append(n)
            vizinhos = dicionario[n][1]

            for v_nome, v_distancia in vizinhos:
                if v_nome not in visitados:
                    g_novo = g + v_distancia
                    h_novo = dicionario[v_nome][0]
                    f_novo = g_novo + h_novo
                    novo_caminho = caminho_ate_n + [v_nome]
                    q.append([f_novo, g_novo, v_nome, novo_caminho])
    


def busca_gulosa(origem, destino):
    cidade_atual = origem
    rota = [cidade_atual]
    
    while cidade_atual != destino:
        vizinhos = dicionario[cidade_atual][1]
        caminho_opcoes = []

        if cidade_atual not in dicionario:
            print("Cidade nao encontrada!")
            return
        
        for v_nome, v_distancia in vizinhos:
            if v_nome not in rota: #evita cidades visitadas
                distancia_h = dicionario[v_nome][0] #pega a heurística h(n) (caminho em linha reta)
                caminho_opcoes.append((distancia_h, v_nome))
        
        if not caminho_opcoes:
            print("Caminho sem saída")
            break

        caminho_opcoes.sort()
        cidade_atual = caminho_opcoes[0][1]
        print(f"Indo para {cidade_atual} (h: {dicionario[cidade_atual][0]})") #indicando a proxima
        rota.append(cidade_atual)
    
    # print(f"Chegou em {origem}!")
    # print(f"passos: {len(rota)}")
    print(f"Rota Final: { '->'.join(rota)}\n")

def menu():
    print("== Menu ==")
    print("1 - Gulosa ")
    print("2 - A* ")
    print("0 - Sair")
    return int(input("\nDigite a opcao: ")) 

def main():
    while True:
        escolha = menu()
        
        if escolha == 0:
            print("Encerrando sistema")
            break

        #menu de cidades
        print("\n====== Lista de cidades: ======")
        for cidade in mapa_cidades:
            print(cidade.nome)

        #Pega a primeira cidade
        origem = input("\nPor onde quer começar? ").title()
        #definir o destino
        destino = "Bucharest"
        # destino = input("\nQual é o destino? ").title()

        #direção das escolhas dos algoritmos
        if escolha == 1:
            print("Busca Gulosa ")
            busca_gulosa(origem, destino)
        elif escolha == 2:
            print("Busca A* ")
            busca_a_estrela(origem, destino)
        else:
            print("Opcao invalida.")
    
    # print("finalizando o programa.")
        
if __name__ == "__main__":
    main()