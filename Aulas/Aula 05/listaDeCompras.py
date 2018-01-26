# Subprogramas

def preencher():
    itens = []
    nome = input("Nome do Produto: ")

    while nome != "Fim":
        qtd = int(input("Quantidade: "))
        preco = float(input("Preço Unitário: "))
        itens.append((nome, qtd, preco))
        nome = input("Nome do Prouto: ")
    return itens

def processar(itens):
    total = 0.0
    for (nome, qtd, preco) in itens:
        total += qtd * preco
        print("Nome: ", nome, " Quantidade: ", qtd, "Preço: ", preco)

    print("Total Gasto: ", total)
    return None

# Programa Principal

compras = preencher()
processar(compras)