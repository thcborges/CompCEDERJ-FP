t = input().split()

hi = int(t[0])
mi = int(t[1])
hf = int(t[2])
mf = int(t[3])

md = mf - mi
hd = hf - hi

if hd <= 0:
    hd += 24

if md < 0:
    md += 60
    hd -= 1

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hd, md), end="\n")