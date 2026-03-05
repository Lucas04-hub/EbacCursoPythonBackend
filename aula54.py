# Na cidade de Digitville, havia uma lista de numeros chamados meu_arrayzinho contendo números inteiros de 0 1 n - 1.
# Cada número deveria aparecer exatamente uma vez na lista.
# No entento, dois números maliciosos apareceram sorrateiramente, tornando a lista mais longa do que o habitual.
# Como deteve da cidade, sua tarefa é encontrar esses dois números sorrateiros.
# Retorne um array de tamanho dois contendo dois números (em qualquer ordem), para que a paz possa retornar a Digitville.


meu_arrayzinho = [1,2,3,4,5,5,6,7,8,9,9]

# Chave - Valor

# Numero dentro do array sendo a Chave
#A quantidadd de vezes que esse número apareceu sendo o valor

meu_dicionariozinho = {}

for numero in meu_arrayzinho:
    if numero not in meu_dicionariozinho:
        meu_dicionariozinho[numero] = 1
    else:
        meu_dicionariozinho[numero] += 1

meu_arrayzinho_resulado = []

for chave, valor in meu_dicionariozinho.items():
    if valor == 2:
        meu_arrayzinho_resulado.append(chave)

print(meu_arrayzinho_resulado)