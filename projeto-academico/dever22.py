def somar_tres(val1, val2, val3):
    return val1 + val2 + val3

def main():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))
    resultado = somar_tres(a, b, c)
    print(f"A soma dos três valores é: {resultado}")

main()