# Dado um endereço IP válido (IPv4), retorne uma versão ajustada desse indereço IP.
# Um endereço IP ajustafi substitui cada ponto "." por "[.]".

# Endereço Original = 1.1.1.1
# Versão Ajustada 1[.]1[.]1[.]1

# 1. Receber a string com nosso endereço IP

endereco_ip = input()

# 2. Fazer a opereção para substituir os pontos por parenteses e ponto

novo_endereco_ip = ""

for i in endereco_ip:
    if i == ".":
        novo_endereco_ip += "[.]"
    else:
        novo_endereco_ip += i

print(novo_endereco_ip)

# 1.1.1.1
# 0123456