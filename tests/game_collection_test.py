import unittest
from unittest.mock import Mock

from src.game_collection import GameCollection
from src.games.game import Game


class MyTestCase(unittest.TestCase):
    def test_len_will_return_amount_of_items(self):
        game_mock: Game = Mock(Game)
        count: int = 5

        collection: GameCollection = GameCollection()
        for i in range(count):
            collection.add_game(game_mock)

        self.assertEqual(count, collection.len())

    def test_len_will_return_amount_of_items_also_when_empty(self):
        collection: GameCollection = GameCollection()
        # todo: test fail when run both tests.
        #  new object has the filled attribute from object before like a static class?
        #  i missed something in python logic
        self.assertEqual(0, collection.len())


if __name__ == "__main__":
    unittest.main()
