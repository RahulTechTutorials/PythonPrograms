def ASCII_Converter():
    '''
    This is a program to return the ASCII values, eg. Input : "xyz"; Output : 120 121 122
    '''
    st = (ord(c) for c in input())
    print(*st)
    
if __name__ == '__main__':
    ASCII_Converter()
