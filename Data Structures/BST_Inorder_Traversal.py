from PIL import Image
class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data,end = ' ')
        inorder(root.right)
        

def main():
    Image.open('/Users/rahuljain/Desktop/Python/PythonPrograms/Data Structures/BinarySearchTree.jpeg').show()
    bst = Node(15)
    bst.left = Node(10)
    bst.left.left = Node(6)
    bst.right = Node(23)
    bst.right.left = Node(20)
    bst.right.right = Node(30)
    inorder(bst)
     
if __name__ == '__main__':
    main()
            
