def update_map(file):
    # Set the color of the faction label and ensure the correct faction name is showing
    for planet in file.planets:
        _faction = planet.faction
        planet.ui.mapPlanetFaction_Label.setStyleSheet(f'color: {_faction.color}')
        planet.ui.mapPlanetFaction_Label.setText(_faction.name)

def update_troops_listing(file, planet):
    _ui = file.application.ui
    _ui.garrisonGround_List.clear()
    _ui.enemyGround_List.clear()
    _ui.outboundGround_List.clear()

    for _unit in planet.troops_present:
        _ui.garrisonGround_List.addItem(str(_unit.name))

    for _unit in planet.outbound_troops:
        _ui.outboundGround_List.addItem(str(_unit.name))

    for _unit in planet.enemies_present:
        _ui.enemyGround_List.addItem(str(_unit.name))