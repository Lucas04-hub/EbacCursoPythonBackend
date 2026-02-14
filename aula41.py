# Lambda: funções anonimas
#def soma(x, y):
#   return x + y


# print(soma(5,3))

#soma = lambda x,y : x + y

#print(soma(5,5))


meu_arrayzinho = (1,2,3,4,5)

duplicados = map(lambda numero : numero * 2, meu_arrayzinho)

print(list(duplicados))