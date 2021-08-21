import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) - Forca (2) - Adivinhação")
    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()
    else:
        print("Escolha uma opção válida!")

if(__name__ == "__main__"):
    escolher_jogo()