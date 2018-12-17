def LCM(num1,num2,num3):
    lcm = {num1 * mul for mul in range(1,(num2*num3)+1) if (num1 * mul)%num2 == 0 and (num1 * mul)%num3 == 0 }
    print('The LCM of ', num1,',',num2,'&',num3, 'is : ',min(lcm))


def HCF(num1,num2,num3):
    commonfac = set()
    commonfac = {i for i in range(1,min(num1,num2,num3) + 1) if num1%i == 0 and num2%i==0 and num3%i==0}
    print('The HCF of ', num1,',',num2,'&',num3, 'is : ',max(commonfac))
   
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
