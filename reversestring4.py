def revstring(string):
    if string == '':
        return string
    else :
        return revstring(string[1:]) + string[0]

def main():
    '''This is a program to reverse the string entered by the user'''
    string = input('Please enter the string to reverse: ')
    rstring = revstring(string)
    print('The reverse string is : ', rstring)

if __name__ == '__main__':
    main()
    
