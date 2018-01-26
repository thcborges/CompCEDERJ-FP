x = []
for i in range(10):
    x.append(int(input()))
for j in range(len(x)):
    if x[j] <= 0:
        x[j] = 1
    print("X[%d] = %d" % (j, x[j]), end="\n")