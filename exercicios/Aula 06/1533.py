n = int(input())
while n != 0:
    suspeiitos = input().split()
    if int(suspeiitos[0]) > int(suspeiitos[1]):
        maior, segundo_maior, pos = int(suspeiitos[0]), int(suspeiitos[1]), 2
    else:
        maior, segundo_maior, pos = int(suspeiitos[1]), int(suspeiitos[0]), 1
    for i in range(2, len(suspeiitos)):
        suspeiitos[i] = int(suspeiitos[i])
        if suspeiitos[i] > maior:
            maior = suspeiitos[i]
        elif suspeiitos[i] > segundo_maior:
            segundo_maior = suspeiitos[i]
            pos = i + 1
    print(pos)
    n = int(input())