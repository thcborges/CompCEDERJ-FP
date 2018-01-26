n = int(input())
x = input().split()
menor = int(x[0])
pos = 0
for i in range(1, len(x)):
    x[i] = int(x[i])
    if x[i] < menor:
        menor = x[i]
        pos = i
print("Menor valor: %d\nPosicao: %d" % (menor, pos), end="\n")