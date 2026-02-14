# Molde do Pokemon

# Vamos ter vários atributos

# A classe é o molde que vamos criar para poder conseguirmos construir coisas

class MoldePokemon:
    def __init__(self, nome, altura, peso, hp, ataque, tipo):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        self.altura = altura
        self.peso = peso

    def mostrar_nome_pokemon(self):
        print(f"O nome do meu pokemon é: {self.nome}")

    def mostrar_hp_pokemon(self):
        print(f"O hp do meu pokemon é: {self.hp}")

    def mostrar_tipo_pokemon(self):
        print(f"O tipo do meu pokemon é: {self.tipo}")

    def mostrar_ataque_pokemon(self):
        print(f"O ataque do meu pokemon é: {self.ataque}")

    def mostrar_altura_pokemon(self):
        print(f"A altura do meu pokemon é: {self.altura}")

    def mostrar_peso_pokemon(self):
        print(f"O peso do meu pokemon é: {self.peso}")

# Chegou a hora de pegar a classe e de fato construir essas coisas
# Por enquanto, a gente ainda tem apenas o molde
# Construir dentro da Orientação a Objetos significa criar um Objeto

pikachu = MoldePokemon("Pikachu", 50, 15, 400, "Choque do Trovão", "Eletrico")
charizard = MoldePokemon("Charizard", 50, 200, 1500, "Lança Chamas", "Fogo")
miau = MoldePokemon("miau", 30, 15, 200, "Unhada", "Normal")

pikachu.mostrar_nome_pokemon()
pikachu.mostrar_ataque_pokemon()
miau.mostrar_nome_pokemon()
miau.mostrar_altura_pokemon()
charizard.mostrar_hp_pokemon()
charizard.mostrar_ataque_pokemon()