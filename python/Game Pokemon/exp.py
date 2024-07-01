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

class Pikachu(Pokemon):
    def __init__(self,name,health,element,electricity):
        super().__init__(name,health,element)
        self.electricity = electricity


pokemon = Jigglypuff("J1", 75, "fairy", 92)
pokemon.doMove()


class Weapons:
    def __init__(self):
        pass

class Thunderbolt(Weapons):
    def __init__(self):
        pass

class Fireball(Weapons):
    def __init__(self):
        pass


