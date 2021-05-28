import unittest
import os
from minesweeper import Minesweeper
os.environ["SDL_VIDEODRIVER"] = "dummy"

class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.game = Minesweeper(10,10,10)

    def test_number_of_mines_correct(self):
        self.assertEqual(str(self.game), "Mines: 10")

    def test_hints_correct(self):
        self.game.place_hints(10,10)
        h = len(self.game.minemap)
        w = len(self.game.minemap[0])
        result = True
        for j in range(0,h):
            for i in range(0,w): # j = y, i = x
                mines = 0
                if 0 < self.game.minemap[j][i] < 10: # (y-1,x-1);(y-1,x);(y-1,x+1);(y,x-1);(y,x+1);(y+1,x-1);(y+1,x);(y+1,x+1)
                    if j-1 >= 0 and i-1 >= 0:
                        if self.game.minemap[j-1][i-1] == 10:
                            mines += 1
                    if j-1 >= 0:
                        if self.game.minemap[j-1][i] == 10:
                            mines += 1
                    if j-1 >= 0 and i+1 < w:
                        if self.game.minemap[j-1][i+1] == 10:
                            mines += 1
                    if i-1 >= 0:
                        if self.game.minemap[j][i-1] == 10:
                            mines += 1
                    if i+1 < w:
                        if self.game.minemap[j][i+1] == 10:
                            mines += 1
                    if j+1 < h and i-1 >= 0:
                        if self.game.minemap[j+1][i-1] == 10:
                            mines += 1
                    if j+1 < h:
                        if self.game.minemap[j+1][i] == 10:
                            mines += 1
                    if j+1 < h and i+1 < w:
                        if self.game.minemap[j+1][i+1] == 10:
                            mines += 1
                if mines != self.game.minemap[j][i]:
                    print(mines, self.game.minemap[j][i])
                    result = False
                    break
        self.assertEqual(result, True)
        