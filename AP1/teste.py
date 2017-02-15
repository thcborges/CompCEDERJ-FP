import random

def gera_vetor():
    vetor = []
    for indice in range(10):
        vetor.append(random.randint(1, 20))
    return vetor


def trocar(vals, i, j):
    aux = vals[i]
    vals[i] = vals[j]
    vals[j] = aux


def particiona(vals, inicio, fim):
    pivo = vals[inicio]
    i = inicio + 1
    j = fim
    while i < j:
        while i < fim and vals[i] < pivo:
            i += 1
        while j > inicio and vals[j] >= pivo:
            j -= 1
        if i < j:
            trocar(vals, i, j)
    if pivo > vals[j]:
        trocar(vals, inicio, j)
    return j


def quickSort(vals, inicio, fim):
    print(vals, inicio, fim)
    if inicio < fim:
        posPivo = particiona(vals, inicio, fim)
        quickSort(vals, inicio, posPivo-1)
        quickSort(vals, posPivo+1, fim)


def ordena(valores):
     quickSort(valores, 0, len(valores)-1)
     return None

lista = gera_vetor()
print(lista)
ordena(lista)
print(lista)