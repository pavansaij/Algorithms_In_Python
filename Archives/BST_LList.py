class LNode():
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class LinkedList():
    def __init__(self):
        self.head = None

    def add_root(self,data):
        self.head = LNode(data)

    def append(self,data):
        if self.head == None:
            self.add_root(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = LNode(data)
    
    def mid(self,root):
        slow = root
        fast = root
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow

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

    def sortedArrayToBST(self,arr):   
        if not arr: 
            return None
        
        mid = (len(arr)) // 2
        root = Node(arr[mid]) 
        root.left = self.sortedArrayToBST(arr[:mid]) 
        root.right = self.sortedArrayToBST(arr[mid+1:]) 
        return root

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

arr = [1,2,4,5,8,9,10]
bst = BST()
root = bst.sortedArrayToBST(arr)
bst.inorder(root)