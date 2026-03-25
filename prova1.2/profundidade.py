# Estrutura: nome e vizinhos
grafo = [
    ("1", ["15", "14"]),
    ("2", ["15", "17"]),
    ("3", ["18", "4", "17"]),
    ("4", ["3", "5"]),
    ("5", ["4", "9", "6"]),
    ("6", ["5", "7"]),
    ("7", ["6", "19"]),
    ("9", ["10", "5"]),
    ("10", ["13", "9"]),
    ("12", ["14"]),
    ("13", ["14", "10"]),
    ("14", ["1", "16", "13", "12"]),
    ("15", ["1", "2"]),
    ("16", ["14"]),
    ("17", ["2", "3"]),
    ("18", ["3"]),
    ("19", ["7"])
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

dicionario = No.dicionario_grafo(grafo)
mapa_nos = No.lista_nos(grafo)

def busca_em_profundidade(origem, destino):
    # Pilha armazena (no_atual, caminho_percorrido) - LIFO
    pilha = [(origem, [origem])]
    visitados = []

    while pilha:
        # pop() remove o último elemento inserido (o topo da pilha)
        n, caminho = pilha.pop() 

        if n == destino:
            print(f"Caminho encontrado: {' -> '.join(caminho)}")
            print(f"Nós visitados: {', '.join(visitados)}\n")
            return

        if n not in visitados:
            print(f"Visitando {n}") # Monitoramento visual
            visitados.append(n)
            
            # Adicionando vizinhos na pilha
            for vizinho in dicionario.get(n, []):
                if vizinho not in visitados:
                    pilha.append((vizinho, caminho + [vizinho]))

    print("Caminho não encontrado.")

def menu():
    print("== Menu Busca em Profundidade ==")
    print("1 - Iniciar Busca")
    print("0 - Sair")
    return int(input("\nDigite a opção: "))

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

            origem = input("\nNó de Origem: ")
            destino = input("Nó de Destino (ex: 19): ")

            if origem in dicionario and destino in dicionario:
                busca_em_profundidade(origem, destino)
            else:
                print("Erro: Nó não encontrado.")
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()