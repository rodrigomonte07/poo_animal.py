class Animal():
    def __init__(self, nome:str,especie:str,raca:str, cor:str, idade:int):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.cor = cor
        self.idade = idade

    def falar(self):
        return  "Este animal faz um som genérico."
    
class Cachorro():
    def __init__(self, nome:str, raca:str, cor:str, idade:int):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade
        

    def falar(self):
        return  "O cachorro está latindo."
    
class Gato():
    def __init__(self, nome:str, raca:str, cor:str, idade:str):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade

    def falar(self):
        return  "O gato está miando."
    
animal_1 = Animal(nome="Marley", especie="Ave", raca="Piriquito", cor ="verde", idade=3 )
cachorro_1 = Cachorro(nome="Bob", raca="Poodle", cor ="Cinza", idade=4 )
gato_1 = Gato(nome="Shaquira", raca="Pé duro", cor ="Marrom", idade=9 )

print(animal_1.falar())
print(cachorro_1.falar())
print(gato_1.falar())

