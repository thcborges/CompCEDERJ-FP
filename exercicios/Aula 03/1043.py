t = input().split()

a = float(t[0])
b = float(t[1])
c = float(t[2])

if ((a + b > c) and (a + c > b) and (b + c > a)):
    medida = a + b + c
    print("Perimetro = %.1f" % medida, end="\n")
else:
    medida = ((a + b) * c) / 2
    print("Area = %.1f" % medida, end="\n")