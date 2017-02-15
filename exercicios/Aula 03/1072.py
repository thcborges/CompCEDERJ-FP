n = int(input())
inn = 0
out = 0
for i in range(n):
    x = int(input())
    if 10 <= x <= 20:
        inn += 1
    else:
        out += 1

print("%d in\n%d out" % (inn, out), end="\n")