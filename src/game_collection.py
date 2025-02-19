from src.games.game import Game


class GameCollection:
    """
    A collection of Game objects only
    """

    __games__: list = []

    def __init__(self):
        __games__: list = []

    def add_game(self, game: Game) -> None:
        self.__games__.append(game)

    def get_all_games(self) -> list:
        return self.__games__

    def len(self) -> int:
        return len(self.__games__)
