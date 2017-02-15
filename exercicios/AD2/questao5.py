import struct  # Importando a biblioteca struct


# Subprogramas
# Função que retorna o valor encontrado no arquivo referenciado na posição
# pedida.
# Eescrita para facilitar a escrita e o entendimento do procedimento buscar
def consulta_posicao(arq, pos):
    arq.seek(pos * 4)
    return struct.unpack("i", arq.read(4))[0]


# Função que fará a busca binária em um arquivo previamente aberto retornando
# sua posição.
# A função começa estipulando os valores da primeira posição do arquivo e da última
# em seguida entra no laço indeterminado onde ocorrerá a busca pelo número desejado
# determina-se a variável meio a metade da soma da posição inicial e da posição final
# se o valor procurado estiver na posição meio, esta é retornada, caso contrário, se
# o número for menor que o apontado na posição meio a variável fim recebe meio - 1,
# sendo maior que num inicio recebe o valor de meio mais um. O laço será executado até
# inicio for maior que fim. Se essa situação ocorrer e o número não for encontrado,
# é porque o número não existe no arquivo, sendo então retornado o valor -1, que indica
# que o número não foi encontrado.
def buscar(arq, num):
    inicio = 0
    arq.seek(0, 2)
    fim = (int(arq.tell())//4) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if num == consulta_posicao(arq, meio):
            return meio
        elif num < consulta_posicao(arq, meio):
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1


# Programa Principal
# Pede-se para o usuário entrar com o nome do arquivo binário, abre-se ese arquivo
# e em seguida entra-se num laço onde o usuário vai digitar um número para ser buscado
# nesse arquivo e em seguida será exibido na saída padrão sua posição se esse foi
# encontrado ou um a mensagem informando que o arquivo não foi achado. Fecha-se o
# laço e termina-se o programa digitand -1.
nome_arquivo = input("Informe o nome do arquivo binário de números: ")
with open(nome_arquivo, "rb") as arquivo:
    n = int(input("Favor informar o valor a ser encontrado (-1 para sair): "))
    while n != -1:
        posicao = buscar(arquivo, n)
        if posicao == -1:
            print("O número não foi encontrado.\n")
        else:
            print("O número está na posição %d\n" % posicao)
        n = int(input("Favor informar o valor a ser encontrado (-1 para sair): "))
