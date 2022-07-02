# Criar uma classe chamada de veículos,
# onde tenham pelo menos 5 atributos.
# Também devem ser criados 5 objetos nesta
# classe, onde cada item deve ser cadastrado
# via input


class Veiculos:
    def __init__(self, cor, ano, modelo, placa, marca):
        self.cor = cor
        self.ano = ano
        self.modelo = modelo
        self.placa = placa
        self.marca = marca

    def __repr__(self):
        return repr(f'{self.cor}, {self.ano}, {self.modelo}, {self.placa}, {self.marca}')

    def ligar(self):
        return 'O carro foi ligado'

    def desligar(self):
        return 'O carro foi desligado'


carros = []

for i in range(1, 6):
    cor = input(f'Digite a cor do veículo {i}: ')
    ano = input(f'Digite o ano do veículo {i}: ')
    modelo = input(f'Digite o modelo do veículo {i}: ')
    placa = input(f'Digite a placa do veículo {i}: ')
    marca = input(f'Digite a marca do veículo {i}: ')
    cadastro = Veiculos(cor, ano, modelo, placa, marca)
    carros.append(cadastro)
    print(carros[i])




