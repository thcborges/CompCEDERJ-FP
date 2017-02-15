x = int(input())
y = int(input())

if x > y:
    aux = x
    x = y
    y = aux

if x % 2 == 0:
    x += 1
else:
    x += 2

soma = 0
for i in range(x, y, 2):
    soma += i

print(soma)