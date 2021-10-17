from galactic_conquest_1_2.game.button_functions import planet_view, ground_view, return_to_planet_view, move_to_garrison, move_to_outbound, movement_selector
# Links all buttons in game to the respective code that they work with

# Sample button click code
def button_links(file):
    #todo must add all buttons
    _ui = file.application.ui
    # _ui.mapPlanet1_Button_4.clicked.connect(lambda: test(1))
    map_links(file, _ui)
    planet_links(file, _ui)
    planet_ground_links(file, _ui)

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




def planet_links(file, _ui):
    _ui.backPlanet_Button.clicked.connect(lambda: file.application.ui.PageSelector.setCurrentIndex(file.screen_Dictionary["Map"]))
    _ui.groundPlanet_Button.clicked.connect(lambda: ground_view(file, file.active_planet))
    _ui.backGround_Button.clicked.connect(lambda: return_to_planet_view(file))

def planet_ground_links(file, _ui):
    _ui.outboundGround_Button.clicked.connect(lambda: move_to_outbound(file))
    _ui.garrisonGround_Button.clicked.connect(lambda: move_to_garrison(file))
    pass