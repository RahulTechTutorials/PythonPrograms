class stack:
    def __init__(self):
        self.values = list()
    
    def push(self,element):
        self.values.append(element)
    
    def isEmpty(self):
        return len(self.values) == 0
    
    def pop(self):
        if not ( self.isEmpty() ):
            return self.values.pop()
        else:
            print('Stack Underflow')
            return none
    
    def top(self):
        if not ( self.isEmpty() ):
            return self.values[-1]
        else:
            print('Stack Underflow')
            return none
    
    def size(self):
        return len(self.values)
    
    def __str__(self):
        stringrep = ''
        for i in reversed(self.values):
            stringrep += str(i) + '\t'
        return stringrep
            

def main():
    while 1:
        print('Choose and option \n')
        print('1: Create stack')
        print('2: Delete stack')
        print('3: Push')
        print('4: Pop')
        print('5: Print Stack Data')
        print('6: Top Element')
        print('7: No. Of elements')
        choice = int(input('Enter Choice: '))
        
        if choice == 1:
            stk = stack()
            print('Stack Created')
        elif choice == 2:
            del stk
            print('Stack Deleted')
        elif choice == 3:
            element = int(input('Enter the numberic element'))
            stk.push(element)
        elif choice == 4:
            print('Element popped: ',stk.pop())
        elif choice == 5:
            print(stk)
        elif choice == 6:
            print('The top element of the stack is : ',stk.top())
        elif choice == 7:
            print('The size of the stack is : ',stk.size())
        
        proceed = input('Enter Y/y if you want to proceed: ')
        if proceed != 'y' and proceed != 'Y':
            break

if __name__ == '__main__':
    main()
            
        
        
        
