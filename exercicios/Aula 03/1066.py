par = 0
impar = 0
positivo = 0
negativo = 0
for i in range(5):
   n = int(input())
   if n % 2 == 0:
       par = par + 1
   else:
       impar = impar + 1
   if n > 0:
       positivo = positivo + 1
   if n < 0:
       negativo = negativo + 1
print("%d valor(es) par(es)\n%d valor(es) impar(es)\n%d valor(es) positivo(s)\n%d valor(es) negativo(s)" % (par, impar, positivo, negativo), end="\n")
'''
print("%d valor(es) impar(es)" % impar, end="\n")
print("%d valor(es) positivos(s)" % positivo, end="\n")
print("%d valor(es) negativo(s)" % negativo, end="\n")
'''