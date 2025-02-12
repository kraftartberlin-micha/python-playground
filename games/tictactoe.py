from games.game import Game
from games.tictactoe_input import Gameinput

class Tictactoe(Game):

    MSG_NOT_EMPTY = 'Feld belegt.'
    MSG_TRY_AGAIN = '{0} Versuche es erneut.'
    MSG_WINNER = 'Spieler: {0} hat gewonnen!'
    MSG_NO_WINNER = 'Unentschieden!'
    MSG_THX_BYE = 'Danke für das Spielen :)'

    current_player = "X"
    first_player = "X"
    second_player = "O"

    gameMap = []

    def play(self):
        self.__create_new_game_map()
        self.__reset_current_player()

        while True:
            self.__print_game_map()
            try:
                row = Gameinput.getUserInput(self.current_player)
                column = Gameinput.getUserInput(self.current_player, False)
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

    def __create_new_game_map(self):
        self.gameMap = []
        for i in range(3):
            row = [" ", " ", " "]
            self.gameMap.append(row)

    def __print_game_map(self):
        for row in self.gameMap:
            print("|".join(row))
            print("-----")

    def __fire(self,player, row, column):
        if self.gameMap[row][column] == " ":
            self.gameMap[row][column] = player
            return True
        raise Exception(self.MSG_NOT_EMPTY)

    def __check_hit(self):
        for row in range(3):
            if self.gameMap[row][0] == self.gameMap[row][1] == self.gameMap[row][2] != " ":
                return True
        for column in range(3):
            if self.gameMap[0][column] == self.gameMap[1][column] == self.gameMap[2][column] != " ":
                return True
        if self.gameMap[0][0] == self.gameMap[1][1] == self.gameMap[2][2] != " ":
            return True
        return False

    def __check_end(self):
        for row in self.gameMap:
            if " " in row:
                return False
        return True

    def __reset_current_player(self):
        self.current_player = self.first_player