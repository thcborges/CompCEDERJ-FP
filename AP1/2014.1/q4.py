def tem_vogal(a):
    for i in range(len(a)):
        if a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u":
            return True
    return False

/
# programa principal
count = 0
count_vogal = 0
a =input()
a = a.lower()
while a != "parar":
    count += 1
    if tem_vogal(a):
        count_vogal += 1
    a = input().lower()
    print(a, count, count_vogal)
print("Foram digitadas %d, dentro das quais %d tinham vogais" %(count, count_vogal), end="\n")
