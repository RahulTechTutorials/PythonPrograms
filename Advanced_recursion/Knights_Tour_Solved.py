import cProfile, pstats, io

def profile(fnc):
    def inner(*args , **kwargs):
    

        pr = cProfile.Profile()
        pr.enable()
        retval= fnc(*args , **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return inner


## This function wil print the chess board in n* n matrix
def printChessboard(board):
    for i in range(5):
        for j in range(5):
            print(board[i][j], end = "  ")
        print('\n')
    
## This function will determine if the possible moves of knight.
def nextMoves(board, row, col):
    possibleMoves = []
    
    lst = list(range(5))
    if row+2 in lst and col-1 in lst and  board[row+2][col-1] == 0 :
        possibleMoves.append(tuple([row+2,col-1]))
    if row+2 in lst and col+1 in lst and  board[row+2][col+1] == 0 :
        possibleMoves.append(tuple([row+2,col+1]))
    if row-2 in lst and col-1 in lst and  board[row-2][col-1] == 0 :
        possibleMoves.append(tuple([row-2,col-1]))
    if row-2 in lst and col+1 in lst and  board[row-2][col+1] == 0 :
        possibleMoves.append(tuple([row-2,col+1]))
    if row+1 in lst and col-2 in lst and  board[row+1][col-2] == 0 :
        possibleMoves.append(tuple([row+1,col-2]))
    if row+1 in lst and col+2 in lst and  board[row+1][col+2] == 0 :
        possibleMoves.append(tuple([row+1,col+2]))
    if row-1 in lst and col-2 in lst and  board[row-1][col-2] == 0 :
        possibleMoves.append(tuple([row-1,col-2]))
    if row-1 in lst and col+2 in lst and  board[row-1][col+2] == 0 :
        possibleMoves.append(tuple([row-1,col+2]))

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
            if board[x][y] == 0:
                board[x][y] = count
                knightMove(board,x,y,count+1)

###This is the back tracking mechanism.
        for a in range(5):
            for b in range(5):
                if board[a][b] == count-1:
                    board[a][b] = 0
        



 
##Main function to call the solution

@profile
def main():

    chessboard = [[0 for x in range(5)] for y in range(5)]
    chessboard[0][0] = 1
    knightMove(chessboard, 0,0,2)

if __name__ == '__main__':
    main()
