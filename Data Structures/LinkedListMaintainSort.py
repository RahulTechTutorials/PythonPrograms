class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def insertBegin(self,value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp
        print('New Linkedlist/Node created ')
    def delBegin(self):
        if self.head == None:
            print('Empty Linked list')
        else:
            temp = self.head
            value = self.head.data
            self.head = self.head.next
            del temp
            print(value,' deleted')
    def delVal(self,value):
        
        if self.head == None:
            print('Linked list is empty')
        else:
            deleteflag = 'No'
            current = self.head
            prev = None
            while current != None:
                if current.data == value:
                    if prev == None:
                        temp = self.head
                        self.head = self.head.next
                        del temp
                        print('Value Deleted: ',value)
                        deleteflag = 'Yes'
                        break
                    else:
                        temp = current
                        prev.next = current.next
                        del current
                        print('Value Deleted: ',value)
                        deleteflag = 'Yes'
                        break
                else:
                    prev = current
                    current = current.next
            if deleteflag == 'No':
                print(value,' Not present in the linkedlist')
    def insertAsPerSort(self,value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
        elif self.head.data >= value:
            temp.next = self.head
            self.head = temp 
            print(value, ' inserted in the sorted linked list')
        elif self.head.data < value:
            current = self.head 
            prev = None
            while current != None:
                if current.next == None and value > current.data :
                    current.next = temp
                    print(value,'Inserted in the end of the queue ' )
                    break
                elif current.data > value and prev.data < value :
                    prev.next = temp
                    temp.next = current
                    print(value,'Inserted between ',prev, ' and ',current )
                    break
                        
                prev = current
                current = current.next
           

    def llprint(self):
        current = self.head
        print('Current Address  data   Next Address   Next')
        while current != None:
            print(id(current), '\t', current.data, '\t', id(current.next),'\t',current.next )
            current = current.next
        return None
            
        
        
def main():
    print('Enter a choice to perform the desired operation:')
    print('1: Insert in the begining')
    print('2: Delete from begining')
    print('3: Delete a specific value')
    print('4: Print the Linkedlist')
    print('5: Insert as per Sorting order')
    print('6: quit')
    
    lst = Linkedlist()
    while 1:
        choice = int(input('Enter Choice: '))
        if choice == 1 :
            val = eval(input('Enter the Value for the node'))
            lst.insertBegin(val)
        elif choice ==2:
            lst.delBegin()
        elif choice ==3:
            val = eval(input('Enter the Value to be deleted'))
            lst.delVal(val)
        elif choice == 4:
            lst.llprint()
        elif choice == 5:
            val = eval(input('Enter the Value for the node'))
            lst.insertAsPerSort(val)
        elif choice ==6:
            break

            
     
if __name__ == '__main__':
    main()
            
