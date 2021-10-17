from galactic_conquest_1_2.gui.pyqt_py3_gui_files.planet_interface_file import Ui_Form
from galactic_conquest_1_2.game.update_functions import update_map
from random import *
from math import *


from PyQt5 import QtCore

# Takes the active file and application window as arguments
def add_planets_to_map(file, application):
    for currently_generated_planet in range(0, file.total_planets_generated):
        # PlanetUI is the UI code for generated planets
        file.planets[currently_generated_planet].ui = Ui_Form()
        file.planets[currently_generated_planet].ui.setupUi(application)

        # Assign names to the planets
        # _planet_name = self.file.planets[currently_generated_planet].name
        _planet_name = PlanetNames()  # Giving random names for now, use line above
        file.planets[currently_generated_planet].ui.mapPlanetName_Label.setText(_planet_name)
        file.planets[currently_generated_planet].name = _planet_name
        # self.file.planets[currently_generated_planet].ui.mapPlanetName_Label.setStyleSheet('color: green')

        # Determine Coordinates of the planets
        _planet_minimum_placed = False
        planet_maximum_placed = False
        while not _planet_minimum_placed:
            _minimum_tripped = False
            _x = randint(0, 4800)  # Giving random coords for now
            _y = randint(0, 1550)  # Giving random coords for now
            # Update the location of the planet GUI frame
            file.planets[currently_generated_planet].ui.planet_Frame.setGeometry(QtCore.QRect(_x, _y, 141, 121))

            # For all planets that were generated
            for compared_planet in file.planets:
                # Find the distance between this planet and any other planet
                _x_difference = compared_planet.x - _x
                _y_difference = compared_planet.y - _y
                if abs(sqrt(_x_difference ** 2 + _y_difference ** 2)) < file.planet_distance:
                    _minimum_tripped = True
            # If distance is too small to any other planet, start the loop again and try again
            if _minimum_tripped:
                _planet_minimum_placed = False
            else:
                # print("Planet Generated")
                file.planets[currently_generated_planet].x = _x
                file.planets[currently_generated_planet].y = _y
                _planet_minimum_placed = True

        # Determine Factions of the planets
        _faction = choice(file.factions)
        file.planets[currently_generated_planet].faction = _faction

def PlanetNames():

    names = [
        "location 1",
        "location 2",
        "location 3",
        "location 4",
        "location 5",
        "location 6",
        "location 7",
        "location 8",
        "location 9",
        "location 10",
        "location 11",
        "location 12",
        "location 13",
        "location 14",
        "location 15",
    ]
    name = choice(names)

    return name
