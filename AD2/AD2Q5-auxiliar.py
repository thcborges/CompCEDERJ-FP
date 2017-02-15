# AD2 - Questão 5 - Programa auxiliar (a escrita e entrega deste programa não faz parte da avaliação)

import struct

nomeArq = input("Informe o nome do arquivo binário de números: ")
numeros = [2, 6, 13, 25, 78, 99, 108, 109, 110, 567];

try:
    with open(nomeArq, "wb") as arq:
        for num in numeros:
            arq.write(struct.pack("i", num))
except IOError:
    print("Erro ar abrir ou manipular o arquivo.")
