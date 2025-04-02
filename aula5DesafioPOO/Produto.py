class Produto:
    def __init__ (self, nome, preço, quantidade_estoque):
        self.nome = nome
        self.preço = preço
        self. quantidade_estoque = quantidade_estoque

    def comprar_produto(self):
        self.comprado = True
