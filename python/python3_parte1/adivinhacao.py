# print("*********************************")
# print("Bem-vindo ao jogo de Adivinhação!")
# print("*********************************")
#
# numero_secreto = 43
# total_de_tentativas = 3
# rodadas = 1
#
# while (rodadas <= total_de_tentativas):
#     print("Tentativa {} de {}".format(rodadas,total_de_tentativas))
#     chute = input("Digite o seu numero: ")
#     print("Você digitou",chute)
#
#     try:
#         acertou = int(chute) == numero_secreto
#         maior   = int(chute) > numero_secreto
#         menor   = int(chute) < numero_secreto
#
#         if (acertou):
#             print("Você acertou!")
#             break
#         else:
#             if (maior):
#                 print("Você errou! O chute foi maior do que o número secreto")
#             elif (menor):
#                 print("Você errou! O chute foi menor do que o número secreto")
#     except:
#         print("Tipo de dado inválido")
#     rodadas = rodadas + 1
# print("Fim do jogo")

import random
print("*********************************")
print("Bem-vindo ao jogo de Adivinhação!")
print("*********************************")

print("Qual o nível de dificuldade?")
print("(1) - Fácil (2) - Médio (3) - Difícil")
nivel = input("Definir nível: ")

if (nivel == "1"):
    print("Nível fácil")
    total_de_tentativas = 20
elif (nivel == "2"):
    print("Nível médio")
    total_de_tentativas = 10
elif (nivel == "3"):
    print("Nível difícil")
    total_de_tentativas = 5
else:
    print("Nível inválido")

limite_inferior     = 1
limite_superior     = 100
numero_secreto      = random.randint(limite_inferior,limite_superior)


for rodadas in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodadas,total_de_tentativas))
    chute = input("Digite um número entre {} e {}: ".format(limite_inferior,limite_superior))
    chute = int(chute)
    print("Você digitou",chute)

    # print("*****************")
    # print("-----------------")
    # print(chute," ",type(chute))
    # print(numero_secreto, " ", type(numero_secreto))
    # print("-----------------")
    # print("*****************")

    try:
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(chute > limite_superior):
            print("Você digitou acima do limite dos números!")
        elif(chute < limite_inferior):
            print("Você digitou a baixo do limite dos números!")
        else:
            if (acertou):
                print("Você acertou!")
                break
            else:
                if (maior):
                    print("Você errou! O chute foi maior do que o número secreto")
                elif (menor):
                    print("Você errou! O chute foi menor do que o número secreto")
                if(rodadas == total_de_tentativas):
                    print("Número secreto:",numero_secreto)
    except:
        print("Tipo de dado inválido")
    # rodadas = rodadas + 1
print("Fim do jogo")