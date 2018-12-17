import functools

def main():
    '''This is a program to understand the functionality of Reduce and Lamba functions on List'''
    lst = [1,2,3,4,5,6,7,8,9,10]
    print ('The list is : ',lst )
    cubelst = list(map(lambda x : x ** 3,lst))
    print('The cube operation on lst is : ',cubelst)
    sumcubelst = functools.reduce(lambda x,y : x + y, cubelst)
    print('The sum of the cubelst is: ', sumcubelst)

if __name__ == '__main__':
    main()
