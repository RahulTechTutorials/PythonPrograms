from string import punctuation

def validator(pswd):
    '''
Program to check the validaty of the password entered
The password should conform to below standards:
-Minimum length is 5
-Maximum length is 10
-Should contain at least one number
-Should contain at least one special character eg. (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
-Should not contain spaces
'''
    num_flag = 'N'
    spe_flag = 'N'
    numbers = [str(i) for i in range(10)]
    if len(pswd) >= 5 and len(pswd) <= 10 and " " not in pswd:
        for char in pswd:
            if char  in numbers:
                num_flag = 'Y'
            elif char in punctuation:
                spe_flag = 'Y'
        if num_flag == 'Y' and spe_flag == 'Y':
            return True
        else: return False
    return False
    
if __name__ == '__main__':
    pswd = input('Enter the password to check its validaity:')
    check = validator(pswd)
    print(check)
    
 
