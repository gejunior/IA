# Apenas as distâncias de todas as cidades em linha reta até Bucareste são consideradas. Essas distâncias estão na tabela. Ou seja, não se sabe a distância de Arad a Cralova em linha reta, por exemplo, e tudo bem.

# As distâncias entre os vizinhos são as estradas do mapa, ou seja, as arestas do grafo. As cidades são os nós do grafo.

# OK - Insira as cidades manualmente no código.
# A busca gulosa não é a busca cega (que varreria todos os nós), portanto há pelo menos uma função heurística simples, a menor distância do vizinho até Bucareste.

# OK - A entrada do programa pelo usuário é apenas a cidade da qual desejo partir (origem) para chegar em Bucareste (destino) e o algoritmo de busca escolhido (gulosa ou A*).

# A saída do programa é o caminho mostrando todas as cidades da origem até Bucareste.

# OK - Pode ser feito em Java, Python ou C.

# Enviar o código pelo Moodle para ser analisado.

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
    print("Buscando estrela...")
    #g -> custo do caminho do nó inicial até o nó n
    #h -> valor da heurística do nó n até um nó objetivo.


def busca_gulosa(origem, destino):
    cidade_atual = origem
    destino_aux = destino
    rota = [cidade_atual] #cidades visitadas
    
    while cidade_atual != destino_aux:
        vizinhos = dicionario[cidade_atual][1]
        caminho = []

        for v in vizinhos:
            if v not in rota: #evita cidades visitadas
                distancia_h = dicionario[v][0] #pega a heurística h(n) (caminho em linha reta)
                caminho.append((distancia_h, v))
        
        if not caminho:
            print("Caminho sem saída")
            break

        caminho.sort()
        
        melhor_escolha = caminho[0][1]

        cidade_atual = melhor_escolha
        rota.append(cidade_atual)
        print("Próxima cidade escolhida:", cidade_atual)
    print("Chegou em Bucareste!")

    if len(rota) > 0:
        print("cidades visitadas: ")
        for c in rota:
            print(c)
    else: 
        print("Nenhuma cidade foi visitada.")

#direção das escolhas dos algoritmos
if escolha == 0:
    busca_gulosa(origem, destino)
else:
    busca_a_estrela(origem)
