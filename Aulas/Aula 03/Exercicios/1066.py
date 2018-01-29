numeros = int(input()), int(input()), int(input()), int(input()), int(input())
negativo = positivo = impar = par = 0
for n in numeros:
    par += 1 if n % 2 == 0 else 0
    impar += 1 if n % 2 == 1 else 0
    positivo += 1 if n > 0 else 0
    negativo += 1 if n < 0 else 0
print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))
