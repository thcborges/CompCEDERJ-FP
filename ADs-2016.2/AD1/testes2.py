import random #Para importar a biblioteca para gerar números aleatórios


# operção que troca o conteudo de duas celulas do vetor
def trocar(vals, posX, posY):
    temp = vals[posX]
    vals[posX] = vals[posY]
    vals[posY] = temp
    return None


# operação que encontra e retorna o local do menos elemento do vetor
# conseiderando as células a partir de um dado inicio
def selecionarMenor(vals, inicio):
    localMenor = inicio
    for pos in range(inicio + 1, len(vals)):
        if vals[pos] < vals[localMenor]:
            localMenor = pos
    return localMenor


# Metodo de seleção
def ordenar(valores):
    for ind in range(len(valores) - 1):
        menor = selecionarMenor(valores, ind)
        trocar(valores, ind, menor)

        return None


def numList():
#solicitar os valores minimos e máximos
    minValor = int(input('Informe o valor inteiro mínimo da faixa:'))
    maxValor = int(input('Informe o valor inteiro máximo da faixa:'))
    quantidadeValor = int(input('Infome a quantidade de valores a serem sorteados:'))
    janela = int(input('Infome o tamanho da janela:'))
    vetor = []

    for n in range(quantidadeValor):
       number = random.uniform(minValor, maxValor)#aleatório entre as faxias de valores máximos e mínimos
       vetor.append(number)

    print(vetor)

    soma = vetor[0]
    maior = 0
    verificar = len(vetor) - janela
    temp = 0
    for i in range(verificar):
        soma = 0
        for j in range(janela):
            soma += vetor[i + j]
        if temp > soma:
            soma = temp
            maior = i
    subvetor = vetor[maior:maior+janela]
    ordenar(subvetor)
    for k in range(janela):
        vetor[k + maior] = subvetor[k]
    print(vetor)



numList()