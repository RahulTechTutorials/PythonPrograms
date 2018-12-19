import copy
def deepcopy(megalist, result=[]):
    if megalist == []:
        pass
    else:
        if type(megalist[0]) != list:
            result.append(megalist[0])
        else:
            result.append([])
            deepcopy(megalist[0],result[-1])
        deepcopy(megalist[1:], result)
    return result 

def main():
    
    '''This program is to understand shallowcopy'''
    global result
    result = []
    megalist = [1,2,3,[4,5]] 
    normalcopylist = copy.copy(megalist)
    deepcopylist = copy.deepcopy(megalist)
    finallist = deepcopy(megalist)
    megalist[0] = 100
    megalist[3][0] = 400
    print('Original list is: ', megalist, ' and ID is : ',id(megalist), ' and id of Internal list is: ', id(megalist[3]))
    print('Normal Copy : ', normalcopylist , ' and the ID is : ', id(normalcopylist), ' and id of Internal list is: ', id(normalcopylist[3]))
    print('Deep Copy : ', deepcopylist , ' and the ID is : ', id(deepcopylist), ' and id of Internal list is: ', id(deepcopylist[3]))
    print('The copied list is : ', finallist, ' and ID is : ', id(finallist), ' and id of Internal list is: ', id(finallist[3]))
    print()
    print ('As you can see the reference to all lists are different but the Internal list is same,i updated below values     megalist[0] = 100 and megalist[3][0] = 400. While the first value in copied list doesnt get updated, the changes to internal list gets reflected in copied lists. This is shallow copy; However in Deep copy, if you see the below two rows, all references are different. The change to values to all are not visible')

if __name__ == '__main__':
    main()
    
