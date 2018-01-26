# Subprogramas
def mostra(nome):
    infos = open(nome, "r")
    for linha in infos:
        print(linha.strip())
    infos.close()
    return None


def copiar(nome_origem, nome_destino):
    original = open(nome_origem, "r")
    destino = open(nome_destino, "w")
    for linha in original:
        destino.write(linha)
    original.close()
    destino.close()
    return None


# Programa Principal
nomes = input("Escreva os nomes dos arquivos, original e destino: ").split()
mostra(nomes[0])
copiar(nomes[0], nomes[1])
mostra(nomes[1])