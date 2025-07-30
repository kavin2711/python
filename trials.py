def print_board():
    counter=1
    for row in range(3):
        print("+-------"*3 + "+")
        print("|       "*3 + "|" )
        for column in range (3):
            print("|   "+ str(counter) + "   ", end="")
            counter+=1
            
        print("|")
        print("|       "*3 + "|" )
        
    print("+-------"*3 + "+")