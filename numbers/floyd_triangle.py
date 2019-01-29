def floydtriangle(rows):
    '''
Program to print floyd triangle which
1
23
456
and so on
'''
    print('floyd triangle')
    counter = 1
    for i in range(1,rows+1):
        for j in range(i):
            print(counter,end="")
            counter += 1
        print('\n')

def revfloydtriangle(row):
    print('Reverse floyd triangle')
    
    for i in range(row,0,-1):
        n = int((i * (i-1)/2) + 1)
        for j in range(i):
            print(n,end="")
            n += 1
        print('\n')
        

if __name__ == '__main__':
    rows = int(input('Enter the number of row for floyd triangle:'))
    floydtriangle(rows)
    revfloydtriangle(rows)
