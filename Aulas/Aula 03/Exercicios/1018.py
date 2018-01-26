valor = int(input())
n1 = valor

n100 = n1 // 100
n1 = n1 % 100
n50 = n1 // 50
n1 = n1 % 50
n20 = n1 // 20
n1 = n1 % 20
n10 = n1 // 10
n1 = n1 % 10
n5 = n1 // 5
n1 = n1 % 5
n2 = n1 // 2
n1 = n1 % 2

print(valor)
print(n100, "nota(s) de R$ 100,00")
print(n50, "nota(s) de R$ 50,00")
print(n20, "nota(s) de R$ 20,00")
print(n10, "nota(s) de R$ 10,00")
print(n5, "nota(s) de R$ 5,00")
print(n2, "nota(s) de R$ 2,00")
print(n1, "nota(s) de R$ 1,00")