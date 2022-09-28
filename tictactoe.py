'''Tic-Tac-Toe: Nathan Frank'''

def main():
    player = switch_player('')
    board = create_board()
    while not (game_end(board) or draw(board)):
        display_game(board)
        player_turn(player, board)
        player = switch_player(player)
    display_game(board)
    if draw(board):
        print("Oh no, it's a draw")
    else:
        player = switch_player(player)
        print(f'Congratulations player "{player}", you won')

#define the game board
def create_board():
    board = []
    for space in range(9):
        board.append(space+1)
    return board

#display the game board
def display_game(board):
    print()
    print(f'{board[0]}|{board[1]}|{board[2]}\n-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}\n-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}\n')

#Check for win or tie
def game_end(board):
    if board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6] or board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]:
        return True

def draw(board):
    for space in range(9):
        if board[space] != "x" and board[space] != "o":
            return False
    return True

#switch player
def switch_player(selected):
    if selected == "" or selected == 'o':
        return 'x'
    elif selected == 'x':
        return 'o'

def player_turn(player, board):
    space = int(input(f'{player}, choose a square (1-9): '))
    board[space - 1] = player

if __name__ == '__main__':
    main()

