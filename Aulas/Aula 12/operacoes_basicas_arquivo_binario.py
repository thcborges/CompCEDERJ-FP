import struct
# Subprogramas
def mostrar_valores(arq, n):
    print("Os primeiros valores contidos no arquivo são:")
    arq.seek(0)
    for k in range(0, n):
        print(struct.unpack("i", arq.read(4))[0])
# Abertura de arquivo para leitura, seguido pelo fechamento
try:
    arq = open("arquivo.bin", "rb")
    salva = arq.read()
    print("O arquivo está aberto")
    arq.close()
except IOError:
    print("Erro ao abrir o arquivo")


# "rb" => abre um arquivo binério para leitura. O arquivo deve existir previamente.

# "wb" => abre um arquivo para escrita. Se o arquivo não existe ele é criado, mas se existir terá todos os seus dados
# sobreescritos

# "r+b" => abre uma arquivo existente para leitura e escrita. O arquivo deve existir previamente.

# "r+b" => abre um arquivo para escrita e leitura, se esse arquivo não existir esse será criado, se existir seus dados
# serão sobreescritos

# "a+b" => abre um arquivo no modo append. Caso o arquivo não exista esse será criado, mas se existir, seus dados serão
# mantidos e o novo conteúdo será adicionado ao final do arquivo


# with as
# simplifica o código de abertura do arquivo.
# Esse comando também garante o fechamento do arquivo


try:
    with open("arquivo.bin", "wb") as arq:
        texto = "Sou aluno do CEDERJ"
        bloco = texto.encode()
        arq.write(bloco)
except IOError:
    print("Erro ao abrir ou ao manipular o arquivo.")


try:
    with open("arquivo.bin", "rb") as arq:
        byte = arq.read(1)
        while byte != b"":
            print(arq.tell(), byte)
            byte = arq.read(1)
except IOError:
    print("Erro ao abrir o arquivo.")


# Escrita de um string binarizado no arquivo


try:
    with open("arquivo.bin", "wb") as arq:
        print("Arquivo foi aberto")
        # Faça alguma manipulação no arquivo
        for i in range(1, 10):
            bloco = struct.pack("i", (i**i))
            arq.write(bloco)
        bloco = struct.pack("d", 99.5)
        arq.write(bloco)
except IOError:
    print("Erro ao abrir o arquivo.")


try:
    with open("Arquivo.bin", "rb") as arq:
        inteiro = struct.unpack("i", arq.read(4))[0]
        real = struct.unpack("d", arq.read(8))[0]
        print("Valor inteiro:", inteiro, "Valor real:", real)
except IOError:
    print("Erro ao abrir ou ao manipular o arquivo.")


# Copiando arquivos binários
try:
    with open("arquivo.bin", "rb") as entrada:
        with open("copia.bin", "wb") as saida:
            byte = entrada.read(1)
            while byte != b"":
                saida.write(byte)
                byte = entrada.read(1)
except IOError:
    print("Erro manipulando aruivos")


try:
    with open("arquivo.bin", "wb") as arq:
        arq.write(salva)
except IOError:
    print("Erro")


try:
    with open("arquivo.bin", "rb") as arq:
        bloco = arq.read(16)
        texto = bloco.decode("utf-8")
        print(texto)
except IOError:
    print("Erro ao abrir o arquivo")

# Verificando o avanço do cursor de leitura
try:
    with open("copia.bin", "rb") as arq:
        pos = arq.tell()
        print("O cursor está no endereço", pos)
        x = struct.unpack("i", arq.read(4))[0]
        pos = arq.tell()
        print("Após ler 4 bytes, ele foi para o endereço", pos)
except IOError:
    print("Erro ao abrir o arquivo")


# Verificando o tamanho do arquivo
try:
    with open("arquivo.bin", "rb") as arq:
        arq.seek(0, 2)
        tam = arq.tell()
        print("O arquivo possui", tam*8, "bits")
except IOError:
    print("Erro ao abrir o arquivo")


# Acesso randômico para leitura do conteúdo do arquivo
try:
    with open("copia.bin", "rb") as arq:
        print("Os 10 primeiros valores inteiros armazenados são:")
        for x in range(0, 10):
            print(struct.unpack("i", arq.read(4))[0])

        print("\nDa posição atual, voltarei o cursor para reler os 5 ultimos valores")
        arq.seek(-(4*5), 1)
        for x in range(0, 5):
            print(struct.unpack("i", arq.read(4))[0])
        print("Agora voltarei para o incio do arquivo para reler o primeiro valor")
        arq.seek(0)
        print(struct.unpack("i", arq.read(4))[0])
except IOError:
    print("Erro ao abrir ou ao manipular o arquivo")


try:
    with open("numeros.bin", "w+b") as arq:
        print('Escrever os valores inteiros de 1 a 5 no arquivo')
        for x in range(1,6):
            arq.write(struct.pack("i", x))
        mostrar_valores(arq, 5)
        print("Substituir o segundo valor inteiro contido no arquivo por 99")
        arq.seek(4)
        arq.write(struct.pack("i", 99))
        mostrar_valores(arq, 5)
except IOError:
    print("Erro manipulando arquivo")