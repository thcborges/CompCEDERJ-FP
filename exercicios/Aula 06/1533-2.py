while True:
    n = int(input())
    if n == 0:
        break
    suspeito = input().split()
    for i in range(len(suspeito)):
        suspeito[i] = int(suspeito[i])
    sus = suspeito[:]
    sus.sort()
    for j in range(len(suspeito)):
        if sus[len(sus) - 2] == suspeito[j]:
            print(j + 1)