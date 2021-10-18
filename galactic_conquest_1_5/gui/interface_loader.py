from galactic_conquest_1_5.gui.create_window import CreateMyWindow
from galactic_conquest_1_5.gui.planet_generation import add_planets_to_map
from galactic_conquest_1_5.gui.button_links import button_links
from galactic_conquest_1_5.data.initialize_start_conditions import create_starting_garrisons
from galactic_conquest_1_5.gui.button_links.button_links import *

# https://stackoverflow.com/questions/4008649/qlistwidget-and-multiple-selection

from PyQt5 import QtWidgets
from galactic_conquest_1_5.game.update_functions import update_map
import sys

def load_interface(file):
    # Initialize application
    app = QtWidgets.QApplication(sys.argv)
    application = CreateMyWindow()
    file.application = application

    # Generate planets
    add_planets_to_map(file, file.application.ui)
    update_map(file)

    # Create initial garrison units for the map
    create_starting_garrisons(file)

    # Give buttons functionality
    button_links(file)

    # Set this window to the starting point. Mostly for debugging, otherwise set to "Main Menu"
    file.application.ui.PageSelector.setCurrentIndex(file.screen_Dictionary["Map"])








    # No edits below
    application.show()
    # application.showFullScreen()  # For fullscreen, #todo change when publishing
    sys.exit(app.exec_())



    # References
    # Allows multi selection
    # file.application.ui.garrisonGround_List.setSelectionMode(2)
    # items = ui.listWidget.selectedItems()