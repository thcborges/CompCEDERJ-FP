import struct
Aluno = struct.Struct("i 30s f")  # Criar a struct com o formato do registro


# Subprogramas
def escrever(file, mat, name, nota):
    file.write(Aluno.pack(mat, name.encode("utf-8"), nota))


def ler(file):
    campos = Aluno.unpack(file.read(Aluno.size))
    return campos  # campos[0], campos[1].decode("utf-8").rstrip(chr(0)), campos[2]


# Programa principal
with open("cr.bin", "w+b") as arq:
    arq.seek(0, 2)
    escrever(arq, 213031001, "Alessandro", 5.4)  # chave 0
    escrever(arq, 114031012, "Dayana", 8.3)  # chave 1
    escrever(arq, 214031173, "Gustavo", 7.2)  # chave 2
    arq.seek(0)
    n = int(arq.seek(0, 2)) // Aluno.size

    for i in range(n):
        arq.seek(i * Aluno.size)
        print(ler(arq))
        # matricula, nome, cr = ler(arq)
        # print("Matrícula:", matricula, "\nNome:", nome, "\nCR:", cr, "\n")
