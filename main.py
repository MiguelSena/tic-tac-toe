from random import randint, choice, seed
from ai import AI

def print_board():
    print('    0   1   2\n')
    row = 0
    for i in range(len(board)):
        print(f'{row}   {board[i][0]} | {board[i][1]} | {board[i][2]}')
        row += 1

        if i != (len(board) - 1):
            print('   -----------')
        
    print()

def play(player, name):
    move = input(f'{name}: Qual a sua jogada (x y)? ').strip().split()

    if len(move) != 2:
        print('ERRO: Resposta inválida\n') 
        play(player, name)
    
    else:
        try:
            x, y = int(move[0]), int(move[1])
            space = board[y][x]

            if space != ' ':
                print('ERRO: Espaço ocupado\n')
                play(player, name)
            
            else:
                board[y][x] = player

        except:
            print('ERRO: Insira apenas caracteres válidos\n')
            play(player, name)	

def get_winner():
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return board[0][0]
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]: 
        return board[0][0]
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]: 
        return board[2][2]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[2][2]

    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]: 
        return board[1][1]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[1][1]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[1][1]
    
    else:
        counter = 0
        for i in board:
            if ' ' not in i:
                counter += 1
        
        if counter == 3:
            return 'No Winner'
        
        return False

def pvp(player):
    x_name = input('Qual será o nome de X?\n>>> ')
    o_name = input('Qual será o nome de O?\n>>> ')
    print()

    if player == 1:
        print(f'Primeiro jogador: {x_name}')
    else:
        print(f'Primeiro jogador: {o_name}')

    while True:
        print('\n\n\n')
        print_board()
        
        if player == 1:
            play('X', x_name)
            player += 1

        else:
            play('O', o_name)
            player = 1

        if get_winner() == 'No Winner':
            print('\n\n\nVELHA')
            print_board()
            break

        elif get_winner() != ' ' and get_winner() != False:
            print(f'\n\n\nO vencedor foi: {get_winner()}!!!')
            print_board()
            break

def pvc(player):
    teams = ['X', 'O']
    ai_team = choice(teams)
    teams.remove(ai_team)
    player_team = teams[0]

    ai = AI(ai_team)
    name = input('Qual será o seu nome?\n>>> ')

    while True:
        print('\n')

        if player == 1:
            print_board()
            play(player_team, name)
            player += 1

        else:
            y, x = ai.ai_play(board)
            board[y][x] = ai_team
            player = 1

        if get_winner() == 'No Winner':
            print('\n\n\nVELHA')
            print_board()
            break

        elif get_winner() != ' ' and get_winner() != False:
            if get_winner() == ai_team:
                print('\n\n\nVocê perdeu')
            else:
                print('\n\n\nVocê ganhou')

            print_board()
            break


while True:
    player = randint(1, 2)
    seed()
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    print('\n\n\n\n\n\n\n')
    print('JOGO DA VELHA')
    mode = input('Qual será o modo de jogo (1: PvP; 2: PvC)?\n>>> ').strip()

    if mode == '1':
        print('\n\n\n')
        pvp(player)

    elif mode == '2':
        print('\n\n\n')
        pvc(player)

    else:
        print('ERRO: Modo desconhecido\n')