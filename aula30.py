# Dada uma string s consistindo apenas dos caracteres 'a' e 'b',
# retorne verdadeiro se cada 'a' aparecer antes de cada 'b' na string.
# Caso contrário, retorne falso.

minha_string = "aaaaaaaaabbbbbbba"

if 'ba' not in minha_string:
    print("Ta certo!! Ta seguindo a regra")
else:
    print("WRONG!!!!!! ERRADO!!!!")