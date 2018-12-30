def partition(lst,low,high):
    pivot = lst[high]
    i = low - 1
    for j in range(low,high):
        if lst[j] <= pivot:
            i+=1
            lst[i],lst[j] = lst[j],lst[i]
    lst[i+1],lst[high] = lst[high],lst[i+1]
    return i+1
        
def quicksort(lst, low = 0, high = None):
    if high == None:
        high = len(lst) -1 
    if low < high:
        splitpoint = partition(lst,low,high)
        quicksort(lst,low,splitpoint-1)
        quicksort(lst,splitpoint+1,high)
    return lst
    

def main():
    lst = [15,17,13,11,12,16,14]
    print('The original list is:\n',lst)
    quicksort1 = quicksort(lst)
    print('The sorted list is\n',lst)
    
if __name__ == '__main__':
    main()
