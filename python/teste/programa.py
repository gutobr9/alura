class Programa:
    def __init__(self,nome,ano):
        self._nome = nome
        self._ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self,ano):
        self._ano = ano

class Filme(Programa):
    def __init__(self,nome,ano,duracao): 
        super().__init__(nome,ano)
        self.duracao = duracao

class Serie(Programa): 
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

p = Programa("Gustavo",1994)
print(p)
repr(p)
# p.dar_like()
# print(f"{p.nome} {p.ano} {p.likes}")

# print("====================")

vingadores = Filme("vingadores - guerra infinita",2018,160)
vingadores.dar_like()
vingadores.dar_like()
# print(f"{vingadores.nome} {vingadores.ano} {vingadores.duracao}")
# print(f" {vingadores.likes}")
print("====================")

atlanta = Serie("atlanta",2018,2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
# print(f"{atlanta.nome} {atlanta.ano} {atlanta.temporadas}")
# print(f" {atlanta.likes}")

filmes_e_series = [vingadores,atlanta]

print("====================")
for programa in filmes_e_series:
    detalhes = str(programa.duracao)+" min" if hasattr(programa,"duracao") else str(programa.temporadas)+" temporadas"
    print(f"{programa.nome} {detalhes} - likes: {programa.likes}")
    repr(f"{programa.nome} {detalhes} - likes: {programa.likes}")
    print(programa)
    repr(programa)