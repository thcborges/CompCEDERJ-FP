import struct


def imprimir(arq):
    tamanho = int(arq.seek(0, 2)) // 4
    arq.seek(0)
    for l in range(tamanho):
        arq.seek(l * 4)
        campo = struct.unpack("i", arq.read(4))[0]
        print(l, " - ", campo, end="\n")
    return None


with open("ab.bin", "w+b") as file:
    for i in range(128):
        x = struct.pack("i", i)
        file.write(x)
    imprimir(file)
