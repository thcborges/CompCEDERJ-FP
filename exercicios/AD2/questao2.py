# Subprogramas


# Função que retornará um conjunto contendo as palavras a serem pesquisadas
# Primeiro cria-se o conjunto e abre-se o arquivo cujo nome foi fornecido pelo
# usuário. Em seguida lê-se  a primeira linha do arquivo texto e entra-se
# em uma laço que vai ler todas as linhas da questão até que esta esteja vazia.
# Dentro do laço, primeiro se divide toda a linha a cada espaço em um vetor.
# Em seguida entra-se em outro laço que rodará para cada item da lista. Dentro
# deste laço cada palavra é aadicionada ao conjunto criado.
# Por final o arquivo é fechado e o conjunto retornado.
def cria_conjunto(nome):
    conjunto = set()
    arquivo = open(nome, "r")

    linha = arquivo.readline()
    while linha != "":
        linha = linha.split("\n")
        sentenca = linha[0].split()

        for palavra in sentenca:
            conjunto.add(palavra)

        linha = arquivo.readline()

    arquivo.close()
    return conjunto


# Procedimento que verificará a existência de cada palavra em arquivo texto cujo nome
# é fornecido pelo usuário em um determinando conjunto.
# Primeiramente o arquivo é aberto e lê-se sua primeira linha, estipulando variável l
# para contar a quantidade de linhas lidas.
# Dentro de um laço de repetições indeterminadas, onde é estipulado seu fim quando a
# última linha do arquivo aberto for lida, divide-se a linha lida em um vetor e entra-se
# em um novo laço de repetiões determinado pela quantidade de palavras obtidas na linha.
# Dentro deste laço se verificará se cada palavra lida está dentro do conjunto passado,
# caso esteja, escreve-se na saída padrão a palavra determinada e sua posição na linha e
# palavra da linha conforme estipulado na questão.
# No final fecha o arquivo que foi aberto.
def verifica_palavras(nome, conjunto):
    arquivo = open(nome, "r")
    linha, l = arquivo.readline(), 1

    while linha != "":
        linha = linha.split("\n")
        palavras = linha[0].split()

        for p in range(len(palavras)):
            if palavras[p] in conjunto:
                print('("%s", %d, %d)' % (palavras[p], l, p+1), end="\n")

        linha = arquivo.readline()
        l += 1

    arquivo.close()
    return None


# Programa Principal
# Recebe do usuário o nome dos arquivos de referência e de pesquisa.
# Chama a função que vai ler o arquivo de referência e retornará um conjunto
# com susas palavras.
# Em seguida chama o procedimento que passa como referência o nome do arquivo de pesquisa
# e o conjunto obtido.
referencia = input()
pesquisa = input()
conjunto_referencia = cria_conjunto(referencia)
verifica_palavras(pesquisa, conjunto_referencia)
