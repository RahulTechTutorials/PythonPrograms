import functools

def main():
    '''This is a program to understand the functionality of Reduce and Lamba functions on List'''
    lst = [1,2,3,4,5,6,7,8,9,10]
    print ('The list is : ',lst )
    cubelst = list(map(lambda x : x ** 3,lst))
    print('The cube operation on lst is : ',cubelst)
    evencubelst = list(filter (lambda x : x%2 == 0 , cubelst))
    print('The even cube lst is : ', evencubelst)
    sumcubeevenlst = functools.reduce(lambda x,y : x + y, evencubelst)
    print('The sum of the evencubelst is: ', sumcubeevenlst)

if __name__ == '__main__':
    main()
