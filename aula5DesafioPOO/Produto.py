class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def aplicar_desconto(self, percentual):
        return self.preco * (1 - percentual / 100)