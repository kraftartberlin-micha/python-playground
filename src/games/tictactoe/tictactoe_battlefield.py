class TictactoeBattlefield:
    """
    Class for the battlefield with interactions
    """

    __MSG_NOT_EMPTY__ = "Feld belegt."
    __battlefield__: list = []

    def create_new_game_map(self) -> None:
        self.__battlefield__ = []
        for i in range(3):
            row = [" ", " ", " "]
            self.__battlefield__.append(row)

    def print_game_map(self) -> None:
        for row in self.__battlefield__:
            print("|".join(row))
            print("-----")

    def fire(self, player, row, column) -> True:
        if self.__battlefield__[row][column] == " ":
            self.__battlefield__[row][column] = player
            return True
        raise Exception(self.__MSG_NOT_EMPTY__)

    def check_end(self) -> bool:
        for row in self.__battlefield__:
            if " " in row:
                return False
        return True

    def has_player_won(self, player: str) -> bool:
        return (
            self.__has_player_won_horizontal__(player)
            or self.__has_player_won_vertical__(player)
            or self.__has_player_won_diagonal__(player)
        )

    def __has_player_won_diagonal__(self, player: str):
        if (
            self.__battlefield__[0][0]
            == self.__battlefield__[1][1]
            == self.__battlefield__[2][2]
            == player
        ):
            return True
        return False

    def __has_player_won_vertical__(self, player: str):
        for column in range(3):
            if (
                self.__battlefield__[0][column]
                == self.__battlefield__[1][column]
                == self.__battlefield__[2][column]
                == player
            ):
                return True
        return False

    def __has_player_won_horizontal__(self, player):
        for row in range(3):
            if (
                self.__battlefield__[row][0]
                == self.__battlefield__[row][1]
                == self.__battlefield__[row][2]
                == player
            ):
                return True
        return False
