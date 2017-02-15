def cria_conjunto():
    escolhidos = set()
    print(escolhidos)
    return escolhidos


def adiciona_valor(valor, escolhidos):
    escolhidos.add(valor)
    print(escolhidos)
    return escolhidos


def descarta_valor(x, escolhidos):
    escolhidos.discard(x)
    print(escolhidos)
    return escolhidos


def tamanho_conjunto(escolhidos):
    return len(escolhidos)


def insere_5_elementos(escolhidos):
    for i in range(5):
        nome = input("Digite um nome: ")
        escolhidos.add(nome)

    print(escolhidos)
    return escolhidos


def cria_conjunto_pronto():
    escolhidos = {"Maria", "Ana", "Giovana", "Leandro", "Dante"}
    print(escolhidos)
    return escolhidos


def uniao_de_conjuntos(s, t):
    s.union(t)  # ou s = s | t
    return s

def intersecao_de_conjuntos(s, t):
    s.intersection(t)  # ou s = s & t
    return s


def diferenca_conjuntos(s, t):
    s.differnce(t)  # ou s = s - t
    return s


def igual(s, t):
    return s == t


def diferente(s, t):
    return s!= t


def contem(s, t):
    return s >= t  # ou s.issubset(t)


def esta_contido(s, t):
    return s <= t # ou s.issuperset(t)


def pertence(x, s):
    return x in s

conjunto = cria_conjunto()
adiciona_valor(13, conjunto)