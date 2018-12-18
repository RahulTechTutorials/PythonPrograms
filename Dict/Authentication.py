def authentication(username,password):
    
    if (username,password) in creds.items():
        print('Congratulations, you are now logged into the system' )
    else: 
        print('The username and password is incorrect')



def main():
    '''This program will allow you to enter the system if you put correct username and password.
           The correct username and passwords are: bill@gates ; steve@jobs ; larry@page  ; sergey@brin
           Please use one of these credentials to login to the system
       '''
    
    print('This program will allow you to enter the system if you put correct username and password.\
           The correct username and passwords are: bill@gates ; steve@jobs ; larry@page  ; sergey@brin\
           Please use one of these credentials to login to the system')
    global creds
    creds = {'bill' : 'gates', 'steve' : 'jobs' , 'larry' : 'page' , 'sergey' : 'brin' }
    username = input('Username: ')
    password = input('Password: ')
    authentication(username,password)

        

if __name__ == '__main__':
    main()
    
