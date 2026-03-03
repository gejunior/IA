
##### testar inserindo uma nova cidade #####

grafo = [
    ("Arad", 366, ["Zerind", "Sibiu", "Timisoara"]),
    ("Bucharest", 0, ["Urziceni", "Pitesti", "Giurgiu", "Fagaras"]),
    ("Craiova", 160, ["Dobreta", "Rimnicu Vilcea", "Pitesti"]),
    ("Dobreta", 242, ["Mehadia", "Craiova"]),
    ("Eforie", 161, ["Hirsova"]),
    ("Fagaras", 176, ["Sibiu", "Bucharest"]),
    ("Giurgiu", 77, ["Bucharest"]),
    ("Hirsova", 151, ["Urziceni", "Eforie"]),
    ("Iasi", 226, ["Neamt", "Vaslui"]),
    ("Lugoj", 244, ["Timisoara", "Mehadia"]),
    ("Mehadia", 241, ["Lugoj", "Dobreta"]),
    ("Neamt", 234, ["Iasi"]),
    ("Oradea", 380, ["Zerind", "Sibiu"]),
    ("Pitesti", 100, ["Rimnicu Vilcea", "Craiova", "Bucharest"]),
    ("Rimnicu Vilcea", 193, ["Sibiu", "Craiova", "Pitesti"]),
    ("Sibiu", 253, ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"]),
    ("Timisoara", 329, ["Arad", "Lugoj"]),
    ("Urziceni", 80, ["Bucharest", "Vaslui", "Hirsova"]),
    ("Vaslui", 199, ["Iasi", "Urziceni"]),
    ("Zerind", 374, ["Oradea", "Arad"])
]

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
    #listas/armazenando a lista do grafo em cidades
    def cidades(dados_grafo):
        return [Cidade(nome, distancia, vizinhos) for nome, distancia, vizinhos in dados_grafo]
        
dicionario = Cidade.dicionario_cidade(grafo)
mapa_cidades = Cidade.cidades(grafo)
algoritmos = ['gulosa', 'a*']

#escolha do algoritmo:
escolha = int(input("Gulosa = 1 ou A* = 2 \nDigite o algoritmo: "))-1
print("Algoritmo selecionado: ", algoritmos[escolha])

#menu de cidades
print("\n====== Lista de cidades: ======")
for cidade in mapa_cidades:
    print(cidade.nome)

#Pega a primeira cidade
origem = input("Por onde quer começar? ").title()
destino = "Bucharest"

def busca_a_estrela(origem, destino):
    # cidade_atual = origem

    #inicializa Q com o no de busca
    #formato: (f, g, estado_atual, caminho)
    h_inicial = dicionario[origem][0]
    q = [(h_inicial, 0, origem, [origem])]
    visitados = []

    #se q esta vazio, interrompe
    while len(q) > 0:
        #escolhendo o menor elemento de Q
        q.sort()

        #g -> custo do caminho do nó inicial até o nó n
        #h -> valor da heurística do nó n até um nó objetivo.
        f, g, n, caminho_ate_n = q.pop(0)

        if n == destino:
            print(f"passos: {g}")
            print(f"Rota { '->'.join(caminho_ate_n)}")
            return
        
        if n not in visitados:
            visitados.append(n)
            vizinhos = dicionario[n][1]

            for descendente in vizinhos:
                if descendente not in visitados:
                    g_novo = g + 1
                    h_novo = dicionario[descendente][0]
                    f_novo = g_novo + h_novo

                    novo_caminho = caminho_ate_n + [descendente]

                    q.append([f_novo, g_novo, descendente, novo_caminho])


def busca_gulosa(origem, destino):
    cidade_atual = origem
    rota = [cidade_atual]
    
    while cidade_atual != destino:
        if cidade_atual not in dicionario:
            print("Cidade nao encontrada!")
            return

        vizinhos = dicionario[cidade_atual][1]
        caminho_opcoes = []

        for v in vizinhos:
            if v not in rota: #evita cidades visitadas
                distancia_h = dicionario[v][0] #pega a heurística h(n) (caminho em linha reta)
                caminho_opcoes.append((distancia_h, v))
        
        if not caminho_opcoes:
            print("Caminho sem saída")
            break

        caminho_opcoes.sort()
        melhor_escolha = caminho_opcoes[0][1]
        cidade_atual = melhor_escolha
        rota.append(cidade_atual)
    print("Chegou em Bucareste!")

    print(f"Rota { '->'.join(rota)}")

#direção das escolhas dos algoritmos
if escolha == 0:
    busca_gulosa(origem, destino)
else:
    busca_a_estrela(origem, destino)
