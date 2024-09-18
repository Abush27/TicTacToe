import random

print("Welcome to tictactoe \n")

array = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def showBoard(array):
    print("")
    print("-------")
    for x in array:
        print("|" + x[0] + "|" + x[1] + "|" + x[2] + "|")
        print("-------")
    print("")

def isFull(array):
    status = True
    for x in array:
        for i in x:
            if i != " ":
                status = False
                return(status)
    return status
    

def computerMove(array):
    looking = True
    computerChoice = []
    randArray = [0, 1, 2]

    while looking:
        row = random.choice(randArray)
        col = random.choice(randArray)
        if array[row][col] == " ":
            computerChoice = [row, col]
            return computerChoice

def checkVictory(array):
    
    for x in array:
        if (x[0] + x[1] + x[2]) == "XXX":
            print("Congratulations you won!")
            return "done"
        elif (x[0] + x[1] + x[2]) == "000":
            print("You Lost!")
            return "done"

    if array[0][0] + array[1][0] + array[2][0] == "XXX" or array[0][1] + array[1][1] + array[2][1] == "XXX" or array[0][2] + array[1][2] + array[2][2] == "XXX" or array[0][0] + array[1][1] + array[2][2] == "XXX" or array[0][2] + array[1][1] + array[2][0] == "XXX":
        print("Congratulations you won")
        return "done"

    elif array[0][0] + array[1][0] + array[2][0] == "000" or array[0][1] + array[1][1] + array[2][1] == "000" or array[0][2] + array[1][2] + array[2][2] == "000" or array[0][0] + array[1][1] + array[2][2] == "000" or array[0][2] + array[1][1] + array[2][0] == "000":
        print("You Lost!")
        return "done"
    else:
        return "nah"


playing = True

while playing:
    
    col = int(input("Which column would you like to place your X in: "))
    row = int(input("Which row would you like to place your X in: "))

    
    
    if array[row-1][col-1] != " ":
        print(f'There is already a {array[row][col]} there, please choose a different slot!')

    else:
        array[row-1][col-1] = "X"
        showBoard(array)

        if checkVictory(array) == "done":
             break
            

        if isFull(array):
            print("OOoo looks like was a tie. Close one!")
            break
        
        computerChoice = computerMove(array)
        array[computerChoice[0]][computerChoice[1]] = "0"
        showBoard(array)

        if checkVictory(array) == "done":
             break
        
        
        
        

        

    
    


        






