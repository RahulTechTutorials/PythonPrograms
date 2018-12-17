def passwordcheck():
    
    count = 1
    while count < 4:
        password = input('Password: ')
        if password == 'luhar':
            print('Congratulations, You are logged into the system')
            break
        elif count == 3:
            print('You exhausted the number of attempts to log in')
            break
        else:
            print('The password entered is not correct, Please reenter(Max 3 attempts)')
            count += 1


def main():
    '''This program will allow you to enter the system if you put correct username and password - Dictionary.
       The correct username and password are as fellow:
       username : rahul
       password : luhar
       '''
    count = 1
    while count <4:
        username = input('Username: ')
        if username == 'rahul':
            passwordcheck()
            break
        elif count == 3:
            print('You exhausted the number of attempts to log in')
            break
        else:
            print('The username entered is not correct, Please reenter(Max 3 attempts)')
            count += 1

        

if __name__ == '__main__':
    main()
    
