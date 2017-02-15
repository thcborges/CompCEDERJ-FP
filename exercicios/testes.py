def insertion_sort(lista):
    for index in range(1, len(lista)):

        currentvalue = lista[index]
        position = index
        print(lista)

        while position > 0 and lista[position - 1] > currentvalue:
            lista[position] = lista[position - 1]
            position -= 1

        lista[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)

if (3, 5.4, 4.2) > (3, 5.4, 3.2):
    print("Blz")
else:
    print("Fudeu")
