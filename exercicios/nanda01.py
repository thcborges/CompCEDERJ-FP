trinta_tres = 0
seis = 0
tres = 0
for i in range(12):
    trinta_tres += (100 ** i) * 33
    seis += (10 ** i) * 6
    tres += (10 ** i) * 3
    resultado = trinta_tres - seis
    print("%dº) %d - %d = %d" % (i + 1, trinta_tres, seis, resultado), end=" ")
    resultado /= tres
    print(": %d = %d" % (tres, resultado), end="\n\n")