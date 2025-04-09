from Loja import Loja

def main():
    loja = Loja()
    while True:
        print("\nMinha Loja")
        print("1. Ver produtos")
        print("2. Adicionar produto no carrinho")
        print("3. Ver carrinho")
        print("4. Finalizar compra")
        print("5. Sair")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            loja.mostrar_produtos()
        elif opcao == "2":
            loja.mostrar_produtos()
            try:
                produto_idx = int(input("Numero do produto: ")) - 1
                if 0 <= produto_idx < len(loja.produtos):
                    quantidade = int(input("Quantidade: "))
                    loja.carrinho.adicionar_item(loja.produtos[produto_idx], quantidade)
                else:
                    print("Produto invalido.")
            except ValueError:
                print("Por favor, digite um numero valido.")
        elif opcao == "3":
            total = loja.carrinho.calcular_total()
            print(f"\nItens no carrinho: {len(loja.carrinho.itens)}")
            for item in loja.carrinho.itens:
                print(f"- {item['quantidade']}x {item['produto'].nome}")
            print(f"Total: R${total:.2f}")
        elif opcao == "4":
            total = loja.carrinho.calcular_total()
            if total > 0:
                loja.menu_pagamento(total)
            else:
                print("Carrinho vazio.")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opcao invalida. Digite de 1 a 5")

if __name__ == "__main__":
    main()

