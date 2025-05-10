# Função para converter Fahrenheit para Celsius
def fahrenheit_to_celsius(f):
    return 5 * (f - 32) / 9

# Entrada do usuário
inicio = float(input("Digite o valor inicial em Fahrenheit: "))
fim = float(input("Digite o valor final em Fahrenheit: "))

# Impressão do cabeçalho
print(f"\n{'Fahrenheit':>11} | {'Celsius':>7}")
print("-" * 22)

# Verifica a direção do intervalo
passo = 1 if inicio <= fim else -1

# Geração da tabela
f = inicio
while (f <= fim if passo == 1 else f >= fim):
    c = fahrenheit_to_celsius(f)
    print(f"{f:10.1f} ºF | {c:6.3f} ºC")
    f += passo