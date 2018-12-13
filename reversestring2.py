def revstring(string):
    rstring = ''
    length = len(string)
    for ch in range(-length,0):
        rstring = string[ch] + rstring
    return rstring

def main():
    '''This is a program to reverse the string entered by the user'''
    string = input('Please enter the string to reverse: ')
    rstring = revstring(string)
    print('The reverse string is : ', rstring)

if __name__ == '__main__':
    main()
