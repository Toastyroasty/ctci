from LinkedList import *

def massDelete(head, value):
    # Given the head of a linked list, removes all nodes with a given value. 
    #   Returns a (reduced) linked list
    if head is None:
        return head
    
    if head.data == value:
        if head.next is None:
            return None
        head = head.next
        
    head.next = massDelete(head.next, value)
    return head

def removeDuplicates(head):
    # Remove duplicates from an unsorted linked list, assuming a temporary 
    #  buffer is not allowed.
    if head is None:
        return head
    
    curr = head
    while curr.next is not None:
        curr.next = massDelete(curr.next, curr.data)
        curr = curr.next
    return head
        
LL = LinkedList()
LL.appendList([7, 3, 1, 7, 4, 3])
LL.head = removeDuplicates(LL.head)
LL.traverse()