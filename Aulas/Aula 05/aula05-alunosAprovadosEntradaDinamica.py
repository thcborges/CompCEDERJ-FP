# Subprograma

def listaAprovadosReprovados2(infos, minimo):
    for pos in range(len(infos)):
        media = (infos[pos][1][0]+infos[pos][1][1]+infos[pos][1][2])/3

        if media >= minimo:
            print(infos[pos][0], "Aprovado com nota:", media)

    print("-----------------------------------------------------------")
    for pos in range(len(infos)):
        media = (infos[pos][1][0] + infos[pos][1][1] + infos[pos][1][2]) / 3

        if media < minimo:
            print(infos[pos][0], "Reprovado com nota:", media)

    return None

def leAlunosComNotas(qtdAlunos, qtdNotas):
    resposta = []                    # inicializa a resposta como uma lista vazia

    for indAluno in range(qtdAlunos):
        nome = input("Diga o nome do aluno " + str(indAluno + 1) + ": ")
        linha = [nome,[]]            # cada linha tem um nome e uma lista vazia de notas

        for indNota in range(qtdNotas):
            nota = float(input("Diga a nota " + str(indNota + 1) + " = "))
            linha[1].append(nota)    # anexa ao final da lista de notas a nota lida

        resposta.append(linha)       # anexa ao final da lista a linha com nome e notas

    return resposta

# Programa Principal

resultados = leAlunosComNotas(5,3)
listaAprovadosReprovados2(resultados, 6.0)