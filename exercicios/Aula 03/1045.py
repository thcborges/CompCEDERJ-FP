tri = input().split()
A = float(tri[0])
B = float(tri[1])
C = float(tri[2])
if B > A:
    aux = A
    A = B
    B = aux
if C > A:
    aux = A
    A = C
    C = aux
if C > B:
    aux = B
    B = C
    C = aux

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if ((A * A) == (B * B) + (C * C)):
        print("TRIANGULO RETANGULO")
    if ((A * A) > (B * B) + (C * C)):
        print("TRIANGULO OBTUSANGULO")
    if ((A * A) < (B * B) + (C * C)):
        print("TRIANGULO ACUTANGULO")
    if ((A == B) and (B == C)):
        print("TRIANGULO EQUILATERO")
    elif ((A == B) or (A == C) or (B == C)):
        print("TRIANGULO ISOSCELES")