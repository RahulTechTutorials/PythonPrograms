def fibonacci(n):
    assert n >=0
    if n == 0:
        return 0
    elif n ==1:
        return 1
    secondlast = 0
    last = 1
    
    for i in range(3,n+1):
        result = secondlast + last
        secondlast = last 
        last = result
    return result
    

#0,1,1,2,3,5,8,13....


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
    
