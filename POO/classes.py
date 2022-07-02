class Pessoa:
    # atributos
    def __init__(self, idade, sexo, nome):
        self.idade = idade
        self.sexo = sexo
        self.nome = nome


pessoa1 = Pessoa(idade=18, sexo='Masculino', nome='Gabriel')
pessoa2 = Pessoa(idade=22, sexo='Masculino', nome='Daniel')

print(pessoa1.nome)
