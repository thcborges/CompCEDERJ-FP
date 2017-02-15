arq = open("primos.txt", "w")
print(2)
arq.write("2\n")
for n in range(3, 1000000000, 2):
    i = 2
    div = True
    while i <= (n // 2) - 1:
        if n % i == 0:
            div = False
        i += 1
    if div:
        texto = str(n) + "\n"
        arq.write(texto)
        print(n, "  ||", end="  ")

arq.close()
