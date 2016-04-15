class ListListTTTBoard:
    """Tic-Tac-Toe board that implements storage as a list
    of rows, each with three slots.

    The following board results in the following data structure.
    X| |
     |X|O
     | |

    [
        ['X', ' ', ' '],
        [' ', 'X', 'O'],
        [' ', ' ', ' '],
    ]
    """

    def __init__(self):
        """Initializes an empty board."""
        self.rows = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        print('init', self.rows)

    def place(self, x, y, player):
        """Places a token on the board at some given coordinates.
        
        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        """
        self.rows[y][x] = player
        print('place', self.rows)
        return self.rows

    def create_diagonals_list(self, list_of_rows, list_of_columns):
        """create list of diagonal areas"""
        list_of_reversed_columns = [list(reversed(_)) for _ in list_of_columns]
        indexr = 0
        indexl = 0
        diagonals = [[], []]
        #for x1, x2 in zip(l, l[1:]):
        for listr in list_of_rows:
            diagonals[0] += [listr[indexr]]
            indexr += 1
        for listl in list_of_reversed_columns:
            print('listl: ', listl)
            diagonals[1] += [listl[indexl]]
            indexl += 1
        return diagonals

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        list_of_rows = list(self.rows)
        list_of_columns = list(zip(*list_of_rows))
        diagonals = self.create_diagonals_list(list_of_rows, list_of_columns)
        joined_list_of_rows = [''.join(rowlist) for rowlist in list_of_rows]
        joined_list_of_columns = [''.join(collist) for collist in list_of_columns]
        joined_diagonals = [''.join(diagonal) for diagonal in diagonals]
                
        if 'XXX' in joined_list_of_rows or 'XXX' in joined_list_of_columns or 'XXX' in joined_diagonals:
                return 'X'
        elif 'OOO' in joined_list_of_rows or 'OOO' in joined_list_of_columns or 'OOO' in joined_diagonals:
                return 'O'
        else:
            return None        

    def __str__(self):
        """Returns a string representation of the board.

        Should be three rows with each cell separated by a '|'.

        X| |
         |X|O
         | |
        """

        rows_as_strings = ['|'.join(_) for _ in self.rows]
        board_strings_plus_carriage_return = '\n'.join(rows_as_strings) + '\n'
        return board_strings_plus_carriage_return


class DictTTTBoard:
    """Tic-Tac-Toe board that implements storage as a flat
    dictionary of slots.

    The following board results in the following data structure.
    X| |
     |X|O
     | |

    {
        'a1': 'X', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': 'X', 'c2': 'O',
        'a3': ' ', 'b3': ' ', 'c3': ' ',
    }
    """

    def __init__(self):
        """Initializes an empty board."""
        self.pos_to_token = {
            'a1': ' ', 'b1': ' ', 'c1': ' ',
            'a2': ' ', 'b2': ' ', 'c2': ' ',
            'a3': ' ', 'b3': ' ', 'c3': ' ',
        }

    def place(self, x, y, player):
        """Places a token on the board at some given coordinates.
        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        """
        board_cols = ['a', 'b', 'c']
        board_row = str(x + 1)
        board_col = board_cols[y]
        board_pos = board_col + board_row
        self.pos_to_token[board_pos] = player 

        return self.pos_to_token

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        pass

    def create_column_sorted_tokens(self):
        """sort tokens by column into single list.  return list"""
        #, reverse=True removed from below
        sorted_pos_to_token = sorted(self.pos_to_token)
        column_ordered_tokens = []
        index_sorted_pos_to_token = 0
        for move in self.pos_to_token:
            key_self.pos_to_token = sorted_pos_to_token[index_sorted_pos_to_token]
            column_ordered_tokens = column_ordered_tokens + [self.pos_to_token[key_selfpos_to_token]]
            index_sorted_pos_to_token += 1
        return column_ordered_tokens

    def __str__(self):
        """Returns a string representation of the board.

        Should be three rows with each cell separated by a '|'.

        X| |
         |X|O
         | |
        """
        # keys in own list, match string slice [1] for each, cast those triplets
            # to string (do they live in a list?) and print in reverse order
            #SPLIT INTO PARALLEL LISTS, FIX THE KEY, RECAST, THEN DO THE LIST
            #CLASS CODE

        column_sorted_tokens = self.create_column_sorted_tokens()


        rows_as_strings = ['|'.join(_) for _ in self.column_sorted_tokens]
        return '\n'.join(rows_as_strings)

        pass


