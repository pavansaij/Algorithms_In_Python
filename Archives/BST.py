class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BST():
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
            if root.right == None:
                root.right = Node(data)
            else:
                self.insert(data,root.right)
        else:
            if root.left == None:
                root.left = Node(data)
            else:
                self.insert(data,root.left)

    def pre_order(self,root="Empty"):
        if self.parent == None:
            return 
        else:
            if root == "Empty":
                root = self.parent
        
        if root:
            print(root.data)
            self.inorder(root.left)
            self.inorder(root.right)

    def post_order(self,root="Empty"):
        if self.parent == None:
            return 
        else:
            if root == "Empty":
                root = self.parent
        
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data)
            
    def inorder(self,root="Empty"):
        if self.parent == None:
            return 
        else:
            if root == "Empty":
                root = self.parent
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

bst = BST()
bst.insert(7)
bst.insert(5)
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(3)
bst.insert(2)
bst.insert(8)
bst.insert(10)
bst.insert(11)
bst.pre_order()