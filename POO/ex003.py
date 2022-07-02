"""Classe Retangulo: Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""


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
