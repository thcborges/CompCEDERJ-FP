import struct  # Importa-se a biblioteca struct
Numeros = struct.Struct("i f f")  # Defini-se o formato do registro do arquivo
TAM = Numeros.size  # Constante com o tamanho em bytes do espaço ocupado pelo registro

#
# Gostaria de deixar claro que  estipulei o primeiro número do arquivo binário
# como a posição 1. Poderia tê-la estipulado como posição 0 na linha 58
# conforme o comentário na referida linha.
#


# Subprogramas
# Procedimento que irá imprimir na saída padrão todas os números presente no arquivo
# Primeiramente obtém-se a quantidade total de registros do arquivo consultado
# apontando o cursor para o seu fim e em seguida dividindo pelo tamanho do registro
# Em seguida entra-se no laço que irá rodar a quantidade de registros presentes no
# arquivo pesquisado. Aponta-se o para a posição buscada no aruivo e desempacota
# a informação nela obtida.
# Por fim mostra na saída padrão os números obtidos em formato de tupla, commo foi
# especificado na questão
def imprimir(arq):
    tamanho = int(arq.seek(0, 2)) // TAM
    for l in range(tamanho):
        arq.seek(l * TAM)
        campo = Numeros.unpack(arq.read(TAM))
        print(l, "-", campo, end="\n\n")
    print("=====================")
    return None


# Procedimento que escreve no arquivo passado como referência um valor
# que também é passado como referência, na posição que também foi passada
# como referência.
# Esta é utilizada afim de facilitar a escrita e o entendimento
# do procedimento ordenar.
def escreve_posicao(arq, pos, valor):
    arq.seek(pos)
    arq.write(Numeros.pack(valor[0], valor[1], valor[2]))
    return None


# Função que retorna o valor encontrado no arquivo referenciado na posição
# pedida.
# Também foi escrita para facilitar a escrita e o entendimento
# do procedimento ordenar
def consulta_posicao(arq, pos):
    arq.seek(pos)
    return Numeros.unpack(arq.read(TAM))


# Procedimento que ordenará o setor de um arquivo.
# Recebe como parametros o arquivo aberto, a posição inicial e final
# que serão ordenadas.
# O procedimento começa entrando em um laço que acontecerá final - incio vezes + 1
# guardará a posição atual a ser verificada em atual
# e a colocará uma posição antes da que obtiver um registro maior que o seu.
def ordenar(arq, l, h):
    for k in range(l, h + 1):  # Com range(l+1, h+2) poderia estipular o primeiro número como posição 0.
        atual = consulta_posicao(arq, (k - 1) * TAM)
        posicao = k - 1

        while (posicao > l - 1) and consulta_posicao(arq, (posicao - 1) * TAM) > atual:

            escreve_posicao(arq,
                            posicao * TAM,
                            consulta_posicao(arq, (posicao - 1) * TAM))
            posicao -= 1

        escreve_posicao(arq, posicao * TAM, atual)
    return None


# Programa Principal
# Recebe o nome de um arquivo do usuário, uma posição inicial, e uma final
# para ordenar os valores presente.
# Em seguida abre o arquivo, imprime na saída padrão os valores presentes no
# arquivo ordena o setor estipulado e imprime novamente na saída padrão
# os registros contidos no arquivo.
nome_arquivo = input("Informe o nome do arquivo binário: ")
inicio = int(input("Informe a posição inicial do setor a ser processado: "))
fim = int(input("Informe a posição final do setor a ser processado: "))
with open(nome_arquivo, "r+b") as arquivo:
    imprimir(arquivo)
    ordenar(arquivo, inicio, fim)
    imprimir(arquivo)
