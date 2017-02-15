mercado = [["pera", 100, 4.9],
           ["manga", 20, 3.9],
           ["uva", 30, 5.9],
           ["caju", 15, 3.5]]
print(mercado)

mercado[1][2] /= 2
print(mercado)

mercado[3][1] -= 10
print(mercado)

mercado.remove(["uva", 30, 5.9])
print(mercado)

mercado.insert(1, [["kiwi", 200, 1.99]])
print(mercado)