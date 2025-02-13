from games.game import Game


class GameCollection:
    """
    A collection of Game objects only
    """
    __games__ = []

    def add_game(self, game: Game) -> None:
        self.__games__.append(game)

    def get_all_games(self) -> list:
        return self.__games__
