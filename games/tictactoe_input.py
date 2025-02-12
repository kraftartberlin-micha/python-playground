class Gameinput:
    """class to read and validate user inputs"""
    @staticmethod
    def getType(row):
        selection = 'Zeile' if row else 'Spalte'
        return selection

    @staticmethod
    def getConfirmString(aktueller_spieler, typ):
        return f"Spieler {aktueller_spieler}, wähle deine {typ} (0-2)"


    @staticmethod
    def is_input_wrong(user_eingabe):
        return user_eingabe > 2 or user_eingabe < 0


    @staticmethod
    def getUserInput(aktueller_spieler, row = True):
        typ = Gameinput.getType(row)
        confirm_text = Gameinput.getConfirmString(aktueller_spieler, typ)
        user_input = int(input(confirm_text))
        if Gameinput.is_input_wrong(user_input):
            raise Exception(f"Falsche Eingabe für {typ}.")
        return user_input
