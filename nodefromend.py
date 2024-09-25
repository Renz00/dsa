class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
        
def find_kth_from_end(ll, k):
    if k == 1:
        return ll.tail
    slow = ll.head
    fast = ll.head
    while fast != None: # loop until tail
        for _ in range(k): # fast steps are based on k value
            if fast == None and slow == ll.head: # handle k > linked list length
                return None # out of bounds
            if fast != None:
                fast = fast.next
        if fast == None and slow == ll.head: # handle k = linked list length
            return slow
        slow = slow.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 3
result = find_kth_from_end(my_linked_list, k)

print('RESULT:',result.value if result != None else None)  # Output: 4


"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