class CoordsTTTBoard:
    """Tic-Tac-Toe board that implements storage as a list of x, y, token triplets.

    An empty board is an empty list.
    Each token that is on the board adds one item to the triplet list.

    The following board results in the following data structure.
    X| |
     |X|O
     | |

    [(0, 0, 'X'), (1, 1, 'X'), (2, 1, 'O')]
    """

    def __init__(self):
        """Initalizes an empty board."""
        self.x_y_token_triplets = []

    def place(self, x, y, player):
        """Places a token on the board at some given coordinates.

        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        """ 
        self.x_y_token_triplets = self.x_y_token_triplets + [(x, y, player)]

        pass

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        pass

    def __str__(self):
        """Returns a string representation of the board.

        Should be three rows with each cell separated by a '|'.

        X| |
         |X|O
         | |
        """
        pass


def play(board):
    """Plays a test game on an empty board.

    Asserts that the board is working properly.
    """
    board.place(1, 1, 'X')
    print(board)
    board.place(0, 0, 'O')
    print(board)
    board.place(1, 0, 'X')
    print('this', str(board))
    assert str(board) == "O|X| \n |X| \n | | \n"
    print(board)
    board.place(0, 2, 'O')
    print(board)
    assert board.won() is None
    board.place(1, 2, 'X')
    print(board)
    assert board.won() == 'X'


def main():
    # board1 = DictTTTBoard()
    # play(board1)
    board2 = ListListTTTBoard()
    board2.won()
    # play(board2)
    # board3 = CoordsTTTBoard()
    # play(board3)

if __name__ == '__main__':

    main()


# selfpos_to_token = {
#             'a1': 'O', 'b1': 'X', 'c1': 'O',
#             'a2': 'O', 'b2': 'X', 'c2': 'X',
#             'a3': ' ', 'b3': 'O', 'c3': ' ',
#         }

# sorted_pos_to_token = sorted(selfpos_to_token)
# print(sorted_pos_to_token)
# column_ordered_tokens = []
# index_sorted_pos_to_token = 0
# for move in selfpos_to_token:
#     key_selfpos_to_token = sorted_pos_to_token[index_sorted_pos_to_token]
#     column_ordered_tokens = column_ordered_tokens + [selfpos_to_token[key_selfpos_to_token]]
#     index_sorted_pos_to_token += 1
# print(column_ordered_tokens)

# if self.rows[0][0] == self.rows[1][0] and self.rows[0][0] == self.rows[2][0]:
        #     return self.rows[0][0]
        # elif self.rows[0][1] == self.rows[1][1] and self.rows[0][1] == self.rows[2][1]:
        #     return self.rows[1][0]
        # elif self.rows[0][2] == self.rows[1][2] and self.rows[0][2] == self.rows[2][2]:
        #     return self.rows[2][0]
        # elif self.rows[0][0] == self.rows[0][1] and self.rows[0][0] == self.rows[0][2]:
        #     return self.rows[0][0]
        # elif self.rows[1][0] == self.rows[1][1] and self.rows[1][0] == self.rows[1][2]:
        #     return self.rows[0][1]
        # elif self.rows[2][0] == self.rows[2][1] and self.rows[2][0] == self.rows[2][2]:
        #     return self.rows[0][2]
        # elif self.rows[0][0] == self.rows[1][1]  == self.rows[2][2]:
        #     return self.rows[0][0]
        # elif self.rows[2][0] == self.rows[1][1]  == self.rows[0][2]:
        #     return self.rows[0][2]
        # else:
        #     print('none win condition')
        #     return None


