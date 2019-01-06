class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
    def push(self,value):
        if self.top == None:
            self.top = Node(value)
        else:
            temp = Node(value)
            temp.next = self.top
            self.top = temp
        print('New LinkedStack created ')
    def pop(self):
        if self.top == None:
            print('Empty LinkedStack ')
            return None
        else:
            temp = self.top
            value = self.top.data
            self.top = self.top.next
            del temp
            return value
    def isEmpty(self):
        return self.top is None
        
    def getTop(self):
        if self.top == None:
            return None
        else : 
            return self.top.data
    def __str__(self):
        current = self.top
        result = ''
        while current != None:
            result += str(current.data) + '->'
            current = current.next
        return result
        
        
def main():
    print('Enter a choice to perform the desired operation:')
    print('1: Create Stack')
    print('2: Delete Stack')
    print('3: Push')
    print('4: Pop')
    print('5: Print Stack data')
    print('6: Top Element')
    print('7: Quit')
    
    
    while 1:
        choice = int(input('Enter Choice: '))
        if choice == 1 :
            lst = LinkedStack()
            print('Stack Created')
        elif choice ==2:
            del lst
            print('Stack Deleted')
        elif choice ==3:
            val = eval(input('Enter the Value to be pushed'))
            lst.push(val)
            print('Value Pushed: ',val)
        elif choice == 4:
            val = lst.pop()
            print('Value Popped: ',val)
        elif choice == 5:
            print(lst)
        elif choice ==6:
            topelement = lst.getTop()
            print('The top element is: ',topelement)
        elif choice ==7:
            break
     
if __name__ == '__main__':
    main()
            
