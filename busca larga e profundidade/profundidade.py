# Estrutura do Grafo: Nome e Lista de Vizinhos (Estilo IA)
dados_grafo = [
    ("3", ["18", "4", "17"]),
    ("1", ["15", "14"]),
    ("14", ["1", "16", "13", "12"]),
    ("16", ["14"]),
    ("15", ["1", "2"]),
    ("12", ["14"]),
    ("13", ["14", "10"]),
    ("2", ["15", "17"]),
    ("17", ["2", "3"]),
    ("18", ["3"]),
    ("4", ["3", "5"]),
    ("5", ["4", "9", "6"]),
    ("9", ["10", "5"]),
    ("10", ["13", "9"]),
    ("6", ["5", "7"]),
    ("7", ["6", "19"]),
    ("19", ["7"])
]

grafo = [
    ("A", ["B"]),
    ("B", ["A", "C"]),
    ("C", ["B", "D", "F"]),
    ("D", ["C","G"]),
    ("E", ["F"]),
    ("F", ["C", "E", "G"]),
    ("G", ["D", "F", "H", "I"]),
    ("H", ["G", "J", "L"]),
    ("I", ["G", "M", "K"]),
    ("J", ["H", "L"]),
    ("K", ["I", "O"]),
    ("L", ["H", "J", "N"]),
    ("M", ["I", "P", "Q"]),
    ("N", ["L"]),
    ("O", ["K", "Q", "R"]),
    ("P", ["M"]),
    ("Q", ["M", "O"]),
    ("R", ["O"])
]

class No:
    def __init__(self, nome, vizinhos):
        self.nome = nome
        self.vizinhos = vizinhos

    @staticmethod
    def dicionario_grafo(dados):
        return {nome: vizinhos for nome, vizinhos in dados}

    @staticmethod
    def lista_nos(dados):
        return [No(nome, vizinhos) for nome, vizinhos in dados]

## <============ DEFINIR o Grafo aqui ===============>
dicionario = No.dicionario_grafo(grafo)
mapa_nos = No.lista_nos(grafo)

# =========== Algoritmo DFS (Busca em Profundidade) ===========

def busca_em_profundidade(origem, destino):
    # Pilha armazena (no_atual, caminho_percorrido) - LIFO
    pilha = [(origem, [origem])]
    visitados = []

    while pilha:
        # pop() remove o último elemento inserido (o topo da pilha)
        n, caminho = pilha.pop() 

        if n == destino:
            print(f"Caminho encontrado: {' -> '.join(caminho)}")
            print(f"Ordem de visitação: {', '.join(visitados)}\n")
            return

        if n not in visitados:
            print(f"Visitando {n}") # Monitoramento visual
            visitados.append(n)
            
            # Adicionando vizinhos na pilha
            for vizinho in dicionario.get(n, []):
                if vizinho not in visitados:
                    pilha.append((vizinho, caminho + [vizinho]))

    print("Caminho não encontrado.")

# =========== Menu e Main (Seu Padrão Consolidado) ===========

def menu():
    print("== Menu Busca em Profundidade (DFS) ==")
    print("1 - Iniciar Busca")
    print("0 - Sair")
    try:
        return int(input("\nDigite a opção: "))
    except:
        return -1

def main():
    while True:
        escolha = menu()

        if escolha == 0:
            print("Encerrando sistema...")
            break
        
        if escolha == 1:
            print("\n====== Lista de Nós Disponíveis: ======")
            for no in mapa_nos:
                print(no.nome, end=" | ")
            print()

## <=========== Definir o tipo aqui: .title() se for string e sem caso for inteiro.
            # origem = input("\nNó de Origem: ")
            origem = input("\nNó de Origem: ").title() ## <============ Definir o tipo aqui
            # destino = input("Nó de Destino: ")
            destino = input("Nó de Destino: ").title() 

            if origem in dicionario and destino in dicionario:
                busca_em_profundidade(origem, destino)
            else:
                print("Erro: Nó não encontrado.")
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()