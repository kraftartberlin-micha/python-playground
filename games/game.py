class Game():
    """
    Eltern-Klasse für Spiele des GameManagers
    """

    game_name = ''

    def __init__(self) -> None:
        self.game_name = 'StandardName'

    def play(self) -> None:
        """
        Method must be defined in subclass
        """
        raise Exception('Missing implementation')
