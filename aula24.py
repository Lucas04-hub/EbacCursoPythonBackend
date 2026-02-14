# Receba um número e determine se ele é um palíndromo (lê-se igual de frente para trás).

# 1. Receber um numero inteiro

meu_numero = int(input())

# 2. Determinar se é um palíndromo
# 3. Retornar se é ou não é

minha_string = str(meu_numero)

if minha_string == minha_string[::-1]:
    print("é um palíndromo!")
else:
    print("não é um palíndromo")