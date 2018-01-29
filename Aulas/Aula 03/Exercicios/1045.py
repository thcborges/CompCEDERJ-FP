lados = list(map(float, input().split()))
maior = max(lados)
lados.remove(maior)
menor = min(lados)
lados.remove(menor)
if maior >= lados[0] + menor:
    print("NAO FORMA TRIANGULO")
else:
    if (maior ** 2) == (lados[0] ** 2) + (menor ** 2):
        print("TRIANGULO RETANGULO")
    elif (maior ** 2) > (lados[0] ** 2) + (menor ** 2):
        print("TRIANGULO OBTUSANGULO")
    elif (maior ** 2) < (lados[0] ** 2) + (menor ** 2):
        print("TRIANGULO ACUTANGULO")
    if maior == lados[0] and lados[0] == menor:
        print("TRIANGULO EQUILATERO")
    elif maior == lados[0] or maior == menor or menor == lados[0]:
        print("TRIANGULO ISOSCELES")
