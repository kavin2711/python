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
board=[1,2,3,4,5,6,7,8,9]

def computer_move():
    import random
    move = random.randint(1, 9)
    if move in board:
       board[move-1]="o"
    else:
        computer_move()

       