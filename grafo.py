class Vert:
    def __init__(self, rotulo):
        self.rotulo = rotulo
    def igualA(self, r):
        return r == self.rotulo

class Grafo:
    def __init__(self):
        self.NumeroVerticesMaximo = 20
        self.NumeroVertices = 0
        self.ListaVertices = []
        self.ListaArcos = []
        self.matrizAdjacencias = []
        for i in range(self.NumeroVerticesMaximo):
            linhaMatriz = []
            for j in range(self.NumeroVerticesMaximo):
                linhaMatriz.append(0)
            self.matrizAdjacencias.append(linhaMatriz)

    def adicionaVertices(self, rotulo):
        self.NumeroVertices += 1
        self.ListaVertices.append(Vert(rotulo))

    def adicionaArco(self, rotulo, peso, inicio, fim, rotuloInicio, rotuloFim):
        self.ListaArcos.append([rotulo, rotuloInicio, rotuloFim])
        self.matrizAdjacencias[inicio][fim] = peso
        self.matrizAdjacencias[fim][inicio] = peso

    def imprimeMatriz(self):
        print(" ", end=" ")
        for i in range(0, self.NumeroVertices):
            print(self.ListaVertices[i].rotulo, end=" ")
        print(" ")
        for i in range(0, self.NumeroVertices):
            print(self.ListaVertices[i].rotulo, end=" ")
            for j in range(0, self.NumeroVertices):
                print(self.matrizAdjacencias[i][j], end=" ")
            print(" ")

    def localizaNo(self, rotulo):
        for i in range(self.NumeroVertices):
            if self.ListaVertices[i].igualA(rotulo):
                return i
        return -1

    def localizaArco(self, rotulo):
        for i in range(len(self.ListaArcos)):
            if self.ListaArcos[i][0] == rotulo:
                return i
        return -1

    def localizaPorOrigemDestino(self, rotulo):
        list_retorno = []
        for i in range(0, len(self.ListaArcos)):
            if self.ListaArcos[i][1] == rotulo or self.ListaArcos[i][2] == rotulo:
                list_retorno.append(self.ListaArcos[i][0])
        if len(list_retorno) == 0:
            return -1
        return list_retorno


if __name__ == "__main__":
    grf = Grafo()
    while True:
        print("Escolha uma opção:")
        print("(M) - Mostra      (V) - Inserir Vértice      (A) - Inserin Arco     (B) - Buscar     (S) - Sair")
        escolha = input()
        if escolha == "M" or escolha == "m":
            grf.imprimeMatriz()
        elif escolha == "V" or escolha == "v":
            val = input("Digite o rótulo do vertice a inserir: ")
            grf.adicionaVertices(val)
        elif escolha == "A" or escolha == "a":
            rotulo = input("Digite o rótulo do arco: ")
            peso = int(input("Digite o peso do arco: "))
            rinicio = input("Digite o rótulo do vértice de início do arco: ")
            inicio = grf.localizaNo(rinicio)
            if inicio == -1:
                print("Vértice não encontrado. Cadastre o vértice primeiro.")
                input()
                continue
            rfim = input("Digite o rótulo do vértice de fim do arco: ")
            fim = grf.localizaNo(rfim)
            if fim == -1:
                print("Vértice não cadastrado. Cadastre o vértice primeiro")
                input()
                continue
            grf.adicionaArco(rotulo, peso, inicio, fim, rinicio, rfim)
        elif escolha == "s" or escolha == "S":
            break
        elif escolha == "B" or escolha == "b":
            escolha2 = input("Buscar nó ou arco? \n(N) - Nó      (A) - Arco")
            if escolha2 == "N" or escolha2 == "n":
                escolha2 = input("Digite o rótulo do nó: ")
                if grf.localizaNo(escolha2) == -1:
                    print("Nó não encontrado!")
                else:
                    print("Nó encontrado!")
            elif escolha2 == "A" or escolha2 == "a":
                escolha2 = input("Buscar por nome ou origem/destino? \n(N) - Nome         (O) - Origem/Destino")
                if escolha2 == "N" or escolha2 == "n":
                    nome = input("Digite o rótulo do arco a ser pesquisado:")
                    if grf.localizaArco(nome) == -1:
                        print("Arco não encontrado!")
                    else:
                        print("Arco encontrado!")
                elif escolha2 == "O" or escolha2 == "o":
                    escolha2 = input("Digite o nome do vértice de origem ou destino: ")
                    resposta = grf.localizaPorOrigemDestino(escolha2)
                    if resposta == -1:
                        print("O arco selecionado não foi encontrado!")
                    else:
                        print("O arco selecionado foi encontrado! Seu nome é ", end=" ")
                        print(resposta)

        else:
input("Entrada inválida. Pressione Enter")
