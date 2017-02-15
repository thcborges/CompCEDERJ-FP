def cedulas(dinheiro):
    for nota in [100, 50, 20, 10, 5, 2, 1]:
        qtd = dinheiro // nota
        if qtd > 0:
            print("%d de R$%d" % (qtd, nota), end=" ")
        dinheiro = dinheiro % nota
        print()


troco = int(input())
while troco > 0:
    cedulas(troco)
    troco = int(input())