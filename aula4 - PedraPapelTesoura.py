import random


itens = ["Pedra, Papel, Tesoura"]

def menu():
    print("Menu de Escolha::")
    print("0. Sair")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    
def escolher_opcao():
    opcoes = {1: "Pedra", 2: "Papel", 3:"Tesoura"}
    
def jogar():
    jogador =  opcoes = {1: "Pedra", 2: "Papel", 3:"Tesoura"}

    while True:
    menu():
    jogador = escolher_opcao()

    maquina = random.randint(1,3)

    print(f"voce ecolheu:(opcoes{jogador})")
    print(f"a maquina escolheu:(opcoes{maquina})\n")

    if jogador == maquina:
        print("Empate")
    elif (jogador == 1 and maquina == 3) or (jogador == 2 and maquina == 1) or (jogador == 3 and maquina == 2):
        print("voce ganhou")
    else:
        print("A maquina ganhou")
