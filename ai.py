from random import randint, seed

class AI:
    def __init__(self, player):
        self.player = player
        seed() 

    def get_array(self, board):
        y, x = 0, 0
        possible = []

        if (board[0][0] == board[1][0] and board[0][0] != ' '): 
            if board[2][0] == ' ':
                y, x = 2, 0
                possible.append([y, x, board[0][0]])

        if (board[2][1] == board[2][2] and board[2][1] != ' '):
            if board[2][0] == ' ':
                y, x = 2, 0
                possible.append([y, x, board[2][1]])

        if (board[0][2] == board[1][1] and board[0][2] != ' '):
            if board[2][0] == ' ':
                y, x = 2, 0
                possible.append([y, x, board[0][2]])

        if (board[0][1] == board[1][1] and board[0][1] != ' '):
            if board[2][1] == ' ':
                y, x = 2, 1
                possible.append([y, x, board[0][1]])

        if (board[2][0] == board[2][2] and board[2][0] != ' '):
            if board[2][1] == ' ':
                y, x = 2, 1
                possible.append([y, x, board[2][0]])

        if (board[0][2] == board[1][2] and board[0][2] != ' '): 
            if board[2][2] == ' ':
                y, x = 2, 2
                possible.append([y, x, board[0][2]])
        
        if (board[2][0] == board[2][1] and board[2][0] != ' '):
            if board[2][1] == ' ':
                y, x = 2, 1
                possible.append([y, x, board[2][0]]) 
        
        if (board[0][0] == board[1][1] and board[0][0] != ' '):
            if board[2][2] == ' ':
                y, x = 2, 2
                possible.append([y, x, board[0][0]])

        if (board[1][0] == board[2][0] and board[1][0] != ' '):
            if board[0][0] == ' ':
                y, x = 0, 0
                possible.append([y, x, board[1][0]])

        if (board[0][1] == board[0][2] and board[0][1] != ' '):
            if board[0][0] == ' ':
                y, x = 0, 0
                possible.append([y, x, board[0][1]])

        if (board[1][1] == board[2][2] and board[1][1] != ' '):
            if board[0][0] == ' ':
                y, x = 0, 0
                possible.append([y, x, board[1][1]])

        if (board[1][1] == board[2][1] and board[1][1] != ' '):
            if board[0][1] == ' ':
                y, x = 0, 1
                possible.append([y, x, board[1][1]])
        
        if (board[0][0] == board[0][2] and board[0][0] != ' '):
            if board[0][1] == ' ':
                y, x = 0, 1
                possible.append([y, x, board[0][0]])

        if (board[1][2] == board[2][2] and board[1][2] != ' '):
            if board[0][2] == ' ':
                y, x = 0, 2
                possible.append([y, x, board[1][2]])

        if (board[0][0] == board[0][1] and board[0][0] != ' '):
            if board[0][2] == ' ':
                y, x = 0, 2
                possible.append([y, x, board[0][0]])

        if (board[1][1] == board[2][0] and board[1][1] != ' '):
            if board[0][2] == ' ':
                y, x = 0, 2
                possible.append([y, x, board[1][1]])

        if (board[1][0] == board[1][1] and board[1][0] != ' '):
            if board[1][2] == ' ':
                y, x = 1, 2
                possible.append([y, x, board[1][0]])

        if (board[0][2] == board[2][2] and board[0][2] != ' '):
            if board[1][2] == ' ':
                y, x = 1, 2
                possible.append([y, x, board[0][2]])

        if (board[1][1] == board[1][2] and board[1][1] != ' '):
            if board[1][0] == ' ':
                y, x = 1, 0
                possible.append([y, x, board[1][1]])

        if (board[0][0] == board[2][0] and board[0][0] != ' '):
            if board[1][0] == ' ':
                y, x = 1, 0
                possible.append([y, x, board[0][0]])
        
        if (board[0][1] == board[2][1] and board[0][1] != ' '):
            if board[1][1] == ' ':
                y, x = 1, 1
                possible.append([y, x, board[0][1]])

        if (board[1][0] == board[1][2] and board[1][0] != ' '):
            if board[1][1] == ' ':
                y, x = 1, 1
                possible.append([y, x, board[1][0]])

        if (board[0][0] == board[2][2] and board[0][0] != ' '):
            if board[1][1] == ' ':
                y, x = 1, 1
                possible.append([y, x, board[0][0]])

        if (board[2][0] == board[0][2] and board[2][0] != ' '):
            if board[1][1] == ' ':
                y, x = 1, 1
                possible.append([y, x, board[2][0]])

        return possible

    def ai_play(self, board):
        possible = self.get_array(board)

        if len(possible) == 0:
            while True:
                x, y = randint(0, 2), randint(0, 2)

                if board[y][x] == ' ':
                    return y, x
    
        for i in possible:
            if i[2] == self.player:
                return i[0], i[1]

        return possible[0][0], possible[0][1]

if __name__ == '__main__':
    board = [
        [' ', ' ', ' '],
        ['X', ' ', 'X'],
        ['X', ' ', 'O']
    ]

    ai = AI('X')
    y, x = ai.ai_play(board)
    board[y][x] = 'X'

    for i in board:
        print(i)