# Polimorfismo

class Colaborador:
    def contratar_novo_colaborador(self):
        pass

class Estagiario(Colaborador):
    def falar(self):
        return "5 etapas de ....!"

class Diretor(Colaborador):
    def falar(self):
        return "150 etapas, + enem + prova discursiva + adrenalina!"
    


Colaboradores = [Estagiario(), Diretor()]

for Colaborador in Colaboradores:
    print(Colaborador.falar())