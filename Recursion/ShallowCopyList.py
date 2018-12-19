
def shallowcopy(megalist):
    
     
    if megalist:
        result.append(megalist[0])
        shallowcopy(megalist[1:])
    return result
    

def main():
    
    '''This program is to understand shallowcopy'''
    global result
    result = []
    megalist = [1,2,3,[4,5]] 
    normalcopylist = megalist.copy()
    finallist = shallowcopy(megalist)
    megalist[0] = 100
    megalist[3][0] = 400
    print('Original list is: ', megalist, ' and ID is : ',id(megalist), ' and id of Internal list is: ', id(megalist[3]))
    print('List copied normally is : ', normalcopylist , ' and the ID is : ', id(normalcopylist), ' and id of Internal list is: ', id(normalcopylist[3]))
    print('The copied list is : ', finallist, ' and ID is : ', id(finallist), ' and id of Internal list is: ', id(finallist[3]))
    print()
    print ('As you can see the reference to all lists are different but the Internal list is same,i updated below values     megalist[0] = 100 and megalist[3][0] = 400. While the first value in copied list doesnt get updated, the changes to internal list gets reflected in copied lists. This is shallow copy')

if __name__ == '__main__':
    main()
    
