import re

def main():
    '''Program to check weather the enter text is a valid email id or not'''
    string = input('Enter the text to be checked for email id: ')
    if re.findall(r'[a-z0-9]+(\.[a-z0-9]+)?@[a-z]+(\.[a-z]+)+',string) and not re.findall(r'\.\.',string):
            print('The entered string is a valid email id')
    else:
        print('The entered string is not a valid email id')
    
if __name__ == '__main__':
    main()
