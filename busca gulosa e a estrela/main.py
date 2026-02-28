# Apenas as distâncias de todas as cidades em linha reta até Bucareste são consideradas. Essas distâncias estão na tabela. Ou seja, não se sabe a distância de Arad a Cralova em linha reta, por exemplo, e tudo bem.

# As distâncias entre os vizinhos são as estradas do mapa, ou seja, as arestas do grafo. As cidades são os nós do grafo.

# OK - Insira as cidades manualmente no código.
# A busca gulosa não é a busca cega (que varreria todos os nós), portanto há pelo menos uma função heurística simples, a menor distância do vizinho até Bucareste.

# OK - A entrada do programa pelo usuário é apenas a cidade da qual desejo partir (origem) para chegar em Bucareste (destino) e o algoritmo de busca escolhido (gulosa ou A*).

# A saída do programa é o caminho mostrando todas as cidades da origem até Bucareste.

# OK - Pode ser feito em Java, Python ou C.

# Enviar o código pelo Moodle para ser analisado.


class Cidade:
    def __init__(self, nome, distancia, visinhos):
        self.nome = nome
        self.distancia = distancia
        self.visinhos = visinhos

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

#criando um dicionario para armazenar as cidades e suas distâncias
dicionario_cidade = {nome: (distancia, visinhos) for nome, distancia, visinhos in grafo}

#listas/armazenando a lista do grafo em cidades
cidades = [Cidade(nome, distancia, visinhos) for nome, distancia, visinhos in grafo]
algoritmos = ['gulosa', 'a*']

#escolha do algoritmo:
escolha = int(input("Gulosa = 1 ou A* = 2 \nDigite o algoritmo: "))-1
print("Algoritmo selecionado: ", algoritmos[escolha])

#menu de cidades
print("\n====== Lista de cidades: ======")
for cidade in cidades:
    print(cidade.nome)

#Pega a primeira cidade
origem = input("Por onde quer começar? ").lower()
destino = "Bucharest"

def validar_cidade(origem):
    for cidade in cidades:
        if cidade.nome.lower() == origem:
            origem = cidade
            print("Cidade de origem selecionada:", origem.nome)
            break
        else : 
            print("cidade nao encontrada")
            return 1

# print(origem)

def busca_a_estrela(origem, destino):
    print("Buscando estrela...")
    #g -> custo do caminho do nó inicial até o nó n
    #h -> valor da heurística do nó n até um nó objetivo.


def busca_gulosa(origem):
    atual = origem.nome
    cidade_visitada = []

    menor_distancia = float('inf')

    lista_visinhos = []
    while atual != destino:
        visinhos = dicionario_cidade[atual][1]

        for v in visinhos:
            if v in cidade_visitada:
                continue
            menor_distancia = dicionario_cidade[v][0]
            lista_visinhos.append((menor_distancia, v))
        
        lista_visinhos.sort()
        menor_distancia = lista_visinhos[0][1]

        atual = menor_distancia
        cidade_visitada.append(atual)
        print("Próxima cidade escolhida:", atual)
    print("Chegou em Bucareste!")

    if len(cidade_visitada) > 0:
        print("cidades visitadas: ")
        for c in cidade_visitada:
            print(c)
    else: 
        print("Nenhuma cidade foi visitada.")

#direção das escolhas dos algoritmos
if validar_cidade(origem):
    if escolha == 0:
        busca_gulosa(origem)
    else:
        busca_a_estrela(origem)
