from galactic_conquest_1_5.gui.button_functions.map_button_functions import planet_view, movement_selector
# Links all buttons in game to the respective code that they work with
from galactic_conquest_1_5.gui.button_functions.planet_button_functions import ground_view
from galactic_conquest_1_5.gui.button_functions.ground_button_functions import return_to_planet_view, move_to_outbound, move_to_garrison
from galactic_conquest_1_5.gui.button_links.map_links import map_links
from galactic_conquest_1_5.gui.button_links.planet_links import planet_links
from galactic_conquest_1_5.gui.button_links.ground_links import ground_links

# Sample button click code
def button_links(file):
    #todo must add all buttons
    _ui = file.application.ui
    # _ui.mapPlanet1_Button_4.clicked.connect(lambda: test(1))
    map_links(file, _ui)
    planet_links(file, _ui)
    ground_links(file, _ui)