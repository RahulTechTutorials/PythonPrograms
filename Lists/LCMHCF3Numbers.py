def LCM(num1,num2,num3):
    multiplier = 1
    while True:
        Num = num1 * multiplier
        if Num % num3 == 0 and Num % num2 == 0: 
            print('The LCM of three number ',num1, ',',num2, '&', num3, ' is : ', Num )
            break
        else:
            multiplier += 1
            continue

def HCF(num1,num2,num3):
    Num = {num1,num2,num3}
    Max = max(Num)
    Fset = set()
    for i in range(1,Max+1):
        if num1%i ==0 and  num2%i ==0 and num3%i ==0 :
            Fset.add(i)
    print('The HCF of ', num1,',',num2,'&',num3, 'is : ',max(Fset))
   
def main():
    '''This is a program to find the LCM and HCF for 3 numbers'''
    try:
        num1 = int(input('Enter the first number: ' ))
        num2 = int(input('Enter the second number: ' ))
        num3 = int(input('Enter the third number: ' ))
        LCM(num1,num2,num3)
        HCF(num1,num2,num3)
    except ValueError: 
        print('The number entered is non interger')
    
if __name__ == '__main__':
    main()
