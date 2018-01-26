import struct
NumeroBin = struct.Struct('<i')


# Sub-Programas
def buscar(arq, num):
    arq.seek(0, 2)  # Coloca o cursor na última posição do arquivo
    tamanho = arq.tell()  # passa para a variável tamanho o valor da última posição do arquivo
    quantNumeros = int(tamanho / 4)  # Determina a quantidade de números inscritos no arquivo
    arq.seek(0)  # volta para o início do arquivo
    pos = -1

    for i in range(quantNumeros):
        arq.seek(4 * i, 0)
        atual = NumeroBin.unpack(arq.read(4))[0]
        if atual == num:
            pos = i
            return pos
    return pos


# Programa Principal
try:
    arqNumeros = input("Informe o nome do arquivo binário de números: ")
    with open(arqNumeros, "rb") as arquivo:
        numero = int(input("Favor informar o valor a ser encontrado (-1 para sair): "))
        while numero != -1:
            posicao = buscar(arquivo, numero)
            if posicao > 0:
                print("O número está na posição %d" % posicao)
            else:
                print("O número não foi encontrado.")
            numero = int(input("Favor informar o valor a ser encontrado (-1 para sair): "))
except IOError:
    print("Erro ao abrir ou manipular o arquivo.")
