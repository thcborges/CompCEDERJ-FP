a, b, c = map(float, input().split())
if max(a, b, c) >= a + b + c - max(a, b, c):
    print("Perimetro = {:.1f}".format(a + b + c))
else:
    print("Area = {:.1f}".format((a + b) * c / 2))
