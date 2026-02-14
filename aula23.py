# Receba uma lista de palavras e ordene-as em ordem alfabética.


# 1. Criar um array vazio para receber essas palavras

meu_array = []

# 2. Definir uma quantidade de palvras

# Serão 5 palvras

# 3. Criar a logica para receber essas palavras e adicionar dentro do array

for i in range(1,6):
    palvra = input()
    print("palavra sendo adicionada")
    meu_array.append(palvra)

print(meu_array)

# 4. Ordernar a lista

meu_array.sort()

# 5. Printar na tela

print(meu_array)