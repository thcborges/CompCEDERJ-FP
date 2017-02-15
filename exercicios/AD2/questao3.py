import tempfile  # imporatando a biblioteca de arquivos temporáios


# Subprogramas
# Função que vai receber o nome de um arquivo e retornar um dicionário
# com uma lista de palavras e seu sinonimo.
# Primeiramente cria-se o dicionário, em seguida abre-se o arquivo, cujo
# nome foi forneciso pel usuário.
# Lê-se a primeira linha e então entra-se num laço que vai rodar até
# que a última linha do arquivo seja lida. Dentro do laço dividi-se as linhas a
# cada espaço dado e estipula-se a primeira palavra como chave e a segunda
# como valor da chave no dicionário.
# Por final fecha-se o arquivo aberto.
def ler_sinonimos(nome):
    dicio = dict()
    arquivo = open(nome, "r")

    linha = arquivo.readline()
    while linha != "":
        palavras = linha.split()
        dicio[palavras[0]] = palavras[1]

        linha = arquivo.readline()
    arquivo.close()
    return dicio


# Procedimento que irá fazer a substituição das linhas do arquivo original.
# Abre-se o arquivo original em modo de escrita e copia-se byte a byte cada
# caractere.
def troca_linhas(nome, temp):
    arq = open(nome, "w")
    i = 0
    temp.seek(i)

    while (temp.tell() != temp.seek(0, 2)) or arq.tell() != arq.seek(0, 2):
        temp.seek(i)
        arq.write(temp.read(1).decode('utf-8'))
        i += 1

    arq.close()

    return None


# Procedimento que processará o texto de um arquivo cujo nome foi fornecido pelo usuário e
# fará as permutações das palavras constantes no dicionário por seus sinonimos.
# Primeiramente abre o arquivo estipulado pelo usuário, em seguida cria-se um arquivo
# temporário. Em seguida lê-se a primeira linha do arquivo de texto e entra-se em um
# laço que irá rodar até o final do arquivo. Dentro deste laço divide-se a linha em um
# vetor e dentro de um laço determinado pela quantidade de itens do vetor, verifica-se
# cada palavra se ela existe no dicionário. Caso exista, ela é substituída  usando uma
# expressão regular que procurará a existência dessa palavra na string obtida com a
# leitura de uma linha do arquivo e substituirá essa pela referência obtida no dicionário
# uma vez para cada verificação da palavra.
# Assim que termina o laço, a string linha é codificada para binário e escrita no
# arquivo temporário. Por final é chamada a função que sobreescreverá o arquivo original.
def processar_texto(nome, sin):
    original = open(nome, "r")
    temp = tempfile.TemporaryFile()

    linha = original.readline()
    while linha != "":
        frase = linha.split()

        for palavra in frase:
            if palavra in sin.keys():
                from re import sub
                linha = sub(r'\b{0}\b'.format(palavra), sin[palavra], linha, 1)

        temp.write(linha.encode('utf-8'))
        linha = original.readline()

    original.close()
    troca_linhas(nome, temp)

    temp.close()

    return None


# Programa principal
# Pede ao usuário que insira o nome do arquivo de sinonimos e arquivo texto
# Em seguida registra o dicionário obtido com a função ler_sinonimos
# e processa o texto do arquivo texto.
sinonimos, texto = input("Informe o nome do arquivo de sinônimos: "), input("Informe o nome do arquivo com o texto: ")
dicionario = ler_sinonimos(sinonimos)
processar_texto(texto, dicionario)
