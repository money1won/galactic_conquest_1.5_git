from random import *
from galactic_conquest_1_2.game.update_functions import update_map

def movement(file):
    if file.movement_start.faction == file.movement_end.faction:
        file.movement_end.outbound_troops = file.movement_start.outbound_troops
    else:
        file.movement_end.enemies_present = file.movement_start.outbound_troops
        combat(file, file.movement_end.enemies_present, file.movement_end.troops_present)
        update_map(file)
    file.movement_start.outbound_troops = []
    pass


def combat(file, attacking_troops, defending_troops):
    in_combat = True
    if len(attacking_troops) == 0:
        in_combat = False
    elif len(defending_troops) == 0:
        in_combat = False
        move_enemy_to_garrison(file, attacking_troops)
    while in_combat:
        # Attackers attack a random defender first
        for _unit in attacking_troops:
            _unit.attack(choice(defending_troops))
        # Defenders attack an attacker second
        for _unit in defending_troops:
            _unit.attack(choice(attacking_troops))

        for _unit in attacking_troops:
            # If attacker unit has no soldiers
            if _unit.soldiers <= 0:
                attacking_troops.remove(_unit)
            # If attacker has no more units
            if len(attacking_troops) == 0:
                in_combat = False

        for _unit in defending_troops:
            # If defender unit has no soldiers
            if _unit.soldiers <= 0:
                defending_troops.remove(_unit)
            # If defender has no more units
            if len(defending_troops) == 0:
                in_combat = False
                move_enemy_to_garrison(file, attacking_troops)


def move_enemy_to_garrison(file, attacking_troops):
    file.movement_end.faction = file.movement_start.faction
    file.movement_end.troops_present = attacking_troops
    file.movement_end.enemies_present = []



