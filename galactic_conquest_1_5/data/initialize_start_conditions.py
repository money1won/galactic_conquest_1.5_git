from random import *
from galactic_conquest_1_5.game.defaults.unit_default import UnitTemplate
from galactic_conquest_1_5.game.general_functions import spawn_garrison

def create_starting_garrisons(file):
    for _planet in file.planets:
        _num_starting_units = randint(0, 3)
        _faction = _planet.faction
        for _num in range(_num_starting_units):
            _unit = spawn_garrison(file, _planet, _planet.faction, randint(500, 600))
            # print(_unit.name + " made on " + _planet.name + " of faction " + _planet.faction.name + " P:U " + _unit.faction.name)
