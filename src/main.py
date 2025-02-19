from src.game_manager import GameManager
from src.game_collection import GameCollection
from src.games.tictactoe.tictactoe import Tictactoe

gameCollection = GameCollection()
gameCollection.add_game(Tictactoe())
GameManager.run(gameCollection)
