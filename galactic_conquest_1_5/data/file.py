from galactic_conquest_1_2.game.defaults.planet_default import PlanetTemplate
from galactic_conquest_1_2.game.defaults.faction_default import FactionTemplate
from galactic_conquest_1_2.game.defaults.player_default import PlayerTemplate
from galactic_conquest_1_2.game.turn_manager import TurnManager


# available colors here:
# https://www.quackit.com/css/css_color_codes.cfm#:~:text=Basic%20CSS%20Colors%20%20%20%20Color%20Name,%20%200%2C128%2C128%20%202%20more%20rows%20

class File:
    def __init__(self):
        # Instantiate the players
        self.players = []
        self.application = None  # UI loaded here

        # Faction pool
        self.factions = []

        self.factions.append(FactionTemplate())
        self.factions[0].name = "Galactic Alliance"
        self.factions[0].owning_player = None
        self.factions[0].color = 'DarkGreen'

        self.factions.append(FactionTemplate())
        self.factions[1].name = "Rebellion"
        self.factions[1].owning_player = None
        self.factions[1].color = 'DarkRed'

        # A player is defined as a human or AI that controls a united group
        self.total_players_generated = 8
        self.human_players = 1

        if self.human_players >= 1:
            self.players.append(PlayerTemplate(False))
            self.players[0].faction = FactionTemplate
            self.players[0].faction.name = "Galactic Alliance"

        for index in range(0, self.total_players_generated-self.human_players):
            self.players.append(PlayerTemplate())
            pass

        # Instantiate the planets
        self.planets = []
        self.active_planet = None

        # generate planets into an array
        self.total_planets_generated = 100  # Max reasonable amount for reasonable distance is 135 planets w/ 200d
        self.planet_distance = 200
        self.planet_distance_neighbor = 5000
        for index in range(0, self.total_planets_generated):
            self.planets.append(PlanetTemplate(self.application))
            pass

        self.active_planet = None

        self.turn_manager = TurnManager(self)

        # Starting condictions data



        # Define what each screen is here as it will not change
        # Dictionary helps to easily identify to programmer what screen is being displayed with a numerical identifier assigned to it
        # Must update everytime you add a new screen so it can track its ID number. Should match in QT Designer
        self.screen_Dictionary = {
            "Menu": 0,
            "Map": 1,
            "Planet": 2,
            "PlanetGround": 3
        }

        # Movement
        self.movement_start = None
        self.movement_end = None