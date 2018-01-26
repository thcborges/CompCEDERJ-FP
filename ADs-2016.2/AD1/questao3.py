# Subprogramas


def ordenaLista(lista):  # Função para ordenação do peso de cada produto. Optei pelo método bolha pois como será
    # inserido item a item este mpetodo será mais eficiente.
    n = len(lista)  # Variável n recebe o comprimento do vetor
    for i in range(n):  # Laço que verificará todas as posições do vetor
        bolha = i   # Varável bolha recebe a posição a ser verificada
        while bolha > 0:  # Laço que rodará enquanto houverem valores menores nas posições mais a esquerda do valor a
            # ser verificado
            if lista[bolha - 1] < lista[bolha]:  # Caso a posição bolha do vetor seja maior que a posição bolha - 1
                aux = lista[bolha - 1]  # Variável aux armazena o valor dda posição bolha - 1
                lista[bolha - 1] = lista[bolha]  # O valor da posição bolha é armazenado na posição bolha -1
                lista[bolha] = aux  # O da variável aux (que recebeu anteriormente bolha -1) é armazenado em bolha e
                # assim completa-se a troca de valores das posições.
                bolha -= 1  # A variável bolha é decrementada
            else:  # Caso a menor posição já esteja ocupada pelo maior valor
                bolha = 0  # a variável bolha recebe 0 para encerrar a ordenação do valor da posição i do vetor
    return lista  # Retorna o novo vetor com as posições ordenadas decrescentemente


def qtdItens():  # Funcão que vai ler a quantidade de itens e a quantidade de tops de itens da lista de produtos
    qtd = input().split()  # Fatia a entrada de dados de forma que seja obedecida o requisitado na questão
    qtd[0] = int(qtd[0])  # Transforma a entrada obtida em inteiro
    qtd[1] = int(qtd[1])  # Transforma a entrada obtida em inteiro
    return qtd  # Retorna o vetor com a quantidade de produtos  na posicão 0 e a quantidade de produtos na posicão 1.
    # Ambos em formato de número inteiro.


def buscaNome(nome, lista):  # Função que fará a busca de cada produto na lista de produtos e retornará, caso existente
    # a sua respectiva posição. Caso seja inexistente retornará -1
    n = len(lista)  # n recebe o comprimento da lista informada
    buscado = -1  # Variável buscado recebe -1, valor que será retornado caso não haja o produto procurado na lista
    for i in range(n):  # Laço para a busca em cada linha da lista de produtos o nome do mesmo
        if lista[i][0] == nome:  # Sendo encontrado o item na lista de produtos
            buscado = i  # Buscado receberá a posição referente do produto
    return buscado   # Retorna -1 caso não encontre o nome do produto na lista, ou a posição referente ao produto


def insereNome(nome, lista):  # Função para inserir um produto não existente na lista de produtos
    n = buscaNome(nome, lista)  # Chama a função buscaNome passando o nome do produto e a lista de produtos e armazena na variável n o número da sua posição.
    if n == -1:  # No caso da função retornar -1 como posição de nome, sendo esta inexistente na lista
        lista.append([nome,[0]])  # nomme é acrescentado a lista
    return lista  # Retorna a nova lista com o produto acrescentado, caso este não exista


def listaCompras(qtd):   # Funcão que vai ler as entradas de cada produto com sua respectiva quantidade. Foi elaborada
    # de forma que a lista de cada produto específico seja dada de forma ordenada desprezando os produtos com mais de
    # 100 gramas
    produtos = qtd[0]  # Armazena a posicão 0 do parâmetro recebido na variável produtos para o código ficar melhor auto
    #  explicável.
    lista = []  # A variável lista é iniciada vazia.
    for p in range(produtos):  # Laco responsável pela leitura de cada produto com seu respectivo peso.
        item = input().split()  # A variável item receberá a entrada fornecida pelo usuário a entrada será fatiada e
        # dividida s cada espaço
        nome = item[0]  # A posicao 0 de item será armazenada na variável nome para o código ficar mais intuitivo
        peso = int(item[1])  # A posicao 1 de item será convertida em inteiro e armazenada na variável peso.
        lista = insereNome(nome, lista)  # A variável lista será atualizada caso ainda não haja o nome do produto
        # informado na mesma.
        n = buscaNome(nome, lista)  # A variável n receberá aposicao da variável nome na lista.
        if peso <= 100:  # Aqui será desposada Quaker entrada cujo peso seja maior que 100
            lista[n][1].append(peso)  # Adiciona o posso fui produto a sua respectiva lista.
            if len(lista[n][1]) > 1:  # Condicao criada para evitar conflito no ordenamento de cada vetor de peso de
                # produtos.
                lista[n][1] = ordenaLista(lista[n][1])  # Envia o vetor de produtos de nome para ordenacão
    return lista  # Retorna a lista com os tipos de produtos e seus respectivos pesos ordenados


def melhorCompra(compras):  # Função que imprimirá na tela a quantidade total de gramas que deverá ser comprada.
    n = len(compras)  # A variável n recebe o comprimento da lista de produtos
    peso = 0  # A variável peso é iniciada recebendo o valor 0
    for i in range(n):  # Laço para a soma do maior peso que não seja maior 100 de cada produto
        peso += compras[i][1][0]  # Incrementa-se a peso o valor do produto mais pesado com 100 gramas ou menos a
        # variável peso
    print(peso, "grama(s)")  # Imprime na tela a variável peso seguido da string "grama(s)" conforme pedido na questão.

    return None

# Programa Principal

testes = int(input())  # Lê quantos casos de testes haverão
for i in range(testes):  # Laço para que o programa rode a quantidade de vezes de casos de testes informado.
    quantidade = qtdItens()  # Armazena no vetor quantidade a quantidade de produtos e a quantidade de itens diferentes
    compras = listaCompras(quantidade)  # Armazena a matriz com a mostra de produtos e a quantidade de cada (ordenado,
    # de forma que o primeiro item é o maior que seja menor ou igual a 100) na variável compras. É passado como
    # parâmetro os valores recebidos em quantidade.
    melhorCompra(compras)  # Passa-se a matriz compras como parâmetro para a funcão melhorCompra onde será impresso na
    # tela o peso resultado da melhor opcão de compra.