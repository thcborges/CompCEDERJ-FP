# Subprogramas
def lerSinonimos(nome):
    dicionario = {}
    arquivo = open(nome, "r")
    while True:
        linha = arquivo.readline()
        if linha == "":
            break
        linha = linha.split()
        dicionario[linha[0]] = linha[1]
    return dicionario


def processarTexto(nomeArq, sinonimos):
    arquivoTemporario = open('Temp.txt', 'w+')
    arquivo_leitura = open(nomeArq, 'r+')
    sinonimos = lerSinonimos(sinonimos)
    while True:
        linha = arquivo_leitura.readline()
        if linha == "":
            break
        else:
            palavras = linha.split()
            for item in range(len(palavras)):
                if linha[item] in sinonimos:
                    from re import sub
                    sub("\\b" + palavras[item] + "\\b", sinonimos[palavras[item]], linha)
            arquivoTemporario.write(linha)
    arquivoTemporario.seek(0)
    arquivo_leitura.seek(0)
    while True:
        linha = arquivoTemporario.readline()
        if linha == "":
            break
        else:
            arquivo_leitura.write(linha)
    arquivo_leitura.close()
    arquivoTemporario.close()
    return None


# Programa principal
sinonimos = str(input("Informe o nome do arquivo de sinônimos: "))
texto = str(input("Informe o nome do arquivo de texto: "))
processarTexto(texto, sinonimos)