def insertionsort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i-1
        while j >= 0 and temp < lst[j]:
            lst[j+1] = lst[j]
            j -= 1      
        lst[j+1] = temp

def main():
    lst = ['Vijaya','Sanvi','Priyanka','Shweta','Priya','Ahana','Bharti']
    print('The original list is:\n',lst)
    insertionsort(lst)
    print('The sorted list is:\n',lst)

if __name__ == '__main__':
    main()
