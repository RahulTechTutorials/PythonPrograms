def multiply(n1,n2,mul = 0):
    mul = mul + n1
    
    if n2 == 1:
        print('The multiplication of two number is : ',mul  )
    else:
        multiply(n1,n2-1,mul)
    
    
    


def main():
    global mul
    print('Enter two numbers to multiply')
    n1 = int(input('Enter the 1st number'))      
    n2 = int(input('Enter the 2nd number'))    
    multiply(n1,n2)



if __name__ == '__main__':
    main()
    
