def fibonacci(n):
    assert n >=0
    if n == 1:
        return 0
    elif n ==2:
        return 1
    result = fibonacci(n-1) + fibonacci(n-2)
    return result
    

#0,1,1,2,3,5,8,13,21....


def main():
    '''This program is to create a fibonacci series n term '''
    try:
        n = int(input('Enter the n for finding the nth term of fibonacci series: '))
        nthterm = fibonacci(n)
        print('The ',n,'th/rd term of fibonacci is',nthterm)
    
    except ValueError:
        print('The value you entered is not numeric')
if __name__ == '__main__':
    main()
    
