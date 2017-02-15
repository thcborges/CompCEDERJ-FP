import random
# Funções
def gera_vetor():
    vet = []
    for i in range(50):
        vet.append(random.randint(1, 20))
    return vet


def busca_media(vet):
    soma = 0
    for item in range(len(vetor)):
        soma += vetor[item]
    return soma / len(vetor)


def maior_menor(vet, m):
    maior, menor = 0, 0
    for i in range(len(vetor)):
        if vetor[i] < m:
            menor += 1
        elif vetor[i] > m:
            maior += 1
    print(menor, " valores menores que a media.")
    print(maior, " valores maiores que a media.")


def nao_gerados(vet):
    for valor in range(1, 21):
        existe = 0
        for item in range(len(vet)):
            if vet[item] == valor:
                existe += 1
        if existe == 0:
            print(valor, " não existe no vetor")


def busca_maior(vet):
    maior = vet[0]
    for i in range(len(vet)):
        if vet[i] > maior:
            maior = vet[i]
    return maior


def busca_maiores(vet, maior):
    maiores = []
    for i in range(len(vet)):
        if vet[i] == maior:
            maiores.append(i)
    print("O maior valor foi encontrado na(s) posição(ões):", end=" ")
    for j in range(len(maiores)):
        if len(maiores) == 1:
            print (j)
        else:
            if j == len(maiores) - 2:
                print(j, end=" e ")
            if j == len(maiores) - 1:
                print(j)


# Programa Principal
vetor = gera_vetor()
media = busca_media(vetor)
print("Média dos valores gerados é ", media)
maior_menor(vetor, media)
nao_gerados(vetor)
maior = busca_maior(vetor)
print("Maior valor gerado foi ", maior)
busca_maiores(vetor, maior)
