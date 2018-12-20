def permute(lst1, lst2 = [], k = 0 , pos = 0):
    lst2.insert(pos, lst1[k])
    
    if len(lst1) == len(lst2):
        print(lst2)
    else: 
        permute(lst1,lst2,k+1,0)
    
    lst2.remove(lst1[k])
    
    if pos < k:
        permute(lst1,lst2,k,pos+1)



def main():
    
    '''This program is to show permutation'''
    lst1 = [1,2,3]
    permute(lst1)

if __name__ == '__main__':
    main()
    
