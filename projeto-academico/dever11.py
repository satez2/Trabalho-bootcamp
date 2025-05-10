from datetime import datetime

def mostrar_mensagem(mensagem, numero):
    print(f"Mensagem: {mensagem}")
    print(f"Número: {numero}")

def calcula_idade(ano_nascimento):
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento

def main():
    print("Escolha uma opção:")
    print("1 - Mostrar mensagem")
    print("2 - Calcular idade")
    escolha = input("Opção: ")

    if escolha == "1":
        mensagem = input("Digite uma mensagem: ")
        numero = input("Digite um número: ")
        mostrar_mensagem(mensagem, numero)
    elif escolha == "2":
        ano = int(input("Digite seu ano de nascimento: "))
        idade = calcula_idade(ano)
        print(f"Sua idade é: {idade} anos")
    else:
        print("Opção inválida.")

main()
