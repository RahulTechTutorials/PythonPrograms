def revstring(string):
    rstring = ''
    length = len(string)
    for ch in range(-1,-length-1,-1):
        rstring += string[ch]
    return rstring

def main():
    '''This is a program to reverse the string entered by the user'''
    string = input('Please enter the string to reverse: ')
    rstring = revstring(string)
    print('The reverse string is : ', rstring)

if __name__ == '__main__':
    main()
    
