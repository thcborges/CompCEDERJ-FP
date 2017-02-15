# subprogramas
def conta_apenas_digitos(texto):
    quantDigitos = 0
    for i in range(len(texto)):
        if texto[i] >= "0" and texto[i] <= "9":
            quantDigitos += 1
    if quantDigitos == len(texto):
        return True
    else:
        return False


def conta_digito(texto, numero):
    for i in range(len(texto)):
        for j in range(len(numero)):
            if texto[i] == str(j):
                numero[j] +=1
    return numero


def mais_digitado(numero):
    maior = numero[0]
    pos = []
    for i in range(1, len(numero)):
        if numero[i] > maior:
            maior = numero[i]
            pos.append(i)
    return pos


# Programa principal

palavra = input()
digitos = 0
numero = [0] * 10

while palavra != "tchau":
    if conta_apenas_digitos(palavra):
        digitos += 1
    numero = conta_digito(palavra, numero)
    palavra = input()

print(digitos, " entradas apenas com digitos")

for i in range(len(numero)):
    print(i, " foi digitado ", numero[i], " vezes")

mais_frequente = mais_digitado(numero)

print("O mais frequentemente digitado foi(foram): ", end=" ")
for j in range(len(mais_frequente)):
    if len(mais_frequente) == 1:
        print(mais_frequente[j])
    elif j == len(mais_frequente) - 2:
        print(mais_frequente[j], end=" e ")
    elif j == len(mais_frequente) - 1:
        print(mais_frequente[j])
