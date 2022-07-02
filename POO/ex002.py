"""Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho = tamanho_do_lado

    def calculo(self, novo_valor):
        print(self.tamanho ** 2)
        self.tamanho = novo_valor
        print(self.tamanho ** 2)


tam = Quadrado(10)
tam.calculo(5)
