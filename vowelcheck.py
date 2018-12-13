def main():
    '''This program is to identify the number of vowels in the string entered by the user'''
    try:
        string = input('Enter the string in which you want to find out the Vowels: ')
        vowels = 'aeiou'
        
        if string.isalpha():
            print('Here are the counts of vowels')
            for alp in vowels:
                print(alp,' count : ',string.count(str(alp))  )
        else: 
            print('The entered string should be alphabets')
    except ValueError:
                print('The entered string is not correct')

if __name__ == '__main__':
    main()
            
