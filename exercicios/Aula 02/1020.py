dia = int(input())

ano = dia // 365
dia = dia % 365
mes = dia // 30
dia = dia % 30

print("%d ano(s)\n%d mes(es)\n%d dia(s)" % (ano, mes, dia), end="\n")