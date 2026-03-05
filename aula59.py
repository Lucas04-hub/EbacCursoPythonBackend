# Às vezes, algumas palavras como "localization" ou "internationalization" são tão longas que escrevê-las muitas vezes em um texto é bastante cansativo.
# Vamos considerar uma palavra muito longa se seu comprimento for estritamente superior a 10 caracteres.
# Todas as palavras muito longas devem ser substituídas por uma abreviatura especial.
# Essa abreviatura é feita assim:
# Escrevemos a primeira e a última letra de uma palavra e entre elas escrevemos a quantidade de letras entre a primeira e a última letra.
# Esse número está no sistema decimal e não contém zeros à esquerda.
# Assim, "localization" será escrita como "110n" e "internationalization" será escrita como "i18n".

minha_stringzinha = "localization"

print(len(minha_stringzinha))

if len(minha_stringzinha) > 10:
    # 1. Escrevemos a primeira letra da string
    # 2. Escrevemos a última letra da string
    # 3. Entre as duas (primeira e última letra), escrevemos o comportamento que sobrou da string
    # tamanhp 10
    print(f"{minha_stringzinha[0]}{len(minha_stringzinha)-2}{minha_stringzinha[-1]}")
else:
    print(minha_stringzinha)