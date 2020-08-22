class Node:
    def __init__(self,data):
        self.val = data
        self.right = None
        self.left = None

class Binary_Tree:
    def search(self,root,data):
        if root == None:
            return False

        if root.val == data:
            return True
        
        if data > root.val:
            self.search(root.right,data)
        else:
            self.search(root.left,data)

    def add(self,root,node):
        if root == None:
            root = node
        else:
            if root.val < node.val:
                root.lheight+=1
                if root.right is None: 
                    root.right = node 
                else: 
                    self.add(root.right, node) 
            else: 
                if root.left is None: 
                    root.left = node 
                else: 
                    self.add(root.left, node) 

    def InOrder(self,root):
        if root:
            self.InOrder(root.left)
            print(root.val)
            self.InOrder(root.right)

    def PostOrder(self,root):
        if root:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.val)

    def PreOrder(self,root):
        if root:
            print(root.val)
            self.PreOrder(root.left)
            self.PreOrder(root.right)

binary = Binary_Tree()
root = Node(9)
binary.add(root,Node(8))
binary.add(root,Node(7))
binary.add(root,Node(6))
binary.add(root,Node(5))
binary.add(root,Node(4))
binary.InOrder(root)