# Definimos o uso de letras maiúsculas em uma palavra como correto quando o seguinte caso é válido:

# Toodas as letras desta palvra são maiúsculas, como "EUA".

# Dada uma palvra de string, retorne verdadeiro se o uso de letras maiúsculas está correto.


minha_stringzinha = "CACHOrro"

contador = 0

for letra in minha_stringzinha:
    if letra.isupper():
        contador += 1

print(contador)
print(len(minha_stringzinha))

if contador == len(minha_stringzinha):
    print("Passou no teste!!!!")
else:
    print("REPROVADO")