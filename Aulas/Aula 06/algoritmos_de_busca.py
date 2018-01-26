# encoding: utf-8
# author: Thiago da Cunha Borges


# Subprogramas
def preencher(valores):
    for ind in range(len(valores)):
        valores[ind] = int(input("Elemento[" + str(ind) + "] = "))


def busca_elementos_for(valores, procurado):
    for indice in range(len(valores)):
        if valores[indice] == procurado:
            return indice
    return -1


def busca_elementos_while(valores, procurado):
    indice = 0
    while indice < len(valores):
        if valores[indice] != procurado:
            indice += 1
        else:
            return indice
    return -1


def busca_elemento_while_sentinela(valores, procurado):
    valores.append(procurado)
    indice = 0
    while valores[indice] != procurado:
        indice += 1
    if indice == len(valores) - 1:
        del valores[-1]
        return -1
    else:
        return indice


def busca_binaria(valores, procurado):
    inicio = 0
    fim = len(valores) - 1
    meio = (inicio + fim) // 2
    while inicio < fim and procurado != valores[meio]:
        if procurado > valores[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1
        meio = (inicio + fim) // 2
    if procurado != valores[meio]:
        return -1
    else:
        return meio


def escrever_resposta(valor, pos):
    if pos < 0:
        print("{} não foi encontrado".format(valor))
    else:
        print("{} foi encontrado na posição {}".format(valor, pos))


# Programa Principal
numeros = [0] * 10  # Cria um vetor de zeros com tamanho 10
preencher(numeros)

# dado: o elemento a ser procurado
dado = int(input("Escolha o valor a ser procurado: "))

# onde: o local no vetor onde foi encontrado ou -1 se não encontrado
onde = busca_elementos_for(numeros, dado)

escrever_resposta(dado, onde)
