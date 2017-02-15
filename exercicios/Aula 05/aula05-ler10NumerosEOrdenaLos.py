# Subprogramas
def escrever(valores):
    for item in valores:
        print(valores, end=" ")
    print()
    return None

def ler(valores):
    for i in range(len(valores)):
        valores[i] = float(input("Digite o %dº valor: " % str(i + 1)))
    return None

def ondeMenor(vals, inicio):
    posMenor = inicio
    for p in range(inicio+1, len(vals)):
        if vals[p] < vals[posMenor]:
            posMenor = p
    return  posMenor

def ordenar(valores):
    #Função Interna ondeMenor
    def ondeMenor(vals, inicio):
        posMenor = inicio
        for p in range(inicio + 1, len(vals)):
            if vals[p] < vals[posMenor]:
                posMenor = p
        return posMenor
    for i in range(len(valores)-1):
        posicao = ondeMenor(valores, i)
        aux = valores[i]
        valores[i] = valores[posicao]
        valores[posicao] = aux
    return None

#def ordena(valores):
#    for i in range(len(valores)):
#        menor = i
#        for j in range(i+1,len(valores)):
#            if valores[j] < valores[menor]:
#                menor = j
#        aux = valores[i]
#        valores[i] = valores[menor]
#        valores[menor] = aux
#    return None

#Programa Principal
TAM = 10
numeros = [0.0]*TAM
ler(numeros)
escrever(numeros)
ordenar(numeros)
escrever(numeros)