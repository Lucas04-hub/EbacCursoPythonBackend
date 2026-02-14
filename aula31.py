# Dado um array meu_arrazyzinho contendo n números do intervalo [0, n],
# retorne o único número no intervalo que está faltando no array.


meu_arrayzinho = [0,1,2,3,4,5,6,7,8,10]


tamanho_meu_arrazyzinho = len(meu_arrayzinho)
soma_valores_meu_arrayzinho = sum(meu_arrayzinho)

soma_total = tamanho_meu_arrazyzinho * (tamanho_meu_arrazyzinho + 1) // 2

print(soma_total - soma_valores_meu_arrayzinho)