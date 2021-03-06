class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class binSearchTree:
    def __init__(self):
        self.root = None
    
    def inorder(self):
        if self.root != None:
            inorder(self.root.left)
            print(self.root.data, end = ' ')
            inorder(self.root.right)
        
    def height(self):
        if self.root == None or (self.root.left == None and self.root.right == None):
            return 0
        else:
            return 1 + max(height(self.root.left), height(self.root.right))
    def insert(self,value)   :
        def insertVal(root,value):
            if root == None:
                root = Node(value)
            elif value <= root.data:
                root.left = insertVal(root.left,value)
            else:
                root.right = insertVal(root.right,value)
                
            return root
        self.root = insertVal(self.root,value)
    
                

def main():
    

    while 1: 
        print('\nEnter a choice to perform operation')
        print('1: To initialize a binary Search tree')
        print('2: To insert a value in binary Search tree')
        print('3: To print inorder traversing in binary Search tree')
        print('4: To print the height of binary Search tree')
        print('5: To delete the binary Search tree')
        print('6: To Exit')
        choice = int(input('Enter Choice'))
        
        if choice == 1:
            bst = binSearchTree() ; print('BST initialized')
        elif choice == 2:
            val= eval(input('Enter the value to be inserted'))
            bst.insert(val)
        elif choice == 3:
            print('\nThis is inorder traversal') ; bst.inorder()
        elif choice == 4:
            print('\nThe height of the BST is: ',bst.height())
        elif choice == 5:
            del bst
        else: break
            
     
if __name__ == '__main__':
    main()
            
