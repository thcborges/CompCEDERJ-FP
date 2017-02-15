# AD2 - Questão 4

# Subprogramas

def lerTurmas(nomeArq):
    listaDeTurmas = []
    bdCurso = open(nomeArq, "r")
    qtdDisciplinas = int(bdCurso.readline())
    for i in range(qtdDisciplinas):
        turma = []
        nomeDisciplina = bdCurso.readline().strip()
        bdDisciplina = open(nomeDisciplina, "r")
        qtdAlunos = int(bdDisciplina.readline())
        for j in range(qtdAlunos):
            linha = bdDisciplina.readline().strip()
            partes = linha.split()
            tupla = (partes[0], float(partes[1]))
            turma.append(tupla)
        listaDeTurmas.append(turma)
    bdCurso.close()
    return listaDeTurmas


def calcularMedia(listaDeDisciplinas, mat):
    somaNotas = 0
    qtdNotas = 0
    for turma in listaDeDisciplinas:
        for (aluno, nota) in turma:
            if aluno == mat:
                somaNotas += nota
                qtdNotas += 1
    if qtdNotas == 0:
        media = 0
    else:
        media = somaNotas / qtdNotas
    return media


# Programa Principal
nomeArquivo = input("Digite o nome do arquivo: ")
matriculaAluno = input("Digite a matrícula do aluno a ser consultado: ")
todasTurmas = lerTurmas(nomeArquivo)
print(matriculaAluno, "obteve média", calcularMedia(todasTurmas, matriculaAluno))
