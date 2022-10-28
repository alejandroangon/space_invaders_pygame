from pyclbr import Class


class Statistics():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings;
        self.reset_stats();
        #initialize an active state
        self.game_active = False;

        #Highest score
        self.high_score = 0;

    def reset_stats(self):
        self.remain_ships = self.ai_settings.ships_amount;
        self.score = 0;
        self.level = 1;