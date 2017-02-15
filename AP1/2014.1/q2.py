import random


# subprogramas
def gera_vetor():
    novo_vetor =[]
    for i in range(1000):
        novo_vetor.append(random.randint(0,90))
    return novo_vetor


def procura_primos(vetor):
    for j in range(len(vetor)):
        divisores = 0
        for k in range(2, vetor[j] + 1):
            if vetor[j] % k == 0:
                divisores += 1
        if divisores <= 1:
            print("Posição %d é primo, valor = %d" % (j, vetor[j]), end="\n")


def escreve_posicoes_primos(vetor):
    for l in range(2, len(vetor)):
        divisores = 0
        for m in range(2, l+1):
            if l % m == 0:
                divisores += 1
        if divisores <= 1:
            print("Posição %d, valor = %d" % (l, vetor[l]), end="\n")


# programa principal
vetor = gera_vetor()
print(vetor)
procura_primos(vetor)
escreve_posicoes_primos(vetor)