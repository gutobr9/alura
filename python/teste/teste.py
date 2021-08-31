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

class Conta:
    def __init__(self,numero,titular,saldo=0,limite=100):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def depositar(self,valor):
        self.__saldo += valor

    @property
    def extrato(self):
        print("===================================")
        print("Titular {}".format(self.__titular))
        print("Valor do saldo R$ {}".format(self.__saldo))
        print("Limite R$ {}".format(self.__limite))
        print("===================================")

    def transferir(self,valor,destino):
        self.saca(valor)
        destino.depositar(valor)
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}

conta = Conta(123,"Gustavo")
conta.extrato
conta.sacar(100)
conta.extrato

# conta2 = Conta(321,"Blenda")
# conta.depositar(50)
# conta.extrato()
# conta.transferir(0,conta2)
# conta.extrato()
# conta2.extrato()

# class Carro:
#     def __init__(self,modelo,marca):
#         self.__modelo = modelo
#         self.__marca = marca
#         self.__status = False
#     def ligar(self):
#         self.__status = True
#     def desligar(self):
#         self.__status = False
#     def detalhes(self):
#         print("Modelo: {} Marca:{} Status:{}".format(self.__modelo,self.__marca,self.__status))

# carro = Carro("gol","VW")
# carro.modelo = "up"
# carro.ligar()
# carro.status = False
# carro._Carro__status = False
# carro.detalhes()