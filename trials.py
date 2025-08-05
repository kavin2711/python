board=[1,2,3,4,5,6,7,8,9]

def print_board():
    counter=0
    for row in range(3):
        print("+-------"*3 + "+")
        print("|       "*3 + "|" )
        for column in range (3):
            print("|   "+ str(board[counter]) + "   ", end="") 
            counter+=1
            
        print("|")
        print("|       "*3 + "|" )
        
    print("+-------"*3 + "+")
    
import random

def computer_move():
    cc=[]
    for i in board:
        if isinstance(i, str):
         continue
        else:
            cc.append(i)
    randomchar = random.choice(cc)
    board[randomchar-1]="o"
    print_board()
       
   
def player_move():
    move= int(input("Enter your move : "))
    if move in board:
        board[move-1]="x"
    else:
        print("Invalid move, try again.")
        player_move()
    print_board() 

def check_winner():
    for i, j, k in [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]:
        if board[i]==board[j]==board[k]:
            return board[i]
    
    
    
   

while True:
    print_board()
    computer_move()
    player_move()
    check_winner()

