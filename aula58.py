# Dado um array inteiro não classificado meu_arrayzinho.
# Retorne o menor número inteiro positivo que não está presente no meu_arrayzinho.

from collections import Counter

meu_arrayzinho = [1,2,0,3,4,5,6]

# Esse número é maior do que ZERO
# Ele NÃo é decimal
# Ele é o menor deppis dos números dentro do meu arrayzinho

contador = 1

meu_dicionariozinho = {}

meu_dicionariozinho = Counter(meu_arrayzinho)


while True:
    if contador in meu_dicionariozinho:
        print(contador)
        contador += 1
    else:
        break


print(f"Contador: {contador}")