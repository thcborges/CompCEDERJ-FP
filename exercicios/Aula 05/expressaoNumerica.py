# Subprograma

def avalia(expressao):
    valor = 0
    if expressao != "":
        partes = expressao.split("+")

        for p in partes:
            valor += float(p)

    return valor

# Programa Principal

lida = input("Entre com um expressão numéirca válida: ")
print("{" + lida + "} =", avalia(lida.strip()))