# Subprogramas


# Função que lerá as notas de cada matéria e retornará em uma lista de tuplas.
# Primeiramente cria-se uma lista vazia onde serão acrescentadas as tuplas, em
# seguida abre-se o arquivo cujo nome foi obtido no arquivo com os nomes das
# disciplinas e lê-se a sua primeira linha onde consta o número de alunos
# cursando a disciplina. Depois entra-se num laço delimitado por esse número
# que lerá a matrícula e a nota de cada aluno cursando a discilpina e depois
# inserido na lista criada em formato de tupla, onde o primeiro elemento é uma
# string com a matrícula do aluno e o segundo elemento é conversão para ponto
# flutuante de sua nota. Por fim fecha-se o arquivo que foi aberto e retorna-se
# a lista obtida.
def ler_notas(nome_arquivo):
    mat_nota = []

    arquivo = open(nome_arquivo, "r")
    n = int(arquivo.readline())

    for i in range(n):
        linha = str(arquivo.readline()).split()
        mat_nota.append((linha[0], float(linha[1])))

    arquivo.close()

    return mat_nota


# Função que retornará uma lista de tuplas cujo chave será o nome da matéria
# Primeiramente cria-se um dicionário, em seguida abre-se o arquivo cujo nome
# foi digitado pelo usuário e lê-se a primeira linha, onde constará a quantidade
# de matérias existentes. Com esse número obtido leremos as próximas linhas que
# conterão o nome dos arquivos de cada disciplinas, removendo a quebra de linha
# final. Passa-se o nome do arquivo como referência para a função que vai ler
# as notas e retornar uma lista com essas. Então adiciona-se essas notas ao
# dicionário onde a chave será o nome da matéria.
# Por fim fecha-se o arquivo que foi aberto e retorna-se o conjunto criado.
def lerTurmas(nomeArq):  # Acusa violação ao PEP8 dizendo que tanto o nome da função quanto da variável deveriam
    # ser minusculas
    turmas = {}

    arquivo = open(nomeArq, "r")
    n = int(arquivo.readline())

    for i in range(n):
        disciplina = str(arquivo.readline()).split("\n")
        mat_nota = ler_notas(disciplina[0])
        turmas[disciplina[0]] = mat_nota

    arquivo.close()

    return turmas


# Função que calculará a média de notas de determinado aluno cuja matrícula
# foi fornecida pelo usuário. Recebe comom parâmetros a lista de diciplinas,
# matrículas e notas de cada aluno.
# Primeiro cria-se duas variáveis com o valor 0. Uma apra somar as notas desse
# aluno e outra para contar a quantidade de disciplinas cursadas por ele.
# Então entra-se em um loop que rodará para cada chave dessa lista.
# Atribui-se então a variável disciplina a lista de notas de cada disciplina
# para então entrar em outro laço que verificará se a matrícula de cada aluno
# corresponde com a matrícula informada pelo usuário. Caso corresponda, essa será
# somada a variável soma e variável que conta as disciplinas será incrementada.
# Antes de retornar algum valor, verifica-se se a matrícula foi encontrada em alguma
# matéria, retornando -1 no caso de não ter sido encontrado a matrícula do aluno
# nas disciplinas pesquisadas ou retorna a média obtida pelo aluno nas disciplinas
def calcularMedia(listaDeListas, mat):  # Acusa erro de PEP8 informando que tanto nome da função quanto a variável
                                        # deveriam ser minusculas
    soma = 0
    qtd_disciplinas = 0

    for chave in listaDeListas:
        disciplina = listaDeListas[chave]

        for matricula_aluno, nota in disciplina:
            if matricula_aluno == mat:
                soma += nota
                qtd_disciplinas += 1

    if qtd_disciplinas == 0:
        return -1
    else:
        media_aluno = soma / qtd_disciplinas
        return media_aluno


# Função que imprimirá a nota do aluno. Caso não seja encontrada a matrícula do
# aluno nas disciplinas procuradas, imprime "Aluno não registrado".
def imprime_media(notas):
    if notas == -1:
        print("Aluno não registrado.")
    else:
        print("%s obteve média %.1f" % (matricula, notas), end="\n")


# Programa Principal
# Primeiramente pede que o usuário entre com o nome do arquivo do curso,
# em seguida cria a lista de notas e matrícula de cada disciplina
# pede que o usuário entre com o número da matrícula do aluno o qual
# deseja-se calcular a média das notas nas disciplinas.
# por fim chama-se a função que escreverá na saída padrão as notas do aluno
curso = input()
lista = lerTurmas(curso)
matricula = input()
media = calcularMedia(lista, matricula)
imprime_media(media)
