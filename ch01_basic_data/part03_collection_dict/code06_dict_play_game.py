# 代码清单05: code05 game


def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def play_game():
    board = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
             'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
    turn = 'X'
    for i in range(9):
        print_board(board)
        print('Turn for ' + turn + ' . Move on which space ?')
        move = input()
        board[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


if __name__ == '__main__':
    play_game()

