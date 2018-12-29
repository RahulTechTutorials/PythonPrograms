def binarysearch(lst,searchvalue):
    low,high = 0,len(lst) - 1
    mid = int ((low + high)/2)
    found = 'No'
    while low != high:
        if searchvalue == lst[mid]:
            print(searchvalue,' found at index : ', mid)
            found = 'Yes'
            break
        elif searchvalue < lst[mid]:
            high = mid - 1
            if searchvalue == lst[high]:
                print(searchvalue,' found at index : ', high)
                found = 'Yes'
                break
        elif searchvalue > lst[mid]:
            low = mid + 1
            if searchvalue == lst[low]:
                print(searchvalue,' found at index : ', low)
                found = 'Yes'
                break
        mid = int ((low + high)/2)
    if found == 'No':
        print('The name "',searchvalue,'" is not found in the list')



def main():
    lst = ['Ahana', 'Bharti', 'Priya', 'Priyanka', 'Sanvi', 'Shweta', 'Vijaya']
    print('The original list is:\n',lst)
    searchvalue = input('Enter the name to search:')
    binarysearch(lst,searchvalue)

if __name__ == '__main__':
    main()
