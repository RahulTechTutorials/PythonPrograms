def palindrome(string):
    rstring = ''
    for ch in string:
        rstring =  ch + rstring
    if string == rstring:
        return 'Yes'
    else:
        return 'No'


def main():
    '''This is a program to check if the number is palindrome, example kayak'''
    string = input('Please enter the string to check if it is palindrome like kayak: ')
    result = palindrome(string)
    print('The string is palindrome or not : ', result)

if __name__ == '__main__':
    main()
