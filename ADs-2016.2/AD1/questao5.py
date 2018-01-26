import random  # Importa a biblioteca random

# Subprogramas


def constroiMatriz(linha, coluna, minimo, maximo):
    matriz = []
    for l in range(linha):
        matriz.append([])
        for c in range(coluna):
            matriz[l].append(random.randint(minimo, maximo))
    return matriz


def largura_coluna(matriz):
    n = len(matriz)
    m = len(matriz[0])
    menor = 0
    maior = 0
    for l in range(n):
        for c in range(m):
            if menor > matriz[l][c]:
                menor = matriz[l][c]
            elif matriz[l][c] > maior:
                maior = matriz[l][c]
    menor = algarismos(menor)
    maior = algarismos(maior)
    if maior > menor:
        return maior
    else:
        return menor


def algarismos(n):
    if n < 0:
        casas = 2
        while n < -9:
            casas += 1
            n //= 10
        return casas
    else:
        casas = 1
        while n > 9:
            casas += 1
            n //= 10
        return casas


def imprime_matriz(matriz):
    tamanho_coluna = largura_coluna(matriz)
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            for espaco in range(tamanho_coluna - algarismos(matriz[l][c])):
                print(" ", end="")
            print(" %d" % matriz[l][c], end="")
        print()
    print()
    return None


def soma(matriz1, matriz2):
    if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
        matriz_soma = []
        for l in range(len(matriz1)):
            matriz_soma.append([])
            for c in range(len(matriz1[l])):
                matriz_soma[l].append(matriz1[l][c] + matriz2[l][c])
        imprime_matriz(matriz_soma)
    else:
        print("Não é possível somar matrizes de dimensões diferentes.")


def produto(matriz1, matriz2):
    if len(matriz1[0]) == len(matriz2):
        matriz_produto = []
        for l in range(len(matriz1)):
            matriz_produto.append([])
            for c in range(len(matriz2[0])):
                temp = 0
                for v in range(len(matriz2)):
                    temp += matriz1[l][v] * matriz2[v][c]
                matriz_produto[l].append(temp)
        imprime_matriz(matriz_produto)
    else:
        print("Não é possível multiplicar matrizes se a quantidade de colunas da primeira é diferente da quantidade de linhas da segunda.")

# Programa Principal

valor_minimo = int(input("Informe o valor inteiro mínimo da faixa: "))
valor_maximo = int(input("Informe o valor inteiro máximo da faixa: "))
linha1, coluna1 = int(input("Informe a quantidade de linhas da primeira matriz: ")), int(input("Informe a quantidade de colunas da primeira matriz: "))
linha2, coluna2 = int(input("Informe a quantidade de linhas da segunda matriz: ")),int(input("Informe a quantidade de colunas da segunda matriz: "))
matriz1 = constroiMatriz(linha1, coluna1, valor_minimo, valor_maximo)
matriz2 = constroiMatriz(linha2, coluna2, valor_minimo, valor_maximo)
imprime_matriz(matriz1)
imprime_matriz(matriz2)
soma(matriz1, matriz2)
produto(matriz1, matriz2)
