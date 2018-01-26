# SubProgramas
# Resolvi essa questão logo nas primeiras semanas do curso, hoje eu já a teria feito de forma mais otimizada.
# Porém sua implementação funciona , a meu ver, conforme especificado na questão.


def converte(numDecimal, base):  # Função, ou Subprograma  que vai converter o número (numDecimal) e a base (base)
    # passados por parametro
    conversao = [0, 1, 2, 3, 4, 5, 6, 7]  # Lista que será usada para armazenar cada casa decimal do número convertido.
    # 8 números são suficientes, pois o maior valor informado será 100, caso fosse maior precisaria aumentar a lista.
    i = 0  # Índice que será usado para defiir onde será salvo o cada casa decimal do número convertido e quanto será
    # necessário multiplicar por 10 para que a soma dos valores seja correta.
    numConvertido = 0  # Declaração da variáve que armazenará e retornará o número convertido. É preciso iniciá-la com
    # 0 para que não ocorra erro mais a frente.
    while numDecimal > 0:  # Laço que efetuará os calculos para transformar o número informado na base decimal recebida.
        conversao[i] = numDecimal % base  # Efetuada a conta aritmética para  conversão do número decimal na base
        # informada ao subprograma, ela é armazenada na lista com a posição correspondente
        numDecimal = numDecimal // base  # O número recebido é dividido para a execussão do próximo passo
        if numDecimal > 0:  # Verifica se o número informado é maior que 0 para incrementação do índice
            i += 1  # Incrementa o índice.
    while i >= 0:  # Laço que vai compor o número convertido.
        numConvertido += (conversao[i] * (10 ** i))  # Aqui eu elevo 10 ao valor do índice, feito isso multiplico o
        # resultado pelo número armazenado  no mesmo índice da lista que armazena cada casa decimal e somo com o valor
        # já armazenado anteriormente.
        i -= 1  # Decrementa-se o índice.
    return numConvertido  # Retorna-se o número recebido no valor convertido.

# Programa Principal
while True:
    numDecimal = int(input())  # Recebe o valor a ser convertido ###Aprendi com o URI que se o problema não pede para
    # haver mensagem para entradas, não devo colocá-las, por isso não pus.###
    if numDecimal == -1:  # Verifica se o valor recebido é a ultima linha do código
        break  # Interrompe o laço while se a entrada for igual a -1
    for i in range(2, 10):  # Laço para a conversão de cada base, começa em 2 e vai até 9
        numConvertido = converte(numDecimal, i)  # Chama a função converte e armazena o resultado em numConvertido,
        # passando os parametros do numero a ser convertido (numDecimal e a base a ser  para a qual o numero vai ser
        # convertido (i)
        print("%d" % (numConvertido), end=" ")  # Imprime na tela o valor convertido e da um espaço.
    print()  # Imprime uma quebra de linha.