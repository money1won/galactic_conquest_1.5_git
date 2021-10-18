from PyQt5 import QtCore, QtGui, QtWidgets
# Where buttons are linked to.

from galactic_conquest_1_5.game.general_functions import movement


def planet_view(file, planet):
    _ui = file.application.ui
    _ui.planetName_Label.setText(planet.name)
    _ui.PageSelector.setCurrentIndex(file.screen_Dictionary["Planet"])
    file.active_planet = planet


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
