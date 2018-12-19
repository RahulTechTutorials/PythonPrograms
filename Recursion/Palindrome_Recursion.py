def palindrome(n):
    length = len(n)
    if n == '':
        return 'Yes'
    elif n[-length] == n[-1] and palindrome(n[1:length-1]) == 'Yes':
        return 'Yes'
    else: 
        return 'No'



def main():
    
    '''This program is to reverese a string'''

    n = input('Enter the string to reverse: ')
    status = palindrome(n)
    print('If the string is palindrome : ', status)

if __name__ == '__main__':
    main()
    
