import random

# Subprogramas


def preencher(minimo, maximo, n):
    vetor = []
    for i in range(n):
        vetor.append(random.uniform(minimo, maximo))
    return vetor


def trocar(subvetor, x, y):
    temp = subvetor[x]
    subvetor[x] = subvetor[y]
    subvetor[y] = temp
    return None



def selecionarMenor(subvetor, inicio):
    local_menor = inicio
    for pos in range(inicio, len(subvetor)):
        if subvetor[pos] < subvetor[local_menor]:
            local_menor = pos
    return local_menor


def ordena(subvetor):
    for i in range(subvetor):
        menor = selecionarMenor(subvetor, i)
        trocar(subvetor, i, menor)
    return None


def verificaSetor(vetor, janela):
    tamanho = len(vetor) - janela
    soma = vetor[0]
    maior = 0
    for item in range(tamanho):
        temp = 0
        for s in range(janela):
            temp += vetor[item + s]
        if temp > soma:
            soma = temp
            maior = item
    subvetor = vetor[maior:maior+janela]
    ordena(subvetor)
    return None

# Programa Principal

valor_minimo = int(input("Informe o valor mínimo da faixa: "))
valor_maximo = int(input("Informe o valor máximo da faixa: "))
n = int(input("Informe a quantidade de valores a serem sorteados: "))
m = int(input("Informe o tamanho da janela: "))
vetor = preencher(valor_minimo, valor_maximo, n)
print(vetor)
verificaSetor(vetor, m)
print(vetor)