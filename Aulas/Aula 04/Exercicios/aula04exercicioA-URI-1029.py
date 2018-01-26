def call(x):
    if x == 0 or x == 1:
        return 1
    else:
        return call(x-1) + call(x - 2) + 1

n = int(input())
for i in range(n):
    x = int(input())
    fib1 = 0
    fib2 = 1
    for j in range(x-1):
        fibonacci = fib1 + fib2
        fib1 = fib2
        fib2 = fibonacci
    c = call(x) - 1
    print("fib(%d) = %d calls = %d" % (x, c, fibonacci), end="\n")