# Decorator: acessorio para a minha linha de código

def meu_decorator(func):
    def wrapper():
        print("Antes da execução da minha função!")
        func()
        print("Depois da execução da minha função!")

    return wrapper



@meu_decorator
def despedida():
    print("tchau!")

@meu_decorator
def cheguei():
    print("Oiiiii")

cheguei()
despedida()