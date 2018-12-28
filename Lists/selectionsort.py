def selectionsort(lst):
    for i in range(0,len(lst) -1):
        minindex = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[minindex]:
                minindex = j
        if minindex != i:
            lst[i],lst[minindex] = lst[minindex],lst[i]
    return lst
    
    
def main():
    lst = ['Vijaya','Sanvi','Priyanka','Shweta','Priya','Ahana','Bharti']
    print('The original list is:\n',lst)
    sortedlst = selectionsort(lst)
    print('The sorted list is:\n',sortedlst)

if __name__ == '__main__':
    main()
