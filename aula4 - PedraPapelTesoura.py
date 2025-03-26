import random

opcoes = ["Pedra", "Papel", "Tesoura"]

while True:
    jogador = input("\nEscolha Pedra, Papel ou Tesoura (ou 'sair' para encerrar): ").capitalize()
    
    if jogador == "Sair":
        print("Até a próxima.")
        break
    
    if jogador not in opcoes:
        print("Escolha inválida!")
        continue
    
    maquina = random.choice(opcoes)
    
    print(f"Voce escolheu: {jogador}")
    print(f"A maquina escolheu: {maquina}")

    if jogador == maquina:
        print("Empate!")
    elif (jogador == "Pedra" and maquina == "Tesoura") or \
         (jogador == "Papel" and maquina == "Pedra") or \
         (jogador == "Tesoura" and maquina == "Papel"):
        print("Você venceu!")
    else:
        print("A maquina ganhou :(")
