def bubblesort(lst):
    for i in range(0, len(lst) -1):
        for j in range(len(lst)-1,i,-1):
            if lst[j] < lst[j-1]:
                lst[j],lst[j-1] = lst[j-1],lst[j]


def main():
    lst = ['Vijaya','Sanvi','Priyanka','Shweta','Priya','Ahana','Bharti']
    print('The original list is:\n',lst)
    bubblesort(lst)
    print('The sorted list is:\n',lst)

if __name__ == '__main__':
    main()
