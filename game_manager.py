from game_collection import GameCollection


class GameManager:
    """
    Display a list of games and prompt the user to start a game
    A GameCollection Object is required to run the Manager
    """

    MSG_GAME_OVERVIEW = 'Folgende Spiele sind verfügbar:'
    MSG_ASK_SINGLE_GAME = 'Möchtest du {0} spielen? (ja)'
    MSG_ASK_CHOICE_GAME = 'Bitte wähle ein Spiel! (1 - {0})'
    MSG_NO_GAMES = 'Derzeit leider keine Spiele vorhanden'
    MSG_BAD_INPUT = 'Falsche Eingabe'
    MSG_START_GAME = '{0} wird gestartet'
    MSG_USER_EXIT = 'User dont want to play. Manager closed.'
    MSG_EXIT = 'Gaming stopped. Manager closed.'

    @staticmethod
    def run(games: GameCollection) -> None:
        """
        this will run the prompt manager to ask for game to start
        """
        while True:
            try:
                GameManager.__start_manager__(games)
                break
            except (RuntimeError, UserWarning) as e:
                print(str(e))
                break
            except (TypeError) as e:
                print(str(e))
                continue

    @staticmethod
    def __start_manager__(games: GameCollection) -> None:
        print(GameManager.MSG_GAME_OVERVIEW)
        all_games = games.get_all_games()
        counter = GameManager.__count_games__(all_games)
        choice = GameManager.__get_choice_from_user__(all_games, counter)
        selected_game = all_games[choice - 1]
        print(GameManager.MSG_START_GAME.format(selected_game.game_name))
        selected_game.play()

    @staticmethod
    def __count_games__(all_games: list) -> int:
        counter = 0
        for game in all_games:
            counter += 1
            print(str(counter) + ". " + game.game_name)
        return counter

    @staticmethod
    def __get_choice_from_user__(all_games, counter: int) -> int:
        if counter == 0:
            raise RuntimeError(GameManager.MSG_NO_GAMES)
        if counter > 1:
            choice = int(input(GameManager.MSG_ASK_CHOICE_GAME.format(str(counter))))
            if choice > counter or choice < 1:
                raise TypeError(GameManager.MSG_BAD_INPUT)
        else:
            choice = input(GameManager.MSG_ASK_SINGLE_GAME.format(all_games[0].game_name))
            if not choice == "" and not choice == "ja":
                raise UserWarning(GameManager.MSG_USER_EXIT)
            choice = 1
        return choice
