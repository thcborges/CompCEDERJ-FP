# Subprogramas
def mostrar(prods):
    for chave, valor in sorted(prods.items()):
        print(chave, " - ", valor)
    return None


def preencher(prods, entradas):
    for i in range(entradas):
        cod = input("Código: ")
        desc = input("Descrição: ")
        qtd = int(input("Quantidade: "))
        preco = float(input("Valor: "))
        data = input("Limite de Validade - dd/mm/aa: ").split("/")
        prods[cod] = [desc, qtd, preco, (int(data[0]), int(data[1]), int(data[2]))]
    return None


def vender(prods, cods_qtds):
    total_gasto = 0
    for chave in cods_qtds:

        if chave not in prods:
            print(chave, "- Código Inexistente")

        else:
            item = prods[chave]

            if item[1] < cods_qtds[chave]:
                print(chave, " - Quantidade Insuficiente")

            else:
                item[1] -= cods_qtds[chave]
                prods[chave] = item

                print(item[0], "x", cods_qtds, "Subtotal:", item[2] * cods_qtds[chave])

                total_gasto += item[2] * cods_qtds[chave]

    print("Tota da Nota Fiscal: ", total_gasto)


# Programa Principal
produtos = {}
preencher(produtos, 5)
mostrar(produtos)
vender(produtos, {"xkk":3, "yzb":2})
mostrar(produtos)