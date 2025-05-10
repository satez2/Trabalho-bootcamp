def mostrar_mensagem(mensagem, numero):
    print(f"Mensagem: {mensagem}")
    print(f"Número: {numero}")

def main():
    mensagem = input("Digite uma mensagem: ")
    numero = input("Digite um número: ")
    mostrar_mensagem(mensagem, numero)

main()

from datetime import datetime

def calcula_idade(ano_nascimento):
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento

def main():
    ano = int(input("Digite seu ano de nascimento: "))
    idade = calcula_idade(ano)
    print(f"Sua idade é: {idade} anos")

main()
