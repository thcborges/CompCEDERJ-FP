t = int(input())
for i in range(t):
    lados = input().split()
    n = int(lados[0])
    m = int(lados[1])
    radar = (n // 3) * (m // 3)
    print(radar)