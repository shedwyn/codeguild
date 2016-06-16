import unittest
import tic_tac_toe


class ListTTTBoardTest(unittest.TestCase):

    def test___init__(self):
        test_board = tic_tac_toe.ListListTTTBoard()
        expected = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        assert test_board.rows == expected

    def test_place(self):
        test_board = tic_tac_toe.ListListTTTBoard()
        test_board.place(0, 0, 'X')
        test_board.place(1, 0, 'X')
        test_board.place(2, 0, 'X')
        assert test_board.rows == [
            ['X', 'X', 'X'],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def test_won_x_on_row(self):
        test_board = tic_tac_toe.ListListTTTBoard()
        test_board.place(0, 1, 'X')
        test_board.place(1, 1, 'X')
        test_board.place(2, 1, 'X')
        assert test_board.won() == 'X'

    def test_won_x_on_column(self):
        test_board = tic_tac_toe.ListListTTTBoard()
        test_board.place(1, 0, 'X')
        test_board.place(1, 1, 'X')
        test_board.place(1, 2, 'X')
        assert test_board.won() == 'X'

    def test_won_x_on_diagonal(self):
        test_board = tic_tac_toe.ListListTTTBoard()
        test_board.place(2, 0, 'X')
        test_board.place(1, 1, 'X')
        test_board.place(0, 2, 'X')
        assert test_board.won() == 'X'

    def test_won_o_on_row(self):
        test_board = tic_tac_toe.ListListTTTBoard()
        test_board.place(0, 0, 'O')
        test_board.place(1, 0, 'O')
        test_board.place(2, 0, 'O')
        assert test_board.won() == 'O'

    def test_won_o_on_column(self):
        test_board = tic_tac_toe.ListListTTTBoard()
        test_board.place(1, 0, 'O')
        test_board.place(1, 1, 'O')
        test_board.place(1, 2, 'O')
        assert test_board.won() == 'O'

    def test_won_o_on_diagonal(self):
        test_board = tic_tac_toe.ListListTTTBoard()
        test_board.place(2, 0, 'O')
        test_board.place(1, 1, 'O')
        test_board.place(0, 2, 'O')
        assert test_board.won() == 'O'

    def test_won_none(self):
        test_board = tic_tac_toe.ListListTTTBoard()
        test_board.place(0, 0, 'O')
        test_board.place(0, 1, 'X')
        test_board.place(0, 2, 'X')
        assert test_board.won() == None

class DictTTTBoardTest(unittest.TestCase):

    def test___init__(self):
        test_board = tic_tac_toe.DictTTTBoard()
        expected = {
            'a1': ' ', 'b1': ' ', 'c1': ' ',
            'a2': ' ', 'b2': ' ', 'c2': ' ',
            'a3': ' ', 'b3': ' ', 'c3': ' ',
        }
        assert test_board.pos_to_token == expected

    def test_place(self):
        test_board = tic_tac_toe.DictTTTBoard()
        test_board.place(0, 0, 'X')
        test_board.place(1, 0, 'X')
        test_board.place(2, 0, 'X')
        assert test_board.pos_to_token == {
            'a1': 'X', 'b1': ' ', 'c1': ' ',
            'a2': 'X', 'b2': ' ', 'c2': ' ',
            'a3': 'X', 'b3': ' ', 'c3': ' ',
        }

    def test_create_column_sorted_tokens(self):
        test_board = tic_tac_toe.DictTTTBoard()
        test_board.place(0, 0, 'X')
        test_board.place(1, 0, 'X')
        test_board.place(2, 0, 'X')
        assert test_board.column_ordered_tokens

    def test_won_x_on_row(self):
        test_board = tic_tac_toe.DictTTTBoard()
        test_board.place(0, 1, 'X')
        test_board.place(1, 1, 'X')
        test_board.place(2, 1, 'X')
        assert test_board.won() == 'X'

    def test_won_x_on_column(self):
        test_board = tic_tac_toe.DictTTTBoard()
        test_board.place(1, 0, 'X')
        test_board.place(1, 1, 'X')
        test_board.place(1, 2, 'X')
        assert test_board.won() == 'X'

    def test_won_x_on_diagonal(self):
        test_board = tic_tac_toe.DictTTTBoard()
        test_board.place(2, 0, 'X')
        test_board.place(1, 1, 'X')
        test_board.place(0, 2, 'X')
        assert test_board.won() == 'X'

    def test_won_o_on_row(self):
        test_board = tic_tac_toe.DictTTTBoard()
        test_board.place(0, 0, 'O')
        test_board.place(1, 0, 'O')
        test_board.place(2, 0, 'O')
        assert test_board.won() == 'O'

    def test_won_o_on_column(self):
        test_board = tic_tac_toe.DictTTTBoard()
        test_board.place(1, 0, 'O')
        test_board.place(1, 1, 'O')
        test_board.place(1, 2, 'O')
        assert test_board.won() == 'O'

    def test_won_o_on_diagonal(self):
        test_board = tic_tac_toe.DictTTTBoard()
        test_board.place(2, 0, 'O')
        test_board.place(1, 1, 'O')
        test_board.place(0, 2, 'O')
        assert test_board.won() == 'O'

    def test_won_none(self):
        test_board = tic_tac_toe.DictTTTBoard()
        test_board.place(0, 0, 'O')
        test_board.place(0, 1, 'X')
        test_board.place(0, 2, 'X')
        assert test_board.won() == None