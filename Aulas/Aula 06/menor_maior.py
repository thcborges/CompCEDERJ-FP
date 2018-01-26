# encoding: utf-8
# author: Thiago da Cunha Borges


# Subprogramas
def preencher(valores):
    for ind in range(len(valores)):
        valores[ind] = int(input("Elemento[" + str(ind) + "] = "))


def busca_maior_menor_elementos(valores):
    menor = valores[0]
    maior = valores[0]
    for valor in valores:
        if menor > valor:
            menor = valor
        elif maior < valor:
            maior = valor
    return [menor, maior]


def escrever(infos):
    print("O menor elemento = {}\nO maior elemento = {}".format(infos[0], infos[1]))


# Programa Principal
numeros = [0] * 10  # Cria um vetor de zeros com tamanho 10
preencher(numeros)
extremos = busca_maior_menor_elementos(numeros)
escrever(extremos)
