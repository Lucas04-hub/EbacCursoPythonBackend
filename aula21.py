# - Soma de 1 a numero_qualquer: Receba um numero_qualquer e exiba a soma de todos os números de 1 até numero_qualquer.

# 1. Receba um número qualquer

numero_qualquer = int(input())

# 2. Entender a lógica da soma

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27

# 3. Exibir a soma de todos os números de 1 até esse número

soma = 0

for i in range(1, numero_qualquer + 1):
    soma += i

print(soma)