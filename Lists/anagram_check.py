def anagram(string):
    '''This is a program to check the string entered is an anagram or not '''
    charset = set(string)
    return { i : string.count(i) for i in charset}

def main():
    string = input('Enter the first string :')
    string2 = input('Enter the second string to check the anagram:')
    result1 = anagram(string)
    result2 = anagram(string2)
    print(result1,result2)
    if result1 == result2:
        print('The two strings are anagrams')
    else:
        print('The two strings are not anagrams')
    
if __name__ == '__main__':
    main()
