
class PlayerTemplate:
    def __init__(self, AI_Bot = True):
        self.ai_player = AI_Bot
        self.credits = 1000
        self.expenses = 0
        self.income = 1000
        self.faction = None
        self.controller = None
        if self.ai_player:
            self.controller = self.AiController
        else:
            self.controller = self.HumanController

    class AiController:
        def __int__(self):
            pass
        def play_turn(self):
            print("AI assesses field and makes turn")


    class HumanController:
        def __init__(self):
            pass
