# AD2 - Questão 6

import struct
Registro = struct.Struct("i f f")


# Subprogramas

def imprimir(arq):
    arq.seek(0, 2)
    n = arq.tell() // Registro.size
    arq.seek(0, 0)
    for pos in range(n):
        campos = Registro.unpack(arq.read(Registro.size))
        print("(%d, %1.2f, %1.2f)" % campos)
    print()
    return None


def ordenar(arq, l, h):
    for i in range(l + 1, h + 1):
        j = i
        arq.seek((j - 1) * Registro.size, 0)
        camposAnterior = Registro.unpack(arq.read(Registro.size))
        camposAtual = Registro.unpack(arq.read(Registro.size))
        while j > l and camposAnterior > camposAtual:
            arq.seek((j - 1) * Registro.size, 0)
            arq.write(Registro.pack(camposAtual[0], camposAtual[1], camposAtual[2]))
            arq.write(Registro.pack(camposAnterior[0], camposAnterior[1], camposAnterior[2]))
            j = j - 1
            if j > l:
                arq.seek((j - 1) * Registro.size, 0)
                camposAnterior = Registro.unpack(arq.read(Registro.size))
    return None


# Programa Principal
nomeArq = input("Informe o nome do arquivo binário: ")
posInicial = int(input("Informe a posição inicial do setor a ser processado: "))
posFinal = int(input("Informe a posição final do setor a ser processado: "))

try:
    with open(nomeArq, "r+b") as arqBinario:
        imprimir(arqBinario)
        ordenar(arqBinario, posInicial, posFinal)
        imprimir(arqBinario)

except IOError:
    print("Erro ar abrir ou manipular o arquivo.")
