def revstring(n):
    if n == '':
        return ''
    else: 
        return n[-1] + revstring(n[:-1])



def main():
    
    '''This program is to reverese a string'''

    n = input('Enter the string to reverse: ')
    revstr = revstring(n)
    print(revstr)

if __name__ == '__main__':
    main()
