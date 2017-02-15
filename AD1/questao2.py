# Subprogramas


def compara(expressao):  # Função que comparará as expressões e retornará um valor booleano
    n = len(expressao) - 1  # A variável n recebe o tamanho da expressão a ser verificada - 1 para poder comparar a
    # primeira posição com a ultima da expressão dada
    if len(expressao) > 0:  # Caso base da função recursiva. Se o tamanho da expressão recebida for menor que 0 a função
        #  retorna verdadeiro para fechar as comparações
        nova = expressao[1:n]  # A variável nova recebe uma substring da expressão atual que será repassada para nova
        # comparação.
        if (expressao[0] == expressao[n]) and (compara(nova)):  # Compara os valores atuais e usa um E lógico para
            # fazer a nova comparação. Se algum valor retornar falso toda a função também retornará falso
            return True  # Retorna True cada comparação realizada
        else:  # se alguma comparação for diferente
            return False  # Esse único retorno falso fará toda a expressão deixar de ser um palindromo
    else:  # Quando o tamanho da expressão for menor que 0
        return True   # será retornado True para que possa fechar a recursão


def preparaExpressao(expressao):   # Função que removerá os espaços da da frase a ser analisada
    nova = expressao.upper().replace(" ", "")  # Substitui os espaços por vazio
    return nova  # Retorna a nova expressão


def resultado(expressao):  # Função que escreverá na tela a mensagem pedida na questão
    nova = preparaExpressao(expressao)  # Armazena na variável nova a expressão fornecida pelo usuário a expressão em
    # caixa alta e sem espaço
    if compara(nova):  # Chama a função booleana que verificará se a nova expressão é um palindromo ou não
        print("é palíndromo")  # Caso seja palíndromo imprime na tela "é palíndromo"
    else:  # Caso contrário
        print("não é palíndromo")  # Imprime na tela "não é palíndromo"
    return None


# Programa Principal

while True:  # Para fazer o programa rodar indefinidamente utilizei o laço while True
    expressao = input()  # Aqui lê-se a expressão a ser analisada
    if expressao == "fim":  # Se a entrada for igual a "fim" o programa encerrará
        break  # Quebra de laço para encerrar o programa
    resultado(expressao)  # Chamada da função que escreverá na tela (saída padrão) a mensagem pedida na questão