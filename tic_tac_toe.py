board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

current_player=""

winner= None

def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2]+"   1 | 2 | 3")
    print("----------  ----------")
    print(board[3]+" | "+board[4]+" | "+board[5]+"   4 | 5 | 6")
    print("----------  ----------")
    print(board[6]+" | "+board[7]+" | "+board[8]+"   7 | 8 | 9")

def menu():
    global current_player
    print("----------MENU---------")
    print("Press X: To play with X")
    print("Press O: To play with O")
    current_player=input("Choose Player: ")
    while current_player not in ["X","O"]:
        current_player=input("Choose Player from X and O: ")

def play_game():
    menu()
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner=="X" or winner=="O":
        print(winner+" won.")
    elif winner==None:
        print("Tie.")        

def handle_turn(player):
    print(current_player+"'s turn.")
    position=input("Choose netween 1-9: ")
    valid=False
    while not valid:
        while position not in ["1", "2","3","4","5","6","7","8","9"]:
            position=input("Choose netween 1-9: ")
        position=int(position) -1
        if board[position]=="-":
            valid=True
        else:
            print("You can't go there.Go again")    

    board[position]=player
    display_board()

def check_if_game_over():
    check_winner()
    check_tie()
    return 

def check_winner():
    global winner
    row_winner=check_for_row()
    column_winner=check_for_column()
    diagonal_winner=check_for_diagonal()

    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None            

def check_for_row():
    global game_still_going
    row_1=board[0]==board[1]==board[2]!="-"
    row_2=board[3]==board[4]==board[5]!="-"
    row_3=board[6]==board[7]==board[8]!="-"
    if row_1 or row_2 or row_3:
        game_still_going=False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:                
        return None

def check_for_column():
    global game_still_going
    column_1=board[0]==board[3]==board[6]!="-"
    column_2=board[1]==board[4]==board[7]!="-"
    column_3=board[2]==board[5]==board[8]!="-"
    if column_1 or column_2 or column_3:
        game_still_going=False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:                
        return None

def check_for_diagonal():
    global game_still_going
    diagonal_1=board[0]==board[4]==board[8]!="-"
    diagonal_2=board[2]==board[4]==board[6]!="-"
    if diagonal_1 or diagonal_2 :
        game_still_going=False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return

def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"    
    else:                
        return None

def check_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
        return True
    else:
        return False    

play_game()        