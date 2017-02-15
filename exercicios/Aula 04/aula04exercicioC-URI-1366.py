while True:
    teste = int(input())
    if teste == 0:
        break
    lados = 0
    while teste > 0:
        palitos = input().split()
        despresa = int(palitos[1]) % 2
        lados = lados + int(palitos[1]) - despresa
        teste = teste - 1
    print(lados//4)