from galactic_conquest_1_2.game.defaults.player_default import PlayerTemplate

class TurnManager:
    def __init__(self, file):
        self.current_player = 0
        self.total_players = file.total_players_generated
        self.order = self.determine_order(file)

    def determine_order(self, file):
        _players = file.players
        _human_players = []
        _ai_players = []
        _order = []
        # find all human players
        for _player in _players:
            if file.players == PlayerTemplate.HumanController:
                _human_players.append(_player)
            else:
                _ai_players.append(_player)
        _order = _human_players + _ai_players
        return _order

    def iterate_turns(self, file):
        if self.current_player == file.total_players_generated-1:
            self.current_player = 0
        else:
            self.current_player += 1
        if self.order[self.current_player].controller == PlayerTemplate.HumanController:
            # find out if you're that player and enable all buttons
            print("player's turn!")
        else:
            # disable all buttons and rotate through the AI
            print("AI's turn: " + str(self.current_player))
            self.order[self.current_player].controller.play_turn(file)
            self.iterate_turns(file)
        pass

