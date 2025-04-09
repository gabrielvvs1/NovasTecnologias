class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        if produto.estoque >= quantidade:
            self.itens.append({"produto": produto, "quantidade": quantidade})
            produto.estoque -= quantidade
            print(f"{quantidade}x {produto.nome} adicionado(s) ao carrinho.")
        else:
            print(f"Sem estoque para {produto.nome}.")

    def calcular_total(self):
        return sum(item["produto"].preco * item["quantidade"] for item in self.itens)

    def finalizar_compra(self):
        self.itens = []