x, y = int(input()), int(input())
if x > y:
    n, x = -1, x - 1
else:
    n, y = 1, y + 1
impares = [impar for impar in range(x, y, n) if impar % 2 == 1]
print(sum(impares))
