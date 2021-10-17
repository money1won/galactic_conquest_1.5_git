from PyQt5 import QtCore, QtGui, QtWidgets
# Where buttons are linked to.
import numpy as np

from galactic_conquest_1_2.game.general_functions import movement

def planet_view(file, planet):
    _ui = file.application.ui
    _ui.planetName_Label.setText(planet.name)
    _ui.PageSelector.setCurrentIndex(file.screen_Dictionary["Planet"])
    file.active_planet = planet
    pass

def ground_view(file, planet):
    _ui = file.application.ui
    _ui.garrisonGround_List.clear()
    _ui.enemyGround_List.clear()
    _ui.outboundGround_List.clear()
    _ui.PageSelector.setCurrentIndex(file.screen_Dictionary["PlanetGround"])
    for _unit in planet.troops_present:
        #if _unit.faction.name == planet.faction.name:
        _ui.garrisonGround_List.addItem(str(_unit.name))

        #else:
         #   _ui.enemyGround_List.addItem(str(_unit.name))

    for _unit in planet.outbound_troops:
        _ui.outboundGround_List.addItem(str(_unit.name))

    for _unit in planet.enemies_present:
        _ui.enemyGround_List.addItem(str(_unit.name))

    if planet.faction.name == file.turn_manager.order[0].faction.name:
            print("players planet")
            _ui.garrisonGround_List.setEnabled(True)
            _ui.outboundGround_Button.setEnabled(True)
            _ui.garrisonGround_Button.setEnabled(True)
    else:
        print("non-controlled planet")
        _ui.garrisonGround_List.setEnabled(False)
        _ui.outboundGround_Button.setEnabled(False)
        _ui.garrisonGround_Button.setEnabled(False)


def return_to_planet_view(file):
    _ui = file.application.ui
    _ui.PageSelector.setCurrentIndex(file.screen_Dictionary["Planet"])
    refresh_unit_list(file)

def refresh_unit_list(file):
    _ui = file.application.ui
    _ui.garrisonGround_List.clear()
    _ui.enemyGround_List.clear()
    _ui.outboundGround_List.clear()
    # ground_view(file, file.active_planet)
    for _unit in file.active_planet.troops_present:
        if _unit.faction.name == file.active_planet.faction.name:
            _ui.garrisonGround_List.addItem(str(_unit.name))

        else:
            _ui.enemyGround_List.addItem(str(_unit.name))
    for _unit in file.active_planet.outbound_troops:
        _ui.outboundGround_List.addItem(str(_unit.name))

def move_to_outbound(file):
    _ui = file.application.ui
    _unit_widgets = _ui.garrisonGround_List.selectedItems()
    _moved_units = []
    # print("Unit Names: " + str(_unit_widgets))
    for _unit in file.active_planet.troops_present:
        for _unit_name in _unit_widgets:
            if _unit.name == _unit_name.text():
                _moved_units.append(_unit)
                file.active_planet.outbound_troops.append(_unit)
                # file.active_planet.outbound_troops.append(file.active_planet.troops_present.pop(file.active_planet.troops_present.index(_unit)))

    for _unit in _moved_units:
        file.active_planet.troops_present.remove(_unit)

    refresh_unit_list(file)

    # todo fix this
    # print("ck1")
    # file.active_planet.outbound_troops = np.concatenate((file.active_planet.outbound_troops, _moved_units))
    # file.active_planet.troops_present = np.delete(file.active_planet.troops_present, _moved_units)
    # print(file.active_planet.outbound_troops)
    # print(file.active_planet.troops_present)



    # file.active_planet.troops_present.remove(_moved_units)
    # _arr1 = np.concatenate(file.active_planet.outbound_troops, _moved_units)
    #
    # # print(file.active_planet.troops_present)
    # print(_arr1)
    #
    # # file.active_planet.troops_present.remove(_items)
    pass

def move_to_garrison(file):
    _ui = file.application.ui
    _unit_widgets = _ui.outboundGround_List.selectedItems()
    _moved_units = []
    # print("Unit Names: " + str(_unit_widgets))
    for _unit in file.active_planet.outbound_troops:
        for _unit_name in _unit_widgets:
            if _unit.name == _unit_name.text():
                _moved_units.append(_unit)
                file.active_planet.troops_present.append(_unit)
                # file.active_planet.outbound_troops.append(file.active_planet.troops_present.pop(file.active_planet.troops_present.index(_unit)))

    for _unit in _moved_units:
        file.active_planet.outbound_troops.remove(_unit)

    refresh_unit_list(file)

def movement_selector(file, planet):
    if file.movement_start is None:
        file.movement_start = planet
        print("Starting planet: " + str(file.movement_start.name))
    else:
        file.movement_end = planet
        print("Ending planet: " + str(file.movement_end.name))
        movement(file)
        file.movement_start = None
        file.movement_end = None
        pass