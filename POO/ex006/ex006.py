# Criar uma classe para uma lata de coca-cola.
# A classe deve ter todos os atributos dimensionais,
# e suas características de material.
# As funcionalidades(métodos) da garrafa sao, abrir,
# beber, esvaziar, amassar, retirar lacre, e descartar

class Lata:
    def __init__(self,  diametro, altura, material, volume):
        self.diametro = diametro
        self.volume = volume
        self.altura = altura
        self.material = material
        self.aberta = False
        self.amassada = False
        self.descartada = False
        self.lacre = True

    def __repr__(self):
        return repr(f'{self.diametro}, {self.altura}, {self.material}')

    def abrir(self):
        if self.aberta:
            print('Já está aberta')
        else:
            print('Abra a lata')
            self.aberta = True

    def beber(self, quantidade):
        if not self.aberta:
            print('A lata está fechada')
        elif self.volume == 0:
            print('A lata está vazia')
        elif self.descartada:
            print('A lata já foi descartada')
        elif self.volume >= quantidade:
            self.volume -= quantidade
            print(f'Ainda restam {self.volume} mL')
        elif quantidade > self.volume:
            print(f'Você bebeu {self.volume}mL e faltou {-(self.volume-quantidade)}mL')
            self.volume = 0

    def esvaziar(self):
        if not self.aberta:
            print('A lata está fechada')
        elif self.volume == 0:
            print('A lata está vazia')
        elif self.descartada:
            print('A lata já foi descartada')
        elif self.amassada:
            print('A lata já foi amassada')
        else:
            self.volume = 0
            print('A lata está vazia')

    def amassar(self):
        if self.amassada:
            print('Já está amassada')
        elif self.descartada:
            print('A lata ja foi descartada')
        elif self.volume == 0:
            print('A lata já está vazia')
            self.amassada = True
        elif self.aberta:
            print('A lata está aberta')
        else:
            print('Você precisa beber tudo antes de amassar')

    def retirar_lacre(self):
        if self.amassada:
            print('A lata já está amassada')
        elif self.descartada:
            print('A lata já foi descartada')
        elif not self.lacre:
            print('O lacre já foi retirado')
        else:
            print('Lacre removido com sucesso')
            self.lacre = False

    def descartar(self, cor):
        if self.descartada:
            print('A lata já foi descartada')
        elif not self.amassada:
            print('A lata ainda não foi amassada')
        elif cor != 'amarelo':
            print('Não pode ser descartado nessa lixeira')
        else:
            print('Lata descartada no lugar correto')
            self.descartada = True




