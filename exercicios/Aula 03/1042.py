a = input().split()
b = [0, 1, 2]
b[0] = int(a[0])
b[1] = int(a[1])
b[2] = int(a[2])

for i in range(0,2):
    for j in range(i+1,3):
        if b[i] > b[j]:
            aux = b[i]
            b[i] = b[j]
            b[j] = aux

for i in range(3):
    print(b[i])

print()

for i in range(3):
    print(a[i])
