ano = {"jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"}

ferias_fim_ano = {"jan", "fev", "dez"}

ferias_meio_ano = {"jul"}

ferias = ferias_fim_ano.union(ferias_meio_ano)

periodo_letivo = ano.difference(ferias)

print(periodo_letivo)