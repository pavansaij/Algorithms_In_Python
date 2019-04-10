class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1

class AVL():
    def __init__(self):
        self.parent = None
    
    def insert(self,data,root="Empty"):
        if self.parent == None:
            self.parent = Node(data)
            return 
        else:
            if root == "Empty":
                root = self.parent
        
        if root == None:
            root = Node(data)
            return 
        
        if root.data < data:
            root.height+=1
            if root.right == None:
                root.right = Node(data)
            else:
                self.insert(data,root.right)
        else:
            root.height+=1
            if root.left == None:
                root.left = Node(data)
            else:
                self.insert(data,root.left)
    
    def inorder(self,root="Empty"):
        if self.parent == None:
            return 
        else:
            if root == "Empty":
                root = self.parent
        if root:
            self.inorder(root.left)
            print(root.data,root.height)
            self.inorder(root.right)

bst = AVL()
bst.insert(6)
bst.insert(8)
bst.insert(4)
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(9)
bst.insert(10)
bst.inorder()
data = 1
data.__hash__()