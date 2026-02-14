# Dado um arraymeu_arrayzinho. Definimos uma soma acumulada de um array como runningSum[i] = sum(meu_arrayzinho[0]+meu_arrayzinho[i]).
# Retorne a soma acumulada de meu_arrayzinho.

# Explicação: A soma acumulada é obtida da seguinte forme: [1, 1+2, 1+2+3, 1+2+3+4].

meu_arrayzinho = [1,2,3,4]
resultado_arrayzinho = []

contador = 0

for numero in meu_arrayzinho:
    contador += numero
    resultado_arrayzinho.append(contador)

print(resultado_arrayzinho)