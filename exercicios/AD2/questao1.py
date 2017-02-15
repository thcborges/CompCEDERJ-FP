# Subprogramas

# As três primeiras funções são as exigidas pela questão

# car(dados) retorna o primeiro elemento da lista
def car(dados):
    return dados[0]


# cdr(dados) retorna a lista sem o seu primeiro elemento
def cdr(dados):
    return dados[1:len(dados)]


# cons(item, dados) retorna uma nova lista com item em sua primeira posição
def cons(item, dados):
    return [item] + dados


# Função exigida na questão (acusa erro de PEP8 devido a haver caracteres maiúsculos).
# Tem como função retornar um determinado setor da lista. Este setor deve estar
# compreendido entre as variáveis inicio e fim.
# Funciona de forma recursiva, primeiramente verificando se a lista fornecida está vazia,
# ou se a variável fim é menor que 1, o que é a base da recursão. Em seguida verifica se
# a variável inicio é maior que 1, se for ela chama a si própria passando como parametros
# a lista de valores sem o primeiro elemento e as variáveis inicio e fim decrementadas.
# Sendo a lista diferente de vazia, fim maior que 1 e inicio menor ou igual a 1, a função
# acumulará os primeiros itens da lista enquanto decrementa a variável fim. Inicio é
# passado com o mesmo valor
def obterSetor(lista, inicio, fim):  # O nome da função causa viola o PEP8 devido a haver letras maiúsculas.
    if lista == [] or fim < 1:
        return []
    elif inicio > 1:
        return obterSetor(cdr(lista), inicio - 1, fim - 1)
    else:
        return cons(car(lista), obterSetor(cdr(lista), inicio, fim - 1))


# Função que retornará o último elemento de uma lista.
# Primeiro verifica-se se a lista está vazia, se estiver,
# retorna uma lista vazia. em seguida, verifica-se se removendo
# o primeiro elemento da lista teremos uma lista vazia, se tivermos
# chegamos no último item da lista (os dois primeiros passos são a base
# da recrusão desta função). Caso nenhuma das hipóteses anteriores sejam
# satisfeitas a função chama a si própria passando como parâmetro a lista
# recebida sem o seu primeiro item.
def ultimo(lista):
    if lista == []:
        return []
    elif cdr(lista) == []:
        return car(lista)
    else:
        return ultimo(cdr(lista))


# Função recursiva que retorna toda a lista com exceção do seu último item
# Primeiro verifica-se se a lista está vazia, ou se removendo o seu primeiro
# item ela estará vazia. Em seguida verifica-se se sem os dois primeiros itens
# da lista está retornará vazio, caso verdadeiro retorna-se o primeiro item da
# lista como uma nova lista. Até aqui tivemos a base da recursão da função.
# Em seguida caso nenhuma das condições anteriores seja satisfeita, a função
# acumula o primeiro item enquanto chama a si própria passando como parâmetro
# a lista recebida sem o primeiro item.
def sem_ultimo(lista):
    if lista == [] or cdr(lista) == []:
        return []
    elif cdr(cdr(lista)) == []:
        return [car(lista)]
    else:
        return cons(car(lista), sem_ultimo(cdr(lista)))


# Função recursiva que adiciona ao final de uma lista o valor passado.
# Primeiro verifica-se se a lista está vazia, caso esteja, retorna-se o
# valor passado como referência em uma nova lista. Caso contrário
# a função acumula seu primeiro item enquanto chama a si própria passando
# o valor recebido e a lista recebida sem seu primeiro item.
def adiciona_final(valor, lista):
    if lista == []:
        return [valor]
    else:
        return cons(car(lista), adiciona_final(valor, cdr(lista)))


# Função recursiva exigida na questão para permurtar os itens de uma lista de lugares.
# Primeiro de tudo verifica-se se a lista é vazia, sendo vazia retorna uma lista vazia.
# Em seguida verifica-se se nVezes é igual a 0, se for retorna-se a lista obtida. Temos
# até aqui a base da recursão desta função.
# Em seguida verifica-se se nVezes é maior que 0 para rotacionar a lista no sentido
# horário. Se for chamamos a função rodar novamente adicionando o último item da lista
# na lista sem o seu último item e passando nVezes decrementado.
# Sendo nVezes menor que 0, adiciona-se ao final da lista sem o seu primeiro item o
# primeiro item da lista e incrementa-se nVezes.
def rodar(lista, nVezes):
    if lista == []:
        return []
    elif nVezes == 0:
        return lista
    elif nVezes > 0:
        return rodar(cons(ultimo(lista), sem_ultimo(lista)), nVezes - 1)
    else:
        return rodar(adiciona_final(car(lista), cdr(lista)), nVezes + 1)


# Função recursiva, exigida na questão. Praticamente toda a função é descrita
# no enunciado da questão. Se a lista estiver vazia retorna uma lista vazia
# se receber uma lista vazia (como estipulado na questão). Base da recursão.
# Caso não esteja vazia, a função retorna uma segunda função, insereOrdenado
# que recebe dois parâmentros o primeiro item da lista e a a chamada a si
# própria passando como parâmetro a lista recebida sem o seu primeiro elemento.
# Tudo como foi estipulado na questão.
def ordenar(lista):
    if lista == []:
        return []
    else:
        return insereOrdenado(car(lista), ordenar(cdr(lista)))


# Função recursiva exigida na questão que irá ordenar pelo método de inserção
# a lista passada como parâmetro  posicionando o valor também passado uma posição
# antes de do primeiro valor maior que este.
# Primeiro verifica-se se a lista está vazia e retorna-se uma nova lista com o
# valor passado como único item.
# Caso a lista não esteja vazia, verifica-se se o primeiro item é menor que o valor
# passado. Se for, acumula-se o primeiro valor da lista enquanto a função chama a si
# própria e passa como referência o valor que se deseja inserir e a lista sem o seu
# primeiro elemento.
# Caso nenhuma das condições sejam satisfeitas, adiciona-se o valor passado a frente
# dos demais itens da lista.
def insereOrdenado(valor, lista):
    if lista == []:
        return cons(valor, [])
    elif valor > car(lista):
        return cons(car(lista), insereOrdenado(valor, cdr(lista)))
    else:
        return cons(valor, lista)


# Programa Principal
# Como foi dito em uma dúvida na Sala de Tutoria o Programa Principal
# ficou a cargo de quem carrigirá a avaliação adicionar aos Subprogramas
# pedidos.
