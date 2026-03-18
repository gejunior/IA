#Estrutura: nome, vizinhos
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

dicionario = No.dicionario_grafo(dados_grafo)
mapa_nos = No.lista_nos(dados_grafo)


def busca_largura(origem, destino):
    from collections import deque
    
    #fila armazena (no_atual, caminho_percorrido)
    fila = deque([(origem, [origem])])
    visitados = []

    while fila:
        n, caminho = fila.popleft() # FIFO: primeiro a entrar, primeiro a sair

        if n == destino:
            print(f"Caminho encontrado: {' -> '.join(caminho)}")
            print(f"Cidades/Nós visitados: {', '.join(visitados)}")
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
            destino = input("Nó de Destino (ex: 13): ")

            if origem in dicionario and destino in dicionario:
                busca_largura(origem, destino)
            else:
                print("Erro: Nó não encontrado no grafo.")
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()