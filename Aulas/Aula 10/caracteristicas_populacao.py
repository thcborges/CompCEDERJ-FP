
def perfil_comum(habitantes, caracteristicas, grupo):
    comuns = caracteristicas

    for ident in range(len(habitantes)):
        if ident in grupo:
            comuns = comuns & habitantes[ident]

    print("As caracteristicas em comum sâo:", end=" ")

    for c in caracteristicas:
        if c in comuns:
            print(c, end=" ")
    print()

    return None


# Programa Principal
caracteristicas = {"esporte","tv","cinema","livro","jornal","teatro","musica"}
alunos = [{"tv","cinema","livro"},{"cinema","musica"},{"cinema","tv","teatro"}]
perfil_comum(alunos, caracteristicas, {2, 0})