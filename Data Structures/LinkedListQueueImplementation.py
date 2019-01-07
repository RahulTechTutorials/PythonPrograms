class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
## Front ->> Rear--> None
class LinkedQueue:
    def __init__(self):
        self.front = self.rear =  None
    def enqueue(self,value):
        if self.front == None:
            self.front = self.rear =  Node(value)
        else:
            temp = Node(value)
            self.rear.next = temp
            self.rear = temp
        print('New value inserted in the Linked Queue ')
    def dequeue(self):
        if self.front == None:
            print('Empty LinkedStack ')
            return None
        else:
            temp = self.front
            value = self.front.data
            self.front = self.front.next
            del temp
            return value
    def isEmpty(self):
        if self.rear == self.front == None:
            return True
        else: 
            return False
            
    def getFront(self):
        if self.front == None:
            return None
            print('The Linked queue is empty')
        else : 
            return self.front.data
    def __str__(self):
        current = self.front
        result = ''
        while current != None:
            result += str(current.data) + '->'
            current = current.next
        return result
        
        
def main():
    print('Enter a choice to perform the desired operation:')
    print('1: Create Queue')
    print('2: Delete Queue')
    print('3: Enqueue')
    print('4: Dequeue')
    print('5: Print Queue data')
    print('6: Front Element')
    print('7: Quit')
    
    
    while 1:
        choice = int(input('Enter Choice: '))
        if choice == 1 :
            qu = LinkedQueue()
            print('Queue Created')
        elif choice ==2:
            del qu
            print('Queue Deleted')
        elif choice ==3:
            val = eval(input('Enter the Value to be enqueued'))
            qu.enqueue(val)
            print('Value queued: ',val)
        elif choice == 4:
            val = qu.dequeue()
            print('Value removed: ',val)
        elif choice == 5:
            print(qu)
        elif choice ==6:
            frontelement = qu.getFront()
            print('The front element is: ',frontelement)
        elif choice ==7:
            break
     
if __name__ == '__main__':
    main()
            
