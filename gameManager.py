import importlib

class Gamemanager:
    """Manager to play games"""

    MSG_GAME_OVERVIEW = "Folgende Spiele sind verfügbar:"
    MSG_ASK_SINGLE_GAME = "Möchtest du {0} spielen? (ja)"
    MSG_ASK_CHOICE_GAME = "Bitte wähle ein Spiel! (1 - {0})"
    MSG_NO_GAMES = "Derzeit leider keine Spiele vorhanden"
    MSG_BAD_INPUT = "Falsche Eingabe"
    MSG_START_GAME = "{0} wird gestartet"

    @staticmethod
    def run(games):

        print(Gamemanager.MSG_GAME_OVERVIEW)
        counter = Gamemanager.count_games(games)

        if counter == 0:
            print(Gamemanager.MSG_NO_GAMES)
            exit()
        if counter > 1:
            choice = input(Gamemanager.MSG_ASK_CHOICE_GAME.format(str(counter)))
            if int(choice) > counter or int(choice) < 1:
                print(Gamemanager.MSG_BAD_INPUT)
                exit()
        else:
            choice = input(Gamemanager.MSG_ASK_SINGLE_GAME.format(games[0]["name"]))
            if not choice == "" and not choice == "ja":
                exit()

        print(Gamemanager.MSG_START_GAME.format(games[counter - 1]["name"]))
        imported_game = type(games[counter - 1]["class"], (), dict(a=1))
        imported_game().play()

    @staticmethod
    def count_games(games):
        counter=0
        for game in games:
            counter += 1
            print(str(counter) + ". " + game["name"])
        return counter