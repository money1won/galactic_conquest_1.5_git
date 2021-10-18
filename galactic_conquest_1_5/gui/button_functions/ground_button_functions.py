from galactic_conquest_1_5.game.update_functions import update_troops_listing


def return_to_planet_view(file):
    _ui = file.application.ui
    _ui.PageSelector.setCurrentIndex(file.screen_Dictionary["Planet"])


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
    update_troops_listing(file, file.active_planet)


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
    update_troops_listing(file, file.active_planet)
