# inteiros = [1,3,4,5,7,8,9]
# pares = []
# for numero in inteiros:
#     if numero % 2 == 0:
#         pares.append(numero)
# print(inteiros)
# print(pares)

# print("====================")


# List Comprehension
# pares = [i for i in inteiros if i % 2 == 0]
# impares = [i for i in inteiros if i % 2 != 0]

# print(inteiros)
# print("Pares: {}".format(pares))
# print("Ímpares: {}".format(impares))

# x = input("Digite: ")
# print(x)
# if(x == ""):
#     x = True
# print(type(x))

# palavra = "teste"

# t = ["_" for p in palavra]

# print(t)

# Leitura de arquivo
# arquivo = open("palavras.txt","w")
# limite = 11
# for x in range(1,limite):
#     if x == limite-1:
#         arquivo.write("teste {}".format(x)) 
#     else:
#         arquivo.write("teste {} \n".format(x)) 
# arquivo.close()


# Leitura apenas da primeira linha
# arquivo = open("palavras.txt","r")
# linha = arquivo.readline()
# print(linha)


# Leitura de palavras a partir de arquivo e escolhe randomica de uma palavra
# import random
# palavras = []
# arquivo = open("palavras.txt","r")
# for linha in arquivo:
#     palavras.append(linha.strip().upper())
# palavra_posicao = random.randrange(0,len(palavras))
# print(palavras)
# print(palavras[palavra_posicao])


# Teste de ordem de funções
# def go():
#     mostrar()

# def mostrar():
#     print("teste de blenda")

# if(__name__ == "__main__"):
#     go()


# Parametros opcionais e obrigatorios
# def pessoa(nome,sb="Bezerra"):
#     return nome,sb

# print(pessoa("Gustavo","Rodrigues"))


# Funções 
# def criar_conta(numero,titular,saldo,limite):
#     conta={
#         "numero":numero,
#         "titular":titular,
#         "saldo":saldo,
#         "limite":limite
#     }
#     return conta

# def depositar(conta,valor):
#     conta["saldo"] += valor

# def sacar(conta,valor):
#     conta["saldo"] -= valor

# def extrato(conta):
#     print("Saldo R$ {}".format(conta["saldo"]))

# conta_gustavo = criar_conta(798465,"Gustavo B Rodrigues",-4000,5000)

# print(conta_gustavo)
# print(conta_gustavo["numero"])
# print(conta_gustavo["titular"])
# print(conta_gustavo["saldo"])
# print(conta_gustavo["limite"])

# extrato(conta_gustavo)
# depositar(conta_gustavo,4000)
# extrato(conta_gustavo)
# sacar(conta_gustavo,1)
# extrato(conta_gustavo)


# OO

# class ContaCorrente:
#     pass

# conta1 = ContaCorrente()
# print(conta1)
# conta2 = ContaCorrente()
# print(conta2)


class ContaCorrente:
    def __init__(self,numero=789465,titular="Gustavo",saldo=-4000,limite=5000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print("Saldo R$ {} do titular {}".format(self.saldo,self.titular))

    def deposita(self,valor):
        self.saldo +=valor

    def saca(self,valor):
        self.saldo -=valor

conta_01 = ContaCorrente()
conta_02 = ContaCorrente(79,"Guto",23000,5000)

print(conta_01)
print(conta_01.numero)
print(conta_01.titular)
print(conta_01.saldo)
print(conta_01.limite)
print("================")
print(conta_02)
print(conta_02.numero)
print(conta_02.titular)
print(conta_02.saldo)
print(conta_02.limite)

print("Extrato:")
conta_02.extrato()
conta_02.deposita(500)
conta_02.extrato()
conta_02.saca(1000)
conta_02.extrato()