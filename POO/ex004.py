class Bomba_Combustivel:
    def __init__(self, tipo_Combustivel, valor_litro, quantidade_Combustivel):
        self.tipo_Combustivel = tipo_Combustivel
        self.valor_Litro = valor_litro
        self.quantidade_Combustivel = quantidade_Combustivel

    def abastecer_por_valor(self, valor_abastecer):
        self.valor_abastecer = valor_abastecer
        print(round(self.valor_abastecer / self.valor_Litro, 4))

    def abastecer_por_litro(self):
        print(self.quantidade_Combustivel * self.valor_Litro)

    def alterar_valor(self, vlitro_novo):
        self.valor_Litro = vlitro_novo

    def alterar_combustivel(self, ntipo_combustivel):
        self.tipo_Combustivel = ntipo_combustivel


abastecimento = Bomba_Combustivel('Gasolina', 7, int(input('Quantidade combustível: ')))
abastecimento.abastecer_por_valor(int(input('Valor a abastecer: R$')))
abastecimento.abastecer_por_litro()
abastecimento.alterar_valor(int(input('Novo valor do litro: ')))
abastecimento.alterar_combustivel(input('Novo tipo de combustível: '))