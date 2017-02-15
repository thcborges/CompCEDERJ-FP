# Subprograma
def mostra(vs):
    qtd_linhas = vs["Número de Linhas"]
    qtd_colunas = vs["Número de Colunas"]
    for linha in range(qtd_linhas):

        for coluna in range(qtd_colunas):
            valor = vs.get((linha,coluna), 0)
            print("%4d" % valor, end=" ")

        print()

    return None


# Programa Principal
# valores matém apenas as dimensões e os poucos números diferentes de zero
valores = {}
valores["Número de Linhas"] = 5
valores["Número de Colunas"] = 10
valores[(1,1)] = 13
valores[(0,8)] = -4
valores[(4,7)] = 75
print(valores)
mostra(valores)