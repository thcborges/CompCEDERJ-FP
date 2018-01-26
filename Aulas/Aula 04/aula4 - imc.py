# Função que calcula o indice de Massa Corporal (IMC)
def imc(p, a):
    return p / (a * a)


# Função que retorna a situação do IMC (valor 1, 2, 3, 4)
def situacao(p, a):
    indice = imc(p, a)

    if indice <= 18.5:
        return 1
    elif indice <= 24.9:
        return 2
    elif indice <= 29.9:
        return 3
    else:
        return 4


# Programa principal
print("Bem-vindo ao programa que analisa seu IMC\n")

peso = float(input("Informe seu peso (em Kg): "))
altura = float(input("Informe sua altura (em metros): "))

opcao = situacao(peso, altura)

if opcao == 1:
    print("Você está abaixo do peso.")
elif opcao == 2:
    print("Você está com o peso adequado para sua altura.")
elif opcao == 3:
    print("Você está acima do peso")
else:
    print("Você está obeso")