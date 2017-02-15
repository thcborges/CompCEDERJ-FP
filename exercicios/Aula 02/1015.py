valor1 = input().split()
valor2 = input().split()

x1 = float(valor1[0])
y1 = float(valor1[1])
x2 = float(valor2[0])
y2 = float(valor2[1])

distancia = (((x2 - x1)**2) + ((y2-y1)**2)) ** (1/2)

print("%.4f" %distancia, end="\n")