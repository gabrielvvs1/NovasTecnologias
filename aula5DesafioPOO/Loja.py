from Carrinho import Carrinho
from Produto import Produto

class Loja:
    def __init__(self):
        self.carrinho = Carrinho()
        self.produtos = [
            Produto("Produto A", 50.0, 10),
            Produto("Produto B", 100.0, 5),
            Produto("Produto C", 150.0, 0),
            Produto("Produto D", 75.0, 8),     # Novo produto
            Produto("Produto E", 30.0, 20)     # Novo produto
        ]

    def mostrar_produtos(self):
        print("\nProdutos disponiveis:")
        for idx, produto in enumerate(self.produtos, 1):
            print(f"{idx}. {produto.nome} - R${produto.preco:.2f} | Estoque: {produto.estoque}")

    def menu_pagamento(self, total):
        print("\nFormas de pagamento:")
        print("1. Dinheiro (15% de desconto)")
        print("2. Cartão (sem desconto / acrescimo)")
        print("3. PIX (15% de desconto)")
        opcao = input("Escolha a forma de pagamento: ")

        if opcao == "1":
            total *= 0.85
            print(f"Total com desconto: R${total:.2f}")
            self.pagar_dinheiro(total)
        elif opcao == "2":
            print(f"Total: R${total:.2f}")
            self.pagar_cartao()
        elif opcao == "3":
            total *= 0.85
            print(f"Total com desconto: R${total:.2f}")
            self.pagar_pix()
        else:
            print("Opcao invalida.")

    def pagar_dinheiro(self, total):
        valor = float(input("Digite o valor pago em dinheiro: "))
        if valor >= total:
            print(f"Valor do troco: R${valor - total:.2f}")
            self.carrinho.finalizar_compra()
        else:
            print("Valor insuficiente.")

    def pagar_cartao(self):
        print("Pagamento com cartao aprovado!")
        self.carrinho.finalizar_compra()

    def pagar_pix(self):
        print("Pagamento via PIX aprovado!")
        self.carrinho.finalizar_compra()

        