from PIL import Image
class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data, end = '->')
        inorder(root.right)
        
def preorder(root):
    if root != None:
        print(root.data,end = ' ')
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = ' ')
def height(root):
    if root == None or (root.left == None and root.right == None):
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))

        

def main():
    Image.open('/Users/rahuljain/Desktop/Python/PythonPrograms/Data Structures/BinarySearchTree.jpeg').show()
    bst = Node(15)
    bst.left = Node(10)
    bst.left.left = Node(6)
    bst.right = Node(23)
    bst.right.left = Node(20)
    bst.right.right = Node(30)
    print('\nThis is inorder traversal')
    inorder(bst)
    print('\nThis is preorder traversal')
    preorder(bst)
    print('\nThis is postorder traversal')
    postorder(bst)    
    print('\nThe height of the BST is: ',height(bst))
     
if __name__ == '__main__':
    main()
            
