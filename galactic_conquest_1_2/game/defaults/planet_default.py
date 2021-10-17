
class PlanetTemplate:
    def __init__(self, ui):
        self.faction = "_"
        self.fleet_present = []  # Container for all ships present
        self.name = "Default"
        self.size = 1
        self.troops_present = []  # Container for all troops on the planet
        self.enemies_present = []
        self.outbound_troops = []
        self.outbound_ships = []
        self.x = 0
        self.y = 0

        self.ui = None