from random import *
from galactic_conquest_1_2.game.defaults.unit_default import UnitTemplate

def create_garrisons(file):
    for _planet in file.planets:
        _num_starting_units = randint(0, 3)
        _faction = _planet.faction
        for _num in range(_num_starting_units):
            _unit = UnitTemplate()
            _unit.faction = _faction
            _unit.soldiers = 600
            _unit.power = randint(20, 80)
            _planet.troops_present.append(_unit)
            print(_unit.name + " made on " + _planet.name + " of faction " + _planet.faction.name + " P:U " + _unit.faction.name)
    pass
