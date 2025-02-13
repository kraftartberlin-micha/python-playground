import game_manager
from games.tictactoe import Tictactoe
from game_collection import GameCollection

gameCollection = GameCollection()
gameCollection.add_game(Tictactoe())
game_manager.GameManager.run(gameCollection)
