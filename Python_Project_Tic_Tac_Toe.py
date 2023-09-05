import copy
def display_board(board):
    arr = copy.deepcopy(board)
    
    for i in range(3):
        for j in range(3):
            if(arr[i][j] == 11):
                arr[i][j] = player_one
            elif(arr[i][j] == 12):
                arr[i][j] = player_two
      
    print("\n")
    print("\t     |     |     ")
    print(f"\t  {arr[0][0]}  |  {arr[0][1]}  |  {arr[0][2]}  ")
    print("\t_____|_____|_____")
    print("\t     |     |     ")
    print(f"\t  {arr[1][0]}  |  {arr[1][1]}  |  {arr[1][2]}  ")
    print("\t_____|_____|_____")
    print("\t     |     |     ")
    print(f"\t  {arr[2][0]}  |  {arr[2][1]}  |  {arr[2][2]}  ")
    print("\t     |     |     ")
    
    
def User_input():
        if(turn == 11):
            print(f'player_one turn:{player_one}')
        else:
            print(f'player_two turn:{player_two}')
                
        n = int(input("Enter the number where you want to place the marker: "))
        return n
        
def Check(board,position,turn):
    
    r = 0 
    c = 0
    for i in range(0,3):
        for j in range(0,3):
            if(position == board[i][j]):
                r = i 
                c = j 
                break
    
    board[r][c] = turn
    
    if(board[r][0] == board[r][1] == board[r][2]):
        return True
    elif(board[0][c] == board[1][c] == board[2][c]):
        return True
    else:
        k = 1
        l = 1
        if(board[k][l] != turn):
            return False
        if((board[k-1][l-1] == board[k][l]) and (board[k][l] == board[k+1][l+1])):
            return True
        elif((board[k-1][l+1] == board[k][l]) and (board[k][l] == board[k+1][l-1])):
            return True
    
    
    return False
    
            
    
global turn, player_one, player_two

board = [[1,2,3],[4,5,6],[7,8,9]]
marker = input("Please pick a marker:'X' or 'O'\n")
while (marker != 'X' and marker != 'O'):
    print('Invalid input')
    marker = input("Please pick a marker:'X' or 'O'\n")

player_one = marker
if(player_one == 'O'):
    player_two = 'X'
else:
    player_two = 'O'
turn = 11 
isWin = False

display_board(board)

while isWin != True:
    position = User_input()
    if(Check(board,position,turn)== True):
        if(turn % 2 != 0):
            print("\n\n")
            print(f"Congratulations!!!! YOU WON THE GAME \n Winner is Player_one : {player_one}")
            isWin = True
        else:
            print("\n\n")
            print(f"Congratulations!!!! YOU WON THE GAME \n Winner is Player_two : {player_two}")
            isWin = True
    display_board(board)
    if(turn == 11):
        turn = 12
    else:
        turn = 11


