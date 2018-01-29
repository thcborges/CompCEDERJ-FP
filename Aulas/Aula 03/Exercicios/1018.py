valor, cedulas, notas = int(input()), [100, 50, 20, 10, 5, 2, 1], [0] * 7
print(valor)
for c in range(7):
    notas[c] = valor // cedulas[c]
    valor %= cedulas[c]
for n in range(7):
    print('{} nota(s) de R$ {},00'.format(notas[n], cedulas[n]))
