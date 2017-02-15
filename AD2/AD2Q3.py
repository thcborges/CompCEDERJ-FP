# AD2 - Questão 3

# Subprogramas

def lerSinonimos(nomeArq):
    sinonimos = dict()

    arq = open(nomeArq, "r")
    for linha in arq:
        par = linha.split()
        sinonimos[par[0]] = par[1]
    arq.close()

    return sinonimos


def processarTexto(nomeArq, sinonimos):
    arq = open(nomeArq, "r")
    tmp = open("temp.txt", "w")
    for linha in arq:
        for palavra in linha.split():
            sinonimo = sinonimos.get(palavra)
            if sinonimo == None:
                tmp.write(palavra)
            else:
                tmp.write(sinonimo)
            tmp.write(" ")
        tmp.write("\n")
    tmp.close()
    arq.close()

    tmp = open("temp.txt", "r")
    arq = open(nomeArq, "w")
    for linha in tmp:
        arq.write(linha)
    arq.close()
    tmp.close()


# Programa Principal
nomeArqSinonimos = input("Informe o nome do arquivo de sinônimos: ")
nomeArqOriginal = input("Informe o nome do arquivo com o texto: ")

pares = lerSinonimos(nomeArqSinonimos)
processarTexto(nomeArqOriginal, pares)
