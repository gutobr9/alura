import adivinhacao
import forca

def jogos():
    op_jogos = ""
    while(op_jogos != "0"):
        op_jogos = input("Escolha o jogo (1) - Adivinhacao | (2) - Forca | (0) - Sair: ")
        if(op_jogos == "1"):
            adivinhacao.jogar()
            break
        elif(op_jogos == "2"):
            forca.jogar()
            break
        else:
            if(op_jogos != "0"):
                print("Opção inválida!")
    print("Fim do programa!")
if(__name__ == "__main__"):
    jogos()