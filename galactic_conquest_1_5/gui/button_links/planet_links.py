from galactic_conquest_1_5.gui.button_functions.planet_button_functions import ground_view
from galactic_conquest_1_5.gui.button_functions.ground_button_functions import return_to_planet_view

def planet_links(file, _ui):
    _ui.backPlanet_Button.clicked.connect(lambda: file.application.ui.PageSelector.setCurrentIndex(file.screen_Dictionary["Map"]))
    _ui.groundPlanet_Button.clicked.connect(lambda: ground_view(file, file.active_planet))
    _ui.backGround_Button.clicked.connect(lambda: return_to_planet_view(file))