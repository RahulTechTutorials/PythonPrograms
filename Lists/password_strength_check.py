import re
def password_strength_check(password):

    with_uppercase = re.search(r'[A-Z]+', password)
    with_lowercase = re.search(r'[a-z]+', password)
    with_numbers = re.search(r'[0-9]+', password)
    with_symbols = re.search(r'.[@#$%^&!;+-.,/\|]+.', password)
    adequate_length = len(password) >= 8
    passing_conditions = len(list(filter(lambda x : bool(x) == True,[with_uppercase, with_lowercase, with_numbers, with_symbols, adequate_length])))
    output = ["Extremely Weak", "Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    print("Your password:", password)
    print("Password Security Level:", output[passing_conditions])

def main():
    '''
    Program to check the strength of password
    '''
    pswd = input('Please input the password to check the strength: ')
    password_strength_check(pswd)

if __name__ == '__main__':
    main()
    
