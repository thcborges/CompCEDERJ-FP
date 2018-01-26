
arquivo = open("teste.txt", "r")
linhas = arquivo.readline()
while linhas != "":
    print(linhas, end="")
    linhas = arquivo.readline()
arquivo.close()

dados = open("teste.txt", "w")
dados.write("Escrevendo\nPulando linha\n")
dados.close()

arquivo2 = open("teste.txt", "r")
for linha in arquivo2:
    print(linha, end="")
arquivo2.close()

dados2 = open("teste.txt", "a")
dados2.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n")
dados2.close()

arquivo3 = open("teste.txt", "r")
todas_as_linhas = arquivo3.readlines()
print(len(todas_as_linhas))
for linha in todas_as_linhas:
    print(linha, end="")
arquivo3.close()


quantas_linhas = int(input("Quantas linhas? "))
dados = open("teste.txt", "w")
for i in range(quantas_linhas):
    nova = input("Linha" + str(i + 1) + ": ")
    dados.write(nova + "\n")
dados.close()