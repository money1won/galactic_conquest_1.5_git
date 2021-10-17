from random import *

class UnitTemplate:
    def __init__(self):
        self.soldiers = randint(100, 2000)
        self.name = self.name_gen()
        self.faction = None
        self.technologies = []
        self.power = randint(1, 1000)
    def name_gen(self):
        _ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
        _number = _ordinal(randint(1, 1000))
        _type = choice(["Infantry", "Armor", "Airborne"])
        _echelon = choice(["Battalion", "Brigade", "Division"])
        _output = str(_number) + " " + _type + " " + _echelon
        return _output

    def attack(self, opponent):
        opponent.soldiers -= self.power
        print(opponent.name + " remaining Soldiers: " + str(opponent.soldiers))
        pass