'''
This Was Authored by:
    - Nir Tuttnauer
    - Tomer Mizrahi
'''

import unittest
from disjoint_set import DisjointSet
from hexgame import HexGame

class TestHexGame(unittest.TestCase):
    """
    A test case for the HexGame class.
    """

    def test_initialize_game(self):
        """
        Test the initialization of the HexGame class.
        """
        game = HexGame(11)
        self.assertEqual(game.n, 11)
        self.assertEqual(len(game.board), 11)
        self.assertEqual(len(game.board[0]), 11)
        self.assertEqual(len(game.cells), 121)
        self.assertEqual(game.top_node, (-1, 0))
        self.assertEqual(game.bottom_node, (11, 0))
        self.assertEqual(game.left_node, (0, -1))
        self.assertEqual(game.right_node, (0, 11))
        self.assertIsInstance(game.ds_red, DisjointSet)
        self.assertIsInstance(game.ds_blue, DisjointSet)

    def test_make_move(self):
        """
        Test the _make_move method of the HexGame class.
        """
        game = HexGame(3)
        game._make_move(0, 0, 'red')
        self.assertEqual(game.board[0][0], 1)
        game._make_move(1, 1, 'blue')
        self.assertEqual(game.board[1][1], 2)

    def test_check_winner_red(self):
        """
        Test the _check_winner method of the HexGame class for the 'red' player.
        """
        game = HexGame(3)
        game._make_move(0, 0, 'red')
        game._make_move(1, 0, 'red')
        game._make_move(2, 0, 'red')
        print('---')
        game._check_winner('red')
        print('---')

    def test_check_winner_red2(self):
        """
        Test the _check_winner method of the HexGame class for the 'red' player with a longer sequence.
        """
        game = HexGame(12)
        game._make_move(0, 0, 'red')
        game._make_move(1, 0, 'red')
        game._make_move(2, 0, 'red')
        game._make_move(3, 0, 'red')
        game._make_move(4, 0, 'red')
        game._make_move(5, 0, 'red')
        game._make_move(6, 0, 'red')
        game._make_move(7, 0, 'red')
        game._make_move(8, 0, 'red')
        game._make_move(9, 0, 'red')
        game._make_move(10, 0, 'red')
        game._make_move(11, 0, 'red')
        print('---')
        game._check_winner('red')
        self.assertEqual(game.winner, 'red')
        print('---')

    def test_check_winner_blue(self):
        """
        Test the _check_winner method of the HexGame class for the 'blue' player.
        """
        game = HexGame(3)
        game._make_move(0, 0, 'blue')
        game._make_move(0, 1, 'blue')
        game._make_move(0, 2, 'blue')
        print('---')
        game._check_winner('blue')
        self.assertEqual(game.winner, 'blue')
        print('---')

    def test_check_winner_no_winner(self):
        """
        Test the _check_winner method of the HexGame class when there is no winner.
        """
        game = HexGame(5)
        game._make_move(0, 0, 'red')
        game._make_move(0, 1, 'red')
        game._make_move(0, 2, 'red')
        game._make_move(1, 0, 'blue')
        game._make_move(1, 1, 'blue')
        game._make_move(1, 2, 'blue')
        game._check_winner('red')
        game._check_winner('blue')
        self.assertIsNone(game.winner)
        

if __name__ == '__main__':
    unittest.main()