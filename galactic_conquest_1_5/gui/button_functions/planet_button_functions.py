from galactic_conquest_1_5.game.update_functions import update_troops_listing

def ground_view(file, planet):
    update_troops_listing(file, planet)
    _ui = file.application.ui
    _ui.PageSelector.setCurrentIndex(file.screen_Dictionary["PlanetGround"])

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

