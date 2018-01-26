from random import randint
n = int(randint(1, 9))
p = 0
t = 0
while p != n:
    p = int(input("Seu palpite: "))
    t += 1
    if p == n:
        print("ACEERTOU! Placar %i" % t)
    elif p < n:
        print("Chute um valor maior!")
    else:
        print("Chute um valor menor!")
print("Fim de jogo")