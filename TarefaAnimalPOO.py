class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print(f"O animal emitiu um som genérico.")


class Cachorro(Animal):
    def emitir_som(self):
        return "O cachorro latiu!"

class Gato(Animal):
    def emitir_som(self):
        return "O gato miou!"

meu_caozinho = Cachorro("Tony", 10)
meu_gatinho = Gato("Alex", 3)

animais = [meu_caozinho, meu_gatinho]

for animal in animais:
    print(animal.emitir_som())