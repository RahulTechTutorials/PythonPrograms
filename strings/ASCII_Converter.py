def ASCII_Converter(string):
    '''
    This is a program to return the ASCII values, eg. Input : "xyz"; Output : 120 121 122
    '''
    for i in string:
        print('ASCII value of ',i,' : ',ord(i))
    
if __name__ == '__main__':
    string = input('Enter the string to convert into ASCII values: ')
    ASCII_Converter(string)
