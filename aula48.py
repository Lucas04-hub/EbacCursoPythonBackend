# Dada uma string minha_stringzinha que consiste em palavras e espaços, retorne o comprimento da última palavra da string.

minha_stringzinha = "   fly me  to  the moon  "

meu_arrayzinho = minha_stringzinha.split()
# a função split divide uma string em uma lista de substrings com base em um delimitador.

print(len(meu_arrayzinho[-1]))