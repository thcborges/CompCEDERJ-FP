# Subprograma
def conta_vogais_digitos(frase):
    vogais = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    digitos = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    numero_vogais = 0
    numero_digitos = 0

    for letra in frase:
        if letra in vogais:
            numero_vogais += 1
        elif letra in digitos:
            numero_digitos += 1

    print("Quantidade de Vogais:", numero_vogais)
    print("Quantidade de Dígitos:", numero_digitos)
    return None


# Programa Principal
lida = input('Diga a frase')
conta_vogais_digitos(lida)