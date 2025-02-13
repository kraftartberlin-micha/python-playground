class GameInput:
    """
    class to read and validate user inputs
    """

    MSG_WRONG_INPUT = "Falsche Eingabe für {0}."
    MSG_CHOOSE_TURN = "Spieler {0}, wähle deine {1} (0-2)"

    row_name = 'Zeile'
    column_name = 'Spalte'

    @staticmethod
    def getUserInput(current_player: str, row: bool = True) -> int:
        typ = GameInput.__getTypeString__(row)
        confirm_text = GameInput.__getConfirmString__(current_player, typ)
        user_input = int(input(confirm_text))
        if GameInput.__is_input_wrong__(user_input):
            raise Exception(GameInput.MSG_WRONG_INPUT.format(typ))
        return user_input

    @staticmethod
    def __getTypeString__(row: bool) -> str:
        selection = GameInput.row_name if row else GameInput.column_name
        return selection

    @staticmethod
    def __getConfirmString__(current_player: str, typ: str) -> str:
        return GameInput.MSG_CHOOSE_TURN.format(current_player, typ)

    @staticmethod
    def __is_input_wrong__(user_input: int) -> bool:
        return user_input > 2 or user_input < 0
