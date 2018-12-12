def Printsquare():
    '''Program is to print the square of a number entered by the user and the 
       execution stops once the user enters a Null value '''
    try:
        while True:     
            nNumber = input("Enter a number you need to find out a square of: ")
            if nNumber == '':
                break
            nNumber = int(nNumber)
            print('The sqaure of the number ', nNumber , 'is ', nNumber **2)
        print('End of Input')
    except ValueError:
        print('The entered string is not a Number')

def main():
    '''The main program will call the printsquare function'''
    Printsquare()

if __name__ == '__main__':
    main()
