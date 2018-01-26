import struct
TAM = 43 # Constante definindo o tamanho do registro

# Subprogramas

def escrever(arq, matricula, nome, cr):
    arq.write(matricula.encode("utf-8"))
    arq.write(nome[:30].ljust(30, chr(0)).encode("utf-8"))
    arq.write(struct.pack("f", cr))


def ler(arq):
    matricula = arq.read(9).decode("utf-8")
    nome = arq.read(30).decode("utf-8").rstrip(chr(0))
    cr = struct.unpack("f", arq.read(4))[0]
    return matricula, nome, cr


# Programa Principal
with open("cr.bin", "w+b") as arq:
    escrever(arq, "213031001", "Alessandro", 5.4)  # chave 0
    escrever(arq, "114031012", "Dayana", 8.3)  # chave 1
    escrever(arq, "214031173", "Gustavo", 7.2)  # chave 2

    arq.seek(1*TAM)
    matricula, nome, cr = ler(arq)
    print("Matricula:", matricula, "Nome:", nome, "CR:", cr)