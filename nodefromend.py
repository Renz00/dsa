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
    slow = ll.head
    fast = ll.head
    while slow != None:
        for _ in range(k):
            print('Fast', fast.value if fast != None else None)
            if fast != None: 
                fast = fast.next
                
        print('> Slow',slow.value if slow != None else None)
        print('> First Loop?',first_loop)
        if fast == None:
            if first_loop:
                return None
            else:
                return slow
                
        slow = slow.next
        first_loop = False
        
    print('Returned', slow)


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print('RESULT:',result.value if result != None else None)  # Output: 4


"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

