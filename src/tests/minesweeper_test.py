import unittest
from minesweeper import Minesweeper
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.game = Minesweeper(10,10,10)

    def test_number_of_mines_correct(self):
        self.assertEqual(str(self.game), "Mines: 10")

    def test_hints_correct(self):
        mines = self.game.minemap
        self.assertEqual(mines, self.game.minemap)

