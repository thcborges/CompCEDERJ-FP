import tempfile

temp = tempfile.TemporaryFile()

palavra = "Teste de escrita em arquivo temporário\n"

bloco = palavra.encode('utf-8')
temp.write(palavra)

with open("texto.txt", "a+b") as file:
    i = 0
    temp.seek(i)
    while temp.tell() != temp.seek(0, 2):
        temp.seek(i)
        print(temp.read(), end="")
        temp.seek(i)
        file.write(temp.read(1))
        i += 1
