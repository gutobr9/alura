import random

def jogar():
    pontos = 1000
    numero_secreto = random.randint(1,100)
    numero_tentativas = 0
    saida = False
    while(saida == False):
        nivel = int(input("Escolha o nível (1) - Fácil | (2) - Médio | (3) - Difícil ou (0) - Sair: "))
        if(nivel == 1):
            numero_tentativas = 20
            saida = True
        elif(nivel == 2):
            numero_tentativas = 10
            saida = True
        elif(nivel == 3):
            numero_tentativas = 5
            saida = True
        else:
            if(nivel == 0):
                saida = True
                print("Fim de jogo!")
            else:
                saida = False
                print("Opção inválida, escolha o nível")
                print("")
    
    while(numero_tentativas > 0):
        chute = int(input("Qual o seu chute: "))
        if(numero_tentativas != 0):
            if(chute == numero_secreto):
                print("Acertou!")
                break
            else:
                pontos = pontos - abs(numero_secreto - chute)
                if(chute < numero_secreto):
                    print("Chute menor que número secreto!")
                elif(chute > numero_secreto):
                    print("Chute maior que número secreto!")
            print("numero secreto {} ".format(numero_secreto))
            print("pontos: {} pts".format(pontos))
        else:
            print("Fim de jogo!")

        numero_tentativas = numero_tentativas - 1
    print("Pontuação: {} pts".format(pontos))

if(__name__ == "__main__"):
    jogar()