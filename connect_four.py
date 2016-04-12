class Board:
    def __init__(self, board_rows_of_columns):
        self.board_rows_of_columns = board_rows_of_columns
    def __eq__(self, other_entry):
        return (self.board_rows_of_columns == other_entry.board_rows_of_columns)
    def __repr__(self):
        return 'Board({})'.format(self.board_rows_of_columns)
    def retrieve_next_empty_row_index(self, col_index):
        """takes board and column index, finds first empty row for that column, returns
        the row index"""
        for pair in reversed(list(enumerate(self.board_rows_of_columns))):
            print('pair', pair)
            row_index = pair[0]
            row = pair[1]
            if row[col_index] == '':
                print('row index', row_index)
                return row_index
    def place_token(self, row_index, col_index, color):
        self.board_rows_of_columns[row_index][col_index] = color


class Token:
    def __init__(self, color, column):
        self.color = color
        self.column = column
    def __eq__(self, other_entry):
        return (self.place == other_entry.color)
    def __repr__(self):
        return 'Token({}, {})'.format(self.color, self.column)
    # def make_move(self):
    #     self.color = 'Y'
    #     return
        # instatiating token will assign color
        # Token method (function) will alternate color for assignment to board


###new functions are below, need to be put in classes
##next step is to integrate 'color' into workflow    

def get_raw_text():
    """takes nothing, opens and saves moves, returns moves_list"""
    with open ('4-moves.txt') as raw_moves_text:
        moves_list = raw_moves_text.readlines()
    return moves_list

def format_moves_list():
    """takes nothing, creates and formats moves_list, returns moves_list"""
    moves_list = get_raw_text()
    split_and_joined_moves_list = ' '.join(moves_list).split()
    return split_and_joined_moves_list

def create_tokens(moves_list):
    """takes in moves_list, pairs move with token color, instantiates tokens with
    data, returns list of instantiated tokens"""
    tokens = []
    for pair in enumerate(moves_list):
        if pair[0] % 2 == 0:
            token = Token('Y', int(pair[1])-1)
            tokens.append(token)
        else:
            token = Token('R', int(pair[1])-1)
            tokens.append(token)
    return tokens

def play_move(token, current_board):
    """takes token and board, iterates across moves list, places tokens
    prints board after each move, returns board"""
    row_index = current_board.retrieve_next_empty_row_index(token.column)
    current_board.place_token(row_index, token.column, token.color)
    print('\npost move in play move', current_board)
    return current_board

def main():
    """collection of functions"""
    current_board = Board([
        ['', '', '', '', '', '', ''],
        ['', '', '', '', '', '', ''],
        ['', '', '', '', '', '', ''],
        ['', '', '', '', '', '', ''],
        ['', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '']
    ])
    moves_list = format_moves_list()
    tokens = create_tokens(moves_list)
    # print('\n', tokens[0])
    # play_move(tokens[0], current_board)
    # print('\nmain function board', current_board)
    num = 1
    for token in tokens:
        print('\nmove# ', num, 'column#', token.column, '\n')
        play_move(token, current_board)
        num += 1
        print('*'*15)
        print('\n', current_board)
        print('*'*15)

    # col_index = current_move - 1
    
    # # 
    # current_token = Token('R')
    # current_move = 2
    # # current_board.place_token(current_move)
    # print ('1_____________________________________')
    # print (test_board)
    # row_index = find_first_empty_row_index(test_board, col_index)
    
main()







# test_board = [
#     #     ['', '', '', '', '', '', ''],
#     #     ['', '', '', '', '', '', ''],
#     #     ['', '', '', '', '', '', ''],
#     #     ['', '', '', '', '', '', ''],
#     #     ['', '', '', '', '', '', ''],
#     #     ['', '', '', '', '', '', '']
#     # ]


#     # current_board[0]['a1'] = 'Y'
    # print (current_board[0]['a1'])

    # move = '1'
    #
    # single_time = 0
    # while single_time < 1
    #     for row_dict in current_board:
    #         if row_dict[key where move is in key.name] == '':
    #             sorted()
    #             single_time += 1