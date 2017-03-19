class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(data)
            
    def appendList(self, L):
        for i in L:
            self.append(i)
            
    def traverse(self):
        curr = self.head
        while curr is not None:
            print curr.data
            curr = curr.next
            
    def prepend(self, data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead
        
    def delete(self, value):
        if self.head is None: 
            return
        if self.head.data == value:
            self.head = self.head.next
            return value
        
        curr = self.head
        while curr.next is not None:
            if curr.next.data == value:
                curr.next = curr.next.next
                return value
            curr = curr.next