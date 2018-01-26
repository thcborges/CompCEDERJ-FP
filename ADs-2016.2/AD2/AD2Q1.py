# AD2 - Questão 1

# Subprogramas

def car(lis):
    return lis[0]


def cdr(lis):
    return lis[1:]


def cons(x, lis):
    return [x] + lis


def obterSetor(lista, inicio, fim):
    if lista == [] or inicio > fim or inicio < 1:
        return []
    else:
        if inicio > 1:
            return obterSetor(cdr(lista), inicio - 1, fim - 1)
        else:
            return cons(car(lista), obterSetor(cdr(lista), inicio, fim - 1))


def rodar(lista, nVezes):
    if lista == [] or nVezes == 0:
        return lista
    else:
        if nVezes < 0:
            return rodar(insereFinal(car(lista), cdr(lista)), nVezes + 1)
        else:
            return rodar(cons(pegaUltimo(lista), tiraUltimo(lista)), nVezes - 1)


def insereFinal(x, lista):
    if lista == []:
        return cons(x, [])
    else:
        return cons(car(lista), insereFinal(x, cdr(lista)))


def pegaUltimo(lista):
    if lista == []:
        return None
    else:
        if cdr(lista) == []:
            return car(lista)
        else:
            return pegaUltimo(cdr(lista))


def tiraUltimo(lista):
    if lista == [] or cdr(lista) == []:
        return []
    else:
        return cons(car(lista), tiraUltimo(cdr(lista)))


def ordenar(lista):
    if lista == []:
        return []
    else:
        return insereOrdenado(car(lista), ordenar(cdr(lista)))


def insereOrdenado(x, lista):
    if lista == [] or x < car(lista):
        return cons(x, lista)
    else:
        return cons(car(lista), insereOrdenado(x, cdr(lista)))


# Programa Principal
dadosTeste1 = ["ana", "maria", "chico", "igor", "juca"]
dadosTeste2 = [10, 2, 5, 13, 26, 4, 2, 9, 33, 18, 6, 100, 12, 17]

print("AD2Q1.a teste 1:", obterSetor(dadosTeste1, 2, 4))
print("AD2Q1.a teste 2:", obterSetor(dadosTeste1, 4, 1))
print("AD2Q1.a teste 3:", obterSetor(dadosTeste2, 5, 9))
print("AD2Q1.a teste 4:", obterSetor(dadosTeste2, 1, 19))
print()
print("AD2Q1.b teste 1:", rodar(dadosTeste1, 2))
print("AD2Q1.b teste 2:", rodar(dadosTeste1, -2))
print("AD2Q1.b teste 3:", rodar(dadosTeste2, 5))
print("AD2Q1.b teste 4:", rodar(dadosTeste2, -15))
print()
print("AD2Q1.c teste 1:", ordenar([]))
print("AD2Q1.c teste 2:", ordenar(dadosTeste1))
print("AD2Q1.c teste 3:", ordenar(dadosTeste2))
