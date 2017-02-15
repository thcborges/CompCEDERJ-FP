c = 0
n = 2**3*3**2*5**4
print ("n =",n)
for i in range(1, n+1):
    if n % i == 0:
        c += 1
        print(i)
print("Total de divisores:", c)