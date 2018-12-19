def flattenlist(megalist):
    for element in megalist:
        if type(element) is list :
            flattenlist(element)
        else:
            result.append(element)
    return result
    

def main():
    
    '''This program is to flatten a list'''
    global result
    result = []
    megalist = [1,2,3,[4,5,6,7],8,9,10,[11,[12,13,[14]]],15,16] 
    flattenedlist = flattenlist(megalist)
    print('Original list is: ', megalist)
    print('The flattened list is : ', flattenedlist)

if __name__ == '__main__':
    main()
    
