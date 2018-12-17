def main():
    '''This is a program to understand the functionality of Reduce and Lamba functions on List'''
    lst = []
    complst = []
    primlst = []
    for i in range(2,101):
         lst.append(i)
    for x in lst:
        for y in range(2,x):
            if x % y == 0:
                complst.append(x)
                break
            else: 
                continue
    primlst = [item for item in lst if item not in complst] 
    print(primlst)
    
if __name__ == '__main__':
    main()
