def escreve_linha(i, x):
    numeros = x
    for j in range(x - i):
        print(numeros**2, end=" ")
        numeros -= 1
    print()
    return None


n = int(input())
if n < 1:
    print("ERROR! o número deve ser maior ou igual a 1!")
else:
    for i in range(n):
        escreve_linha(i, n)
