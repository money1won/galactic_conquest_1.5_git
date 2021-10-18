from galactic_conquest_1_5.gui.button_functions.map_button_functions import planet_view, movement_selector

def map_links(file, _ui):
    _ui.mapEndTurn_Button.clicked.connect(lambda: file.turn_manager.iterate_turns(file))

    class _Link_Function_Instances:
        def __init__(self, file, planet):
            pass
        def _method(self, file, planet):
            planet.ui.mapPlanet_Button.clicked.connect(lambda: planet_view(file, planet))
            planet.ui.mapPlanetAssault_Button.clicked.connect(lambda: movement_selector(file, planet))

    for planet in file.planets:
        _link_command = _Link_Function_Instances(file, planet)
        _link_command._method(file, planet)
        # planet.ui.mapPlanet_Button.clicked.connect(planet_view(file, file.planets[0]))

