# Subprogramas
def preencher(listaElems, qtd, min, max):
    from random import randint
    for item in range(qtd):
        linha = []
        for c in range(qtd):
            linha.append(randint(min, max))
        listaElems.append(linha)
    return None


def remover_duplicatas(elems):
    for i in range(len(elems)):
        indice = 0
        while indice < len(elems):
            if elems.count(elems[i][indice]) == 1:
                indice += 1
            else:
                elems.remove(elems[i][indice])
    return None


def car(dados):
    return dados[0]


def cdr(dados):
    return dados[1:len(dados)]


def cons(item, dados):
    return [item] + dados


def eh_lista(item):
    return isinstance(item, list)


def eh_atomo(item):
    return not eh_lista(item)


def soma(dados):
    if dados == []:
        return 0
    else:
        if eh_atomo(car(dados)):
            return car(dados) + soma(cdr(dados))
        else:
            return soma(car(dados)) + soma(cdr(dados))


'''
qtdNumeros = int(input("A lista deve ter quantos valores?: "))
minimo = int(input("Menor valor da faixa: "))
maximo = int(input("Maior valor da faixa: "))
numeros = []
preencher(numeros, qtdNumeros, minimo, maximo)
print(numeros)
'''
numeros = []
preencher(numeros, 10, 0, 40)
print(numeros)
print(soma(numeros))
# remover_duplicatas(numeros)
print(numeros)

print(soma(numeros))