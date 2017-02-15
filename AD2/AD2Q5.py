# AD2 - Questão 5

# Subprogramas

def buscar(arq, num):
    import struct

    arq.seek(0, 2)
    tam = arq.tell()

    esq = 0
    dir = (tam // 4) - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        arq.seek(meio * 4, 0)
        atual = struct.unpack("i", arq.read(4))[0]
        if atual < num:
            esq = meio + 1
        elif atual > num:
            dir = meio - 1
        else:
            return meio

    return -1


# Programa Principal
nomeArq = input("Informe o nome do arquivo binário de números: ")

try:
    with open(nomeArq, "rb") as arqNumeros:
        valor = int(input("Favor informar o valor a ser encontrado (-1 para sair): "))
        while valor != -1:
            pos = buscar(arqNumeros, valor)
            if pos != -1:
                print("O número está na posição %d." % pos)
            else:
                print("O número não foi encontrado")
            valor = int(input("Favor informar o valor a ser encontrado (-1 para sair): "))
except IOError:
    print("Erro ar abrir ou manipular o arquivo.")
