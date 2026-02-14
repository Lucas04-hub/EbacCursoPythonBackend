# Dado um array inteiro meu_arrayzinho, retorne verdadeiro se algum alor aparecer pelo menos duas vezes no array
# E retorne falso se cada elemento for distinto.

meu_arrayzinho = [1,1,3,3,4,4,3,2,4,2]

# Chave - Valor

meu_dicionariozinho = {}

for numero in meu_arrayzinho:
    if numero not in meu_dicionariozinho:
        meu_dicionariozinho[numero] = 1
    else:
        meu_dicionariozinho[numero] += 1


for chave, valor in meu_dicionariozinho.items():
    if valor >+ 2:
        print(True)
    else:
        print(False)