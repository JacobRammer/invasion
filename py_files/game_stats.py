# TODO add high scores to a text file to be store between executions
#   since high score is set to 0 on each startup, need to ask if user wants to load values


class GameStats():
    """tracking statistics for invasion"""

    def __init__(self, ai_settings):
        """initialize statistics """

        self.ai_settings = ai_settings
        self.reset_stats()

        # start game in inactive state
        self.game_active = False

        # high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
