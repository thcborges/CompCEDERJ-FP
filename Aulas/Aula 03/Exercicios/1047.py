hora_inicial, minuto_inicial, hora_final, minuto_final = map(float, input().split())
horas_duracao, minutos_duracao = hora_final - hora_inicial, minuto_final - minuto_inicial
horas_duracao += 24 if horas_duracao < 0 else 0
if minutos_duracao < 0:
    minutos_duracao, horas_duracao = minutos_duracao + 60, horas_duracao - 1
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas_duracao, minutos_duracao))
