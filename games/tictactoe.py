from games.game import Game
from games.tictactoe_input import GameInput


class Tictactoe(Game):
    """
    Tic Tac Toe Spiel mit einem 3x3 Spielfeld und Spieler X und O
    Jeder darf abwechseln sein Zeichen irgendwo auf das Feld setz
    Bei 3 in einer Reihe gewinnt der Spieler
    Sind alle Felder ohne eine Reihe belegt, endet es unentschieden
    """

    MSG_NOT_EMPTY = 'Feld belegt.'
    MSG_TRY_AGAIN = '{0} Versuche es erneut.'
    MSG_WINNER = 'Spieler: {0} hat gewonnen!'
    MSG_NO_WINNER = 'Unentschieden!'
    MSG_THX_BYE = 'Danke für das Spielen :)'

    current_player = "X"
    first_player = "X"
    second_player = "O"
    battlefield = []

    def __init__(self) -> None:
        self.game_name = 'Tic Tac Toe'

    def play(self) -> None:
        self.__create_new_game_map()
        self.__reset_current_player()

        while True:
            self.__print_game_map()
            try:
                row = GameInput.getUserInput(self.current_player)
                column = GameInput.getUserInput(self.current_player, False)
                self.__fire(self.current_player, row, column)
            except BaseException as exception:
                print(self.MSG_TRY_AGAIN.format(str(exception)))
                continue

            winner = self.__check_hit()
            if winner:
                self.__print_game_map()
                print(self.MSG_WINNER.format(self.current_player))
                break
            if self.__check_end():
                self.__print_game_map()
                print(self.MSG_NO_WINNER)
                break

            self.current_player = self.second_player if self.current_player == self.first_player else self.second_player
        print(self.MSG_THX_BYE)

    def __create_new_game_map(self) -> None:
        self.battlefield = []
        for i in range(3):
            row = [" ", " ", " "]
            self.battlefield.append(row)

    def __print_game_map(self) -> None:
        for row in self.battlefield:
            print("|".join(row))
            print("-----")

    def __fire(self, player, row, column) -> True:
        if self.battlefield[row][column] == " ":
            self.battlefield[row][column] = player
            return True
        raise Exception(self.MSG_NOT_EMPTY)

    def __check_hit(self) -> bool:
        for row in range(3):
            if self.battlefield[row][0] == self.battlefield[row][1] == self.battlefield[row][2] != " ":
                return True
        for column in range(3):
            if self.battlefield[0][column] == self.battlefield[1][column] == self.battlefield[2][column] != " ":
                return True
        if self.battlefield[0][0] == self.battlefield[1][1] == self.battlefield[2][2] != " ":
            return True
        return False

    def __check_end(self) -> bool:
        for row in self.battlefield:
            if " " in row:
                return False
        return True

    def __reset_current_player(self) -> None:
        self.current_player = self.first_player
