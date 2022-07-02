class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def valor(self):
        print(f'Comprimento: {self.comprimento}cm')
        print(f'Largura: {self.largura}cm')

    def mudar_valor(self, novo_comprimento, nova_largura):
        self.comprimento = novo_comprimento
        self.largura = nova_largura
        print(f'Novo comprimento: {novo_comprimento}cm \nNova largura: {nova_largura}cm')

    def calculo_area(self):
        print(f'{(self.comprimento * self.largura) / 100}m')

    def calculo_perimetro(self):
        print(f'{((self.comprimento * 2) + (self.largura * 2)) / 100}m')


x = Retangulo(10, 10)
x.valor()
x.mudar_valor(novo_comprimento=int(input('Novo comprimento: ')), nova_largura=int(input('Nova largura: ')))
x.calculo_area()
x.calculo_perimetro()
