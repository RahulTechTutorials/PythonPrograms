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

        
def main():
    print('Enter a choice to perform the desired operation:')
    print('1: Insert in the begining')
    print('2: Delete from begining')
    print('3: quit')
    lst = Linkedlist()
    while 1:
        choice = int(input('Enter Choice: '))
        if choice == 1 :
            val = eval(input('Enter the Value for the node'))
            lst.insertBegin(val)
        elif choice ==2:
            lst.delBegin()
        elif choice ==3:
            break

     
if __name__ == '__main__':
    main()
            
