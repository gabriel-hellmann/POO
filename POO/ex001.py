class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self):
        print(f'\nCor da bola: {self.cor}')
        self.cor = input('\nDigite a nova cor: ').title()
        print(f'\nNova cor: {self.cor}')


coloracao = Bola('Preta', 10, 'Borracha')
print(f'A circunferência da bola é {coloracao.circunferencia}')
print(f'\nO material da bola é {coloracao.material}')
coloracao.troca_cor()
