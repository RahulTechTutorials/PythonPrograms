def primecheck():
    '''This is a program to check the entered number is a prime or not'''
    try:
        Number = input('Enter the number to check the prime:')
        status = 'prime'
        Number = int(Number)
        for i in range(2,Number):
            if Number % i == 0:
                status = 'composite'
            else:
                continue
        if Number == '':
            print('The input is not a valid number')
        elif Number < 0:
            print('The number is a negative Number')
        elif Number == 0 or Number == 1 :
            print('The number is neither prime nor composite')
        else: 
            print('The number ', Number, ' is ', status)
                
    
    except ValueError:
        print('You have entered a Non numeric number')
        
def main():
    primecheck()

if __name__ == '__main__':
    main()
        