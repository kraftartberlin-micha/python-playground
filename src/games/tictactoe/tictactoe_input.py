class TictactoeInput:
    """
    class to read and validate user inputs
    """

    __MSG_WRONG_INPUT__: str = "Falsche Eingabe für {0}."
    __MSG_CHOOSE_TURN__: str = "Spieler {0}, wähle deine {1} (0-2)"

    __row_name__: str = "Zeile"
    __column_name__: str = "Spalte"

    @staticmethod
    def get_user_input(current_player: str, row: bool = True) -> int:
        typ = TictactoeInput.__getTypeString__(row)
        user_input = int(
            input(TictactoeInput.__MSG_CHOOSE_TURN__.format(current_player, typ))
        )
        if TictactoeInput.__is_input_wrong__(user_input):
            raise Exception(TictactoeInput.__MSG_WRONG_INPUT__.format(typ))
        return user_input

    @staticmethod
    def __getTypeString__(row: bool) -> str:
        selection = (
            TictactoeInput.__row_name__ if row else TictactoeInput.__column_name__
        )
        return selection

    @staticmethod
    def __is_input_wrong__(user_input: int) -> bool:
        return user_input > 2 or user_input < 0
