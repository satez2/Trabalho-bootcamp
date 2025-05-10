# Crie uma função que receba a altura (em metros) e o peso (em kg) de uma pessoa e calcule o Índice de Massa Corporal (IMC).
# A função deve retornar o valor do IMC.
# A função principal deve ler os dados do usuário, chamar a função e exibir o IMC calculado.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def main():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")

main()
