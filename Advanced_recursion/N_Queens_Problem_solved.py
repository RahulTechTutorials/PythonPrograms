## This function wil print the chess board in n* n matrix
def printChessboard(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = "  ")
        print('\n')
    
## This function will determine if the particular position is under attack or not.
def ungaurded(board, i, j,n):
    for row in range(n):
        for col in range(n):
            if not board[row][col] == "_" :
                if row == i or col == j:
                    return False
                elif row + col == i + j:
                    return False
                elif row - col == i - j:
                    return False
                    
    return True               

## This function will recursively run and place all the Queens
def queenPlacement(board,col, count,n):

    if count == n:
        print('The queen placement is done\n')
        printChessboard(board,n)
        return
    else :
        count += 1
        for row in range(n):
            if ungaurded(board,row,col,n):
                board[row][col] = 'Q'
                queenPlacement(board,col+1, count,n)
###This is the back tracking mechanism.
        for x in range(n):
            board[x][col-1] = "_"
        count -= 1
            
 
##Main function to call the solution
def main():
    n = int(input('Please input the number of queens you want to place: '))
    chessboard = [["_" for x in range(n)] for y in range(n)]
    queenPlacement(chessboard, 0,0,n)

if __name__ == '__main__':
    main()
    
