def update_map(file):
    # Set the color of the faction label and ensure the correct faction name is showing
    for planet in file.planets:
        _faction = planet.faction
        planet.ui.mapPlanetFaction_Label.setStyleSheet(f'color: {_faction.color}')
        planet.ui.mapPlanetFaction_Label.setText(_faction.name)

