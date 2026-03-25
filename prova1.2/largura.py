#Estrutura: nome, vizinhos
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


def busca_largura(origem, destino):
    from collections import deque
    
    #fila armazena (no_atual, caminho_percorrido)
    fila = deque([(origem, [origem])])
    visitados = []

    while fila:
        n, caminho = fila.popleft() # FIFO: primeiro a entrar, primeiro a sair

        if n == destino:
            print(f"Caminho encontrado: {' -> '.join(caminho)}")
            print(f"Nós visitados: {', '.join(visitados)}")
            return

        if n not in visitados:
            print(f"Explorando nó: {n}")
            visitados.append(n)
            
            for vizinho in dicionario.get(n, []):
                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho]))

    print("Caminho impossível de encontrar.")

def menu():
    print("\n== Menu Busca em Largura ==")
    print("1 - Iniciar Busca")
    print("0 - Sair")
    return int(input("Escolha uma opção: "))

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
                busca_largura(origem, destino)
            else:
                print("Erro: Nó não encontrado no grafo.")
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()