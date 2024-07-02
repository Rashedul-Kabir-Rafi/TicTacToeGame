import random

def initialize_game():
    global board, current_player, game_running
    
    board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

    current_player = "X"
    winner = None
    game_running = True

# printing the game board

def print_Board(board): 
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("- - - - -")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("- - - - -")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input

def player_Input(board):
    while True:
        try:
            inpuT = int(input("Enter a number between 1 to 9: "))
            if inpuT >= 1 and inpuT <= 9 and board[inpuT - 1] == "-":
                board[inpuT - 1] = current_player
                break
            else:
                print("Oops, player is already in that place!")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


# check for win or tie

# Check for horizontal win
def check_Horizontal(board):
    global winner
    
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

# Check for vertical win
def check_Vertical(board):
    
    global winner
    
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[3]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[6]
        return True
    return False

# Check for diagonal win
def check_Diagonal(board):
    
    global winner
     
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True   
    return False
    
def check_Tie(board):
    
    global game_running
    
    if "-" not in board:
        print_Board(board)
        print("Oops, it's a tie !")
        game_running = False
        
# Check for win

def check_Win():
    
    global game_running
    if check_Diagonal(board) or check_Horizontal(board) or check_Vertical(board):
        print_Board(board)
        print(f"The winnner is {winner}")
        game_running = False


# switch the player

def switch_Player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
        
        
# computer move

def computer(board):
    while current_player == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switch_Player()

# chexk for win or tie again

def play_game():
    
    while game_running:
        print_Board(board)
        player_Input(board)
        check_Win()
        if not game_running:
            break
            check_Tie(board)
        if not game_running:
            break
        switch_Player()
    
        computer(board)
        check_Win()
        if not game_running:
            break
        check_Tie(board)
        if not game_running:
            break



# Main game loop
while True:
    initialize_game()
    play_game()
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
