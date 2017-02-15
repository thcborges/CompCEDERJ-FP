# Subprogramas
def imprime(num, prim):
    print("Primos entre 2 e", num, ":")
    contador = 0

    for candidato in range(2, num+1):
        if candidato in prim:
            print(candidato, end=" ")
            contador += 1
    print("\n", contador)


def eratostenes(num):
    resposta = set()
    vazio = set()
    crivo = set(range(2, num + 1))
    prox = 2
    arq = open("primos.txt", "w")

    while crivo != vazio:

        while not (prox in crivo):
            prox += 1

        resposta.add(prox)
        arq.write(str(prox) + "\n")
        j = prox

        while j <= num:
            crivo.discard(j)
            j += prox

    arq.close()

    return resposta


n = int(input("Digite o valor: "))
primos = eratostenes(n)
imprime(n, primos)
