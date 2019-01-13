
## This function wil print the chess board in n* n matrix
def printChessboard(board):
    for i in range(5):
        for j in range(5):
            print(board[i][j], end = "  ")
        print('\n')
    
## This function will determine if the possible moves of knight.
def nextMoves(board, row, col):
    possibleMovesX = ''
    possibleMovesY = ''
    possibleMoves = ()
    
    lst = list(range(5))
    if row+2 in lst and col-1 in lst and  board[row+2][col-1] == 0 :
        possibleMovesX += str(row+2)
        possibleMovesY += str(col-1)
    if row+2 in lst and col+1 in lst and  board[row+2][col+1] == 0 :
        possibleMovesX += str(row+2)
        possibleMovesY += str(col+1)
    if row-2 in lst and col-1 in lst and  board[row-2][col-1] == 0 :
        possibleMovesX += str(row-2)
        possibleMovesY += str(col-1)
    if row-2 in lst and col+1 in lst and  board[row-2][col+1] == 0 :
        possibleMovesX += str(row-2)
        possibleMovesY += str(col+1)
    if row+1 in lst and col-2 in lst and  board[row+1][col-2] == 0 :
        possibleMovesX += str(row+1)
        possibleMovesY += str(col-2)
    if row+1 in lst and col+2 in lst and  board[row+1][col+2] == 0 :
        possibleMovesX += str(row+1)
        possibleMovesY += str(col+2)
    if row-1 in lst and col-2 in lst and  board[row-1][col-2] == 0 :
        possibleMovesX += str(row-1)
        possibleMovesY += str(col-2)
    if row-1 in lst and col+2 in lst and  board[row-1][col+2] == 0 :
        possibleMovesX += str(row-1)
        possibleMovesY += str(col+2)
    
    possibleMovesX = tuple(possibleMovesX)
    possibleMovesY = tuple(possibleMovesY)
    possibleMoves = tuple(zip(possibleMovesX,possibleMovesY))
    return possibleMoves
       

## This function will recursively run and place all the knights
def knightMove(board,row,col,count):
    if count == 26:
        print('The knight tour has completed\n')
        printChessboard(board)
        return
    else :
        possibleMoves = nextMoves(board,row,col)
        for (x,y) in possibleMoves:
            i = int(x) ; j = int(y)
            if board[i][j] == 0:
                board[i][j] = count
                knightMove(board,i,j,count+1)

###This is the back tracking mechanism.
        for a in range(5):
            for b in range(5):
                if board[a][b] == count-1:
                    board[a][b] = 0
        
            
 
##Main function to call the solution
def main():

    chessboard = [[0 for x in range(5)] for y in range(5)]
    chessboard[0][0] = 1
    knightMove(chessboard, 0,0,2)

if __name__ == '__main__':
    main()
    
