# Escreva um programa que receba três números e exiba o segundo maior número entre eles.

# 1. Preciso receber esses numeros separadamente. (Receber os numeros atravez do input, separar eles atravez do split, receber essas informações/variaveis em numeros atravez do map(int))

numero1, numero2, numero3 = map(int, input().split())

# 2. Criar uma lógica para ver quem é o segundo maior

meu_array = []

meu_array.append(numero1)
meu_array.append(numero2)
meu_array.append(numero3)

meu_array.sort()

# posição 4 7 9
# posição 0 1 2

# 3. Mostrar na tela quem é o vencedor, ou seja quem é o segundo maior

print(meu_array[1])