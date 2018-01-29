n, inn, out = int(input()), 0, 0
for i in range(n):
    x = int(input())
    inn += 1 if 10 <= x <= 20 else 0
    out += 1 if 10 >= x <= 20 else 0
print("{} in\n{} out".format(inn, out))
