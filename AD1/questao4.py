import random

# Subprogramas


def preencher(minimo, maximo, quantidade):
    vetor = []
    for i in range(quantidade):
        vetor.append(random.randint(minimo, maximo))
    return vetor


def maior_menor(vetor):
    menor = None
    maior = None
    vetor.sort()
    for i in range(len(vetor)):
        if vetor.count(vetor[i]) == 1:
            menor = vetor[i]
            break
    for j in range(len(vetor)-1, -1, -1):
        if vetor.count(vetor[j]) == 1:
            maior = vetor[j]
            break
    return menor, maior


# Programa Principal
valor_minimo = int(input("Informe o valor inteiro mínimo da faixa: "))
valor_maximo = int(input("Informe o valor inteiro máximo da faixa: "))
n = int(input("Informe a quantidade de valores a serem sorteados: "))
vetor = preencher(valor_minimo, valor_maximo, n)
print(vetor)
extremos = maior_menor(vetor)
print(extremos)