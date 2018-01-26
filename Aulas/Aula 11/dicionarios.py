pares = dict()  #ou pares = {}
print(pares)

pares[13] = "Valor da Sorte"
print(pares)

pares = {51:"Boa ideia", 13:"Valor da Sorte", 31:"Dia do Azar"}
print(pares)

del pares[13] # ou pares.pop(13)
print(pares)

print(len(pares))

'''
pares = dict()
for i in range(5):
    nome = input("Digite nome: ")
    fone = input("Digite o telefone de " + nome + ": ")
    pares[nome] = fone
print(pares)
'''

print()
pares = {"Maria":"3456-7922", "Ana":"3214-2211", "Giovanna":"4564-1234"}
print(pares)

print()
print("pares.items() ", pares.items())
print("pares.keys() ", pares.keys())
print("pares.values() ",pares.values())
print()

print("for chave in pares:")
for chave in pares:
    print(chave, ":", pares[chave])
print()


print("for chave, valor in pares.items():")
for chave, valor in pares.items():
    print(chave, ":", valor)
print()

print("for chave in sorted(pares):")
for chave in sorted(pares):
    print(chave, ":", pares[chave])
print()

print("for chave in sorted(pares.keys()):")
for chave in sorted(pares.keys()):
    print(chave, ":", pares[chave])
print()

print("for valor in pares.values():")
for valor in pares.values():
    print(valor)
print()

print("get()")
pares = {51:"Boa ideia", 13:"Valor da Sorte", 31:"Dia do Azar"}
print(pares)
print("pares.get(51)", pares.get(51))
print("pares.get(44)", pares.get(44))
print('pares.get(51, "Vazia")', pares.get(51, "Vazia"))
print('pares.get(44, "Vazia")', pares.get(44, "Vazia"))
print()
