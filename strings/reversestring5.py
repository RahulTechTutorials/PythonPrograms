def revstring(string):
    orgstring = string
    for ch in string:
        string = ch + string
    if string == (orgstring * 2) :
        return orgstring
    else:
        return string.replace(orgstring,'')


def main():
    '''This is a program to reverse the string entered by user'''
    string = input('Please enter the string to reverse: ')
    rstring = revstring(string)
    print('The reverse string is : ', rstring)

if __name__ == '__main__':
    main()
