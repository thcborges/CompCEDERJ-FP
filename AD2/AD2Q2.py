# AD2 - Questão 2

# Subprogramas

def produzConjunto(nArq):
    conjPals = set()
    bd = open(nArq, "r")
    for linha in bd:
        palavras = linha.split()
        for pal in palavras:
            conjPals.add(pal)
    bd.close()
    return conjPals


def escrevePalavrasContidasNoConjunto(nArqPesq, conjunto):
    posLinha = 0
    bdPesq = open(nArqPesq, "r")
    for linha in bdPesq:
        posLinha += 1
        palavras = linha.split()
        for posPalavra in range(len(palavras)):
            if palavras[posPalavra] in conjunto:
                print("(" + palavras[posPalavra] + ", " + str(posLinha) + ", " + str(posPalavra+1) + ")")
    bdPesq.close()
    return None


# Programa Principal
nomeArqReferencia = input("Diga nome arquivo de referência: ")
nomeArqPesquisa = input("Diga nome do arquivo a ser pesquisado: ")
conjPalavras = produzConjunto(nomeArqReferencia)
escrevePalavrasContidasNoConjunto(nomeArqPesquisa, conjPalavras)