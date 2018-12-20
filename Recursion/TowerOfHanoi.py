def hanoi(n,source,spare, target):
    if n ==1:
        print('Move a dics from', source, ' to ', target)
    elif n ==0:
        return
    else: 
        hanoi(n-1,source,target, spare)
        print('Move a dics from', source, ' to ', target)
        hanoi(n-1,spare,source,target)

def main():
          n = int(input('Enter the number of discs'))
          hanoi(n,'Pole1','Pole2','pole3')


if __name__ == '__main__':
    main()
    
