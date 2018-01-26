# Subprogramas
def car(dados):
    return dados[0]


def cdr(dados):
    return dados[1:len(dados)]


def cons(item, dados):
    return [item] + dados


def obterSetor(lista, inicio, fim):
    if lista == []:
        return []
    else:
        if fim < inicio:
            return []
        else:
            if inicio > 1:
                return obterSetor(cdr(lista), inicio - 1, fim - 1)
            else:
                return cons(car(lista), obterSetor(cdr(lista), inicio, fim - 1))


def rodar(lista, nVezes):
    if nVezes == 0:
        return lista
    else:
        if nVezes > 0:
            if lista == []:
                return []
            else:
                if cdr(lista) == []:
                    return [car(lista)]
                else:
                    # if
                    return rodar()




# Programa Principal

lista1 = ["ana", "maria", "chico", "igor", "juca"]
lista2 = [10, 2, 5, 13, 26, 4, 2, 9, 33, 18, 6, 99, 12, 17]

print(obterSetor(lista1, 2, 4))
print(obterSetor(lista1, 4, 1))
print(obterSetor(lista2, 4, 9))
print(obterSetor(lista2, 15, 19))
print("=====================")
'''
print(rodar(lista1, 2))
print(rodar(lista1, -2))
print(rodar(lista2, 4))
print(rodar(lista2, -15))
print("=====================")
''''''
print(ordenar(lista1))
print(ordenar(lista2))
'''