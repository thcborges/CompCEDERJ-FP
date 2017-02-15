# Subprogramas


def cria_arquivo_de_pontos(nome, qtd, min, max):
    from random import randint
    arq = open(nome, "w")
    for pos in range(qtd):
        arq.write(str(randint(min, max)) + " " + str(randint(min, max)) + "\n")
    arq.close()
    return None


def mostra(nome):
    arq = open(nome, "r")
    for pt in arq:
        print(pt, end="")
    arq.close()
    return None


def centroide(nome):
    arquivo = open(nome, "r")
    quantidade_de_pontos = 0
    soma_x = 0
    soma_y = 0
    for coordenada in arquivo:
        partes = coordenada.split()
        soma_x += float(partes[0])
        soma_y += float(partes[1])
        quantidade_de_pontos += 1
    arquivo.close()
    if quantidade_de_pontos == 0:
        print(arquivo.name, " - vazio!!!")
    else:
        print("Ponto calculado: (", soma_x / quantidade_de_pontos, ", ", soma_y / quantidade_de_pontos, ").")
    return None


# Programa Principal
for i in range(1):
    cria_arquivo_de_pontos("pontos.txt", 10, -10000000000, 10000000000)
    print(i, end=" ")
print()
mostra("pontos.txt")
centroide("pontos.txt")