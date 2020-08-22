class Node():
    def __init__(self,val):
        self.data = val
        self.next = None
        

class LinkedList():
    def __init__(self):
        self.head = None

    def add_root(self,data):
        self.head = Node(data)

    def append(self,data):
        if self.head == None:
            self.add_root(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def pop(self):
        if self.head == None:
            raise Exception('Cannot pop from empty LinkedList')

        if self.head.next == None:
            self.head = None
            return

        current = self.head
        prev  = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def ret_head(self):
        return self.head.data

    def ret_next(self,root):
        if root.next:
            root = root.next
            return root.data
        else:
            return None

    def display(self,arg=None):
        if self.head == None:
            raise Exception('List is empty')

        if arg == None:
            current = self.head
            print(self.ret_head(),end=' ')
            while (self.ret_next(current)):
                if  current.next.next == None:
                    print(self.ret_next(current))
                else:
                    print(self.ret_next(current),end = ' ')
                current = current.next
        elif arg == 'rev':
            def print_rev(root):
                if root == None:
                    return
                print_rev(root.next)
                if root.next == None:
                    print(root.data)
                else:
                    print(root.data,end=' ')
            print_rev(self.head)

    def reverse(self):
        current = self.head
        prev = None
        while current:
            nxt = current.next 
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def mid(self):
        slow = self.head
        fast = self.head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    def rotate(self,k):
        if k == 0:
            return    
        current = self.head
        while (k != 1 and current):
            current = current.next
            k-=1
        if current == None:
            return
        new_head = current
        while (current.next):
            current = current.next
        current.next = self.head
        self.head = new_head.next
        new_head.next = None

    def createLoop(self, n):
        if n == 0:
            return None
        temp = self.head
        ptr = self.head
        cnt = 1
        while (cnt != n):
            ptr = ptr.next
            cnt += 1
        
        while (temp.next):
            temp = temp.next
        temp.next = ptr

    def detectloop(self):
        slow = self.head
        fast = self.head
        while (slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def detect_remove_loop(self):
        slow = self.head
        fast = self.head
        while (slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while (slow.next != fast.next): 
                    slow = slow.next
                    fast = fast.next
                fast.next = None

ll = LinkedList()
ll.append(3)
ll.append(6)
ll.append(8)
ll.append(5)
ll.append(10)
ll.append(11)