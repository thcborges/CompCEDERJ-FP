print("Bem-vindo ao programa para cálculo de CR\n")

soma = 0.0
chTotal = 0

ind = 1
print("Carga horária %d (inorme 0 para encerrar): " % ind, end="")
ch = int(input())

while ch != 0:
    print("Nota final %d: " % ind, end="")
    nota = float(input())

    soma += ch * nota
    chTotal += ch

    ind += 1
    print("\nCarga horaria %d (informe 0 para encerrar): " % ind, end="")
    ch = int(input())

if chTotal != 0:
    cr = soma / chTotal
else:
    cr = 0

print("\nSeu CR é %1.2f." % cr)