import functools

def main():
    '''This is a program to understand the functionality of Map,Reduce, Filter and Lamba functions with shortcut on List'''
    lst = [1,2,3,4,5,6,7,8,9,10]
    print ('The list is : ',lst )
    sumcubeevenlst = functools.reduce(lambda x,y : x + y, filter (lambda x : x%2 == 0 , list(map(lambda x : x ** 3,lst))))
    print('The sum of the evencubelst is: ', sumcubeevenlst)

if __name__ == '__main__':
    main()
