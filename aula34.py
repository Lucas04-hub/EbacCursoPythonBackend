# Uma classe é um Molde.
# Vamos usar esse Molde para construir coisas que queremos que tem um mesmo padrão

# - Nome
# - HP
# - Tipo do meu Pokemon (Terra, Eletrico, Fogo, etc)
# - Quais seus ataques (Choque do trovão)
# - Altura
# - Peso

# Nome -> Pikachu
# HP -> 300
# Tipo -> Eletrico
# Ataque -> Choque do trovão
# Altura -> 50 cm
# Peso - 15kg

# Nome -> Charizard
# - HP -> 400
# - Tipo -> Fogo
# - Ataque ->  Lança chamas
# - Altura -> 2m
# - Peso - 1500 kg

class MoldePokemon:
    # Metodo == Função
    # Metodo construtor
    # Self tem a responsabilidade de armazenar e manipular essas informcaçõoes dos atributos
    def __init__(self, nome, hp, tipo, ataque, altura, peso):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        self.altura = altura
        self.peso = peso

    def mostrar_nome_pokemon(self):
        print (f"O nome do meu pokemon é: {self.nome}")