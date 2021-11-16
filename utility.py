import random


def generate_board(n):
    board = [random.randint(0, n-1) for _ in range(n)]
    return board


def get_heuristic_cost(n, board):
    h = 0
    for i in range(n):
        for j in range(i+1, n):

            if board[i] == board[j]:   # Queens in same row
                h+=1

            offset = j - i

            # checking digonal contstrain 
            if board[j] == board[i]-offset or board[j] == board[i]+offset:
                h+=1

    return h


def print_board(board):
    n = len(board)
    for i in range(n-1, -1, -1):
        for j in range(n):
            if board[j] == i: print(' Q ', end='')
            else: print(' - ', end='')
        print()
    pass


if __name__ == '__main__':
    board = generate_board(4)
    print(board)
    print_board(board)
    print(get_heuristic_cost(4, board))