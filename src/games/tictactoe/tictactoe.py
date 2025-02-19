from src.games.game import Game
from src.games.tictactoe.tictactoe_input import TictactoeInput
from src.games.tictactoe.tictactoe_battlefield import TictactoeBattlefield


class Tictactoe(Game):
    """
    Tic Tac Toe Spiel mit einem 3x3 Spielfeld und Spieler X und O
    Jeder darf abwechseln sein Zeichen irgendwo auf das Feld setz
    Bei 3 in einer Reihe gewinnt der Spieler
    Sind alle Felder ohne eine Reihe belegt, endet es unentschieden
    """

    __MSG_TRY_AGAIN__: str = "{0} Versuche es erneut."
    __MSG_WINNER__: str = "Spieler: {0} hat gewonnen!"
    __MSG_NO_WINNER__: str = "Unentschieden!"
    __MSG_THX_BYE__: str = "Danke für das Spielen :)"

    __current_player__: str = "X"
    __first_player__: str = "X"
    __second_player__: str = "O"

    def __init__(self) -> None:
        self.__game_name__ = "Tic Tac Toe"

    def play(self) -> None:
        self.__reset_current_player__()
        battlefield = TictactoeBattlefield()
        battlefield.create_new_game_map()

        while True:
            battlefield.print_game_map()
            try:
                row = TictactoeInput.get_user_input(self.__current_player__)
                column = TictactoeInput.get_user_input(self.__current_player__, False)
                battlefield.fire(self.__current_player__, row, column)
            except BaseException as exception:
                print(self.__MSG_TRY_AGAIN__.format(str(exception)))
                continue
            if battlefield.has_player_won(self.__current_player__):
                battlefield.print_game_map()
                print(self.__MSG_WINNER__.format(self.__current_player__))
                break
            if battlefield.check_end():
                battlefield.print_game_map()
                print(self.__MSG_NO_WINNER__)
                break
            self.__switch_current_player__()
        print(self.__MSG_THX_BYE__)

    def __switch_current_player__(self):
        self.__current_player__ = (
            self.__second_player__
            if self.__current_player__ == self.__first_player__
            else self.__second_player__
        )

    def __reset_current_player__(self) -> None:
        self.__current_player__ = self.__first_player__
