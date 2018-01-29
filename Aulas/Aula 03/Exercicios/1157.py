n = int(input())
divisores = [div for div in range(1, n + 1) if n % div == 0]
for div in divisores:
    print(div)
