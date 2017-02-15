triangulo = []

for i in range(26):
    linha = []
    for j in range(26):
        if j > i:
            valor = 0
        elif j == 0:
            valor = 1
        else:
            valor = triangulo[i - 1][j] + triangulo[i - 1][j - 1]
        linha.append(valor)
    triangulo.append(linha)

for linha in triangulo:
    for valor in linha:
        if valor != 0:
            print(valor, end=" ")
    print()

print("\n\n\n\n")
soma = 0
for i in range(12, 26):
    soma += triangulo[i][10]
print(soma)