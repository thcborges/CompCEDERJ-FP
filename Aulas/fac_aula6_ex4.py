cont = 0
for i in range(391, 1000):
    c = i // 100
    d = (i % 100) // 10
    u = i % 10
    cont += 1
    if c == 1 or c == 3 or c == 5 or d == 1 or d == 3 or d == 3 or u == 1 or u == 3 or u == 5 or c == d or c == u or d == u:
        cont -= 1


print(cont)