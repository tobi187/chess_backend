import dataclasses


@dataclasses.dataclass
class Game:
    game_key: str
    player1: any
    player2: any
    current_move = 0
    gamestate = []

    def get_players(self):
        return [self.player1, self.player1]

    def init_game(self):
        pass
