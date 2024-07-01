import random

class Pokemon:
    def __init__(self,name,health,element):
        self.name = name
        self.health = health
        self.element = element

    def doMove(self):
        print("Pokemon Move")

    def doEat(self):
        print("Pokemon Eat")

class Jigglypuff(Pokemon):
    def __init__(self,name,health,element,lungcapacity):
        super().__init__(name,health,element)
        self.lungcapacity = lungcapacity

    def doMove(self):
        super().doMove()
        print("Jigglypuff can Float")

    def __str__ (self):
        return f"Name: {self.name}\n Health: {self.health}\nElement: "

class Pikachu(Pokemon):
    def __init__(self,name,health,element,electricity):
        super().__init__(name,health,element) 
        self.electricity = electricity


pokemon = Jigglypuff("J1", 75, "fairy", 92)
pokemon.doMove()

class Game:

    def __init__(self):
        self.elements = ["thunder","fire","water","ghost","ice"]
        self.pokemons = {

        }

        

        self.pokemons = {
            "jigglypuff":[Jigglypuff(f"P{i}", random.randint(50, 100), self.elements[random.int(0, len(self.elements))], random.randint(50, 100)) for i in range(0, random.randint(3, 15))],
            "pikachu":[Pikachu(f"P{i}", random.randint(50, 100), self.elements[random.int(0, len(self.elements))], random.randint(50, 100)) for i in range(0, random.randint(5, 20))]
        }

game = Game()


'''class Weapons:
   def __init__(self):
        pass

class Thunderbolt(Weapons):
    def __init__(self):
        pass

class Fireball(Weapons):
    def __init__(self):
        pass
    
'''

import random

class Pokemon:

    def __init__(self, name, health, element):
        self.name = name
        self.health = health
        self.element = element

    def doMove(self):
        print("Pokemon Move")

    def doEat(self):
        print("Pokemon Eat")

class Jigglypuff(Pokemon):

    def __init__(self, name, health, element, lungcapacity):
        super().__init__(name, health, element)
        self.lungcapacity = lungcapacity

    def doMove(self):
        super().doMove()
        print("Jigglypuff can Float")

class Pikachu(Pokemon):

    def __init__(self, name, health, element, electricity):
        super().__init__(name, health, element)
        self.electricity = electricity


class Game:

    def __init__(self):
        self.elements = ["thunder", "fire", "water", "ghost", "ice"]
        self.pokemons = {
            "jigglypuff":[Jigglypuff(f"P{i}", random.randint(50, 100), self.elements[random.int(0, len(self.elements))], random.randint(50, 100)) for i in range(0, random.randint(3, 15))],
            "pikachu":[Pikachu(f"P{i}", random.randint(50, 100), self.elements[random.int(0, len(self.elements))], random.randint(50, 100)) for i in range(0, random.randint(5, 20))]
        }


game = Game()

 
