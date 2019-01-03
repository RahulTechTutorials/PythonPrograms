class queue:
    def __init__(self):
        self.values = list()
    
    def enqueue(self,element):
        self.values.append(element)
    
    def isEmpty(self):
        return len(self.values) == 0
    
    def dequeue(self):
        if not ( self.isEmpty() ):
            return self.values.pop(0)
        else:
            print('Empty Queue')
            return None
    
    def front(self):
        if not ( self.isEmpty() ):
            return self.values[0]
        else:
            print('Empty Queue')
            return None
            
    
    def size(self):
        return len(self.values)
    
    def __str__(self):
        stringrep = ''
        for i in (self.values):
            stringrep += str(i) + '\t'
        return stringrep
        
        
def main():
    
    while 1:
        print('Choose one of the queue operation:')
        print('1: Create queue ')
        print('2: Delete queue ')
        print('3: Enqueue ')
        print('4: Dequeue ')
        print('5: Print queue data ')
        print('6: Front element')
        print('7: No of elements ')
        choice = int(input('Enter Choice: '))
        if choice == 1:
            qu = queue()
        elif choice ==2:
            del qu
        elif choice ==3:
            qu.enqueue(int(input('Enter the element to insert in queue: ')))
            print('Element inserted in the queue')
        elif choice ==4:
            print('Element dequeued : ',qu.dequeue())
        elif choice ==5:
            print(qu)
        elif choice ==6:
            print(qu.front())
        elif choice ==7:
            print('The no of elements in the queue are:',qu.size())
        
        proceed = input('Press y/Y to continue:')
        if proceed == 'y' or proceed == 'Y':
            continue
        else: break
        
     
if __name__ == '__main__':
    main()
            
