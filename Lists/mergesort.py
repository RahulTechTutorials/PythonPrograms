def merge(lst1,lst2):
    
    sortedlst = []  
    while len(lst1) != 0 and len(lst2) != 0:
        if lst1[0] < lst2[0]:
            sortedlst.append(lst1[0])
            lst1.remove(lst1[0])
        else:
            sortedlst.append(lst2[0])
            lst2.remove(lst2[0])
    
    if len(lst1) ==0 :
        sortedlst += lst2
    elif len(lst2) ==0 :
        sortedlst += lst1
    return sortedlst
    

def mergesort(lst):
    
    if len(lst) == 0 or len(lst) == 1:
        return lst
    mid = len(lst) // 2
    lst1 = mergesort(lst[:mid])
    lst2 = mergesort(lst[mid:])
    return merge(lst1,lst2) 
    

def main():
    lst = [15,17,13,11,12,16,14]
    print('The original list is:\n',lst)
    mergedsort = mergesort(lst)
    print('The sorted list is\n',mergedsort)
    
if __name__ == '__main__':
    main()
