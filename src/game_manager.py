from src.game_collection import GameCollection
from src.games.game import Game


class GameManager:
    """
    Display a list of games and prompt the user to start a game
    A GameCollection Object is required to run the Manager
    """

    __MSG_GAME_OVERVIEW__: str = "Folgende Spiele sind verfügbar:"
    __MSG_ASK_SINGLE_GAME__: str = "Möchtest du {0} spielen? (ja)"
    __MSG_ASK_CHOICE_GAME__: str = "Bitte wähle ein Spiel! (1 - {0})"
    __MSG_NO_GAMES__: str = "Derzeit leider keine Spiele vorhanden"
    __MSG_BAD_INPUT__: str = "Falsche Eingabe"
    __MSG_START_GAME__: str = "{0} wird gestartet"
    __MSG_USER_EXIT__: str = "User dont want to play. Manager closed."
    __MSG_EXIT__: str = "Gaming stopped. Manager closed."

    @staticmethod
    def run(games: GameCollection) -> None:
        """
        this will run the prompt manager to ask for game to start
        """
        while True:
            try:
                GameManager.__start_manager__(games)
                break
            except (RuntimeError, UserWarning) as exception:
                print(str(exception))
                break
            except TypeError as exception:
                print(str(exception))
                continue
            except object as obj:
                print(str(obj))
                break

    @staticmethod
    def __start_manager__(game_collection: GameCollection) -> None:
        print(GameManager.__MSG_GAME_OVERVIEW__)

        GameManager.__ensure_games_loaded__(game_collection)

        GameManager.__display_all_games__(game_collection)
        selected_game = GameManager.__ask_user_and_get_game(game_collection)

        print(GameManager.__MSG_START_GAME__.format(selected_game.get_game_name()))
        selected_game.play()

    @staticmethod
    def __ensure_games_loaded__(game_collection: GameCollection):
        if game_collection.len() == 0:
            raise RuntimeError(GameManager.__MSG_NO_GAMES__)

    @staticmethod
    def __display_all_games__(game_collection: GameCollection) -> None:
        counter: int = 0
        for game in game_collection.get_all_games():
            counter += 1
            print(str(counter) + ". " + game.get_game_name())

    @staticmethod
    def __ask_user_and_get_game(game_collection):
        games_counter: int = game_collection.len()
        if games_counter > 1:
            choice: int = GameManager.__get_choice_from_user__(games_counter)
            selected_game: Game = game_collection.get_all_games()[choice - 1]
        else:
            selected_game: Game = game_collection.get_all_games()[0]
            GameManager.__ask_user_want_play__(selected_game)
        return selected_game

    @staticmethod
    def __get_choice_from_user__(counter: int) -> int:
        choice: int = int(
            input(GameManager.__MSG_ASK_CHOICE_GAME__.format(str(counter)))
        )
        if choice > counter or choice < 1:
            raise TypeError(GameManager.__MSG_BAD_INPUT__)
        return choice

    @staticmethod
    def __ask_user_want_play__(game: Game) -> True:
        confirm: str = input(
            GameManager.__MSG_ASK_SINGLE_GAME__.format(game.get_game_name())
        )
        if not confirm == "" and not confirm == "ja":
            raise UserWarning(GameManager.__MSG_USER_EXIT__)
        return True
