# AD2 - Questão 6 - Programa auxiliar (a escrita e entrega deste programa não faz parte da avaliação)

import struct
Registro = struct.Struct("i f f")

nomeArq = input("Informe o nome do arquivo binário: ")
registros = [(5, 3.6, 4.5), (10, 2.3, 1.0), (5, 10.0, 9.0), (9, 8.0, 9.0), (4, 7.8, 9.9), (8, 10.0, 11.0), (12, 12.0, 12.0), (0, 5.0, 3.4), (-8, 6.0, 8.0), (-6, 9.3, 2.4)];

try:
    with open(nomeArq, "wb") as arq:
        for campos in registros:
            arq.write(Registro.pack(campos[0], campos[1], campos[2]))
except IOError:
    print("Erro ar abrir ou manipular o arquivo.")
