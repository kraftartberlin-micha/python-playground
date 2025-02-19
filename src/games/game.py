class Game:
    """
    Eltern-Klasse für Spiele des GameManagers
    """

    __game_name__: str = ""

    def __init__(self) -> None:
        self.__game_name__ = "StandardName"

    def play(self) -> None:
        """
        Method must be defined in subclass
        """
        raise Exception("Missing implementation")

    def get_game_name(self) -> str:
        return self.__game_name__
