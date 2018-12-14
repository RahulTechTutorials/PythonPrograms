def main():
    """This program is to print the pyramid"""
    shape = int(input("Enter the type of shape. 1 for triangle and 2 for right pyramid and 3 for inverted pyramid"))
    assert (shape == 1 or shape == 2 or shape ==3)
    nrows = int(input("Enter the number of rows for the  pyramid/triangle, odd number fo pyramid please"))
    assert nrows > 0
    if shape == 1:
        printtriange(nrows)
    elif shape ==2:
        printpyramid(nrows)
    else:
        printinvertedpyramid(nrows)

def printtriange(n):
    for i in range(1,n+1):
        print('*' * i)

def printpyramid(n):
    for i in range(1,n+1):
        print(' ' * (n-i) , '*' * (2*i-1))
        
def printinvertedpyramid(n):
    for i in range(1,n+1):
        print(' ' * (i-1) , '*' * ((2*(n-i)) + 1))

if __name__ == "__main__":
    main()
