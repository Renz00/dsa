class Node:
    def __init__(self, value):
        self.value: any = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self, value):
        new_node: Node = Node(value) # create new node
        self.head, self.tail = new_node, new_node # set initial node as head and tail
        self.length: int = 1 # track length of linkedlist
        
    def print_list(self):
        temp = self.head # get fist element in linked list
        print('PRINTING NODES...')
        while temp is not None: # loop through until there is no next node
            print(temp.value)
            temp = temp.next # set the next node to temp per iteration
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0: # Handle empty linked list. If empty, set new node as initial node in list
            self.head, self.tail = new_node, new_node # set initial node as head and tail
        else:
            self.tail.next = new_node # point tail node to the new node
            self.tail = new_node # replace tail node with new node
        self.length += 1 # increment linked list length
        return True # just returns something
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1: # reset head and tail nodes if only 1 node exists
            temp: Node = self.head # get fist element in linked list
            self.head, self.tail = None, None
            self.length -= 1
            return temp
        temp: Node = self.head # get fist element in linked list
        prev_node: Node | None = None
        while temp != None: # loop through until tail is reached
            if temp.next == None: # if True, then next node is the tail
                self.tail = prev_node # set previous node as tail node
                self.tail.next = None # set next node to None
                self.length -= 1
                if self.length == 0: # reset head and tail nodes if no nodes remain
                    self.head, self.tail = None, None
                return temp # return popped node
            prev_node = temp
            temp = temp.next # set the next node to temp per iteration
                
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head, self.tail = new_node, new_node # set initial node as head and tail
        else:
            new_node.next = self.head # point new node to current head
            self.head = new_node # replace current head with new node
        self.length += 1 # increment linked list length
        return True # just returns something
        
    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1: # reset head and tail nodes if only 1 node exists
            temp: Node = self.tail # get last element in linked list
            self.head, self.tail = None, None
            self.length -= 1
            return temp
        temp = self.head # place current head node to temp
        self.head = temp.next # replace current head with temp next node
        self.length -= 1 # decrement length of ll
        if self.length == 0: # reset head and tail nodes if no nodes remain
            self.head, self.tail = None, None
        return temp
    
    def get(self, index):
        if self.length == 0:
            return None
        if index < 0 or index > self.length-1: # handle index out of bounds
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next # set the next node to temp per iteration
        return temp # return node at index
    
    def set_value(self, index, new_value):
        temp: Node | None = self.get(index)
        if temp == None: # if temp is none, no node at given index
            return False
        temp.value = new_value
        return True
    
    def insert(self, index, new_value):
        if index == 0: # if index is head, use prepend
            return self.prepend(new_value)
        if index == self.length-1: # if index is tail, use append
            return self.append(new_value)
        prev_node: Node | None = self.get(index-1) # prev_node will be the previous node of the given index
        if prev_node == None:
            return False
        new_node = Node(new_value) # create new node with new value
        new_node.next = prev_node.next # pass temp next pointer to new node pointer
        prev_node.next = new_node # temp points to new node
        self.length += 1
        return True
    
    def remove(self, index):
        if index == 0: # if index is head, use pop_first
            return self.pop_first()
        if index == self.length-1: # if index is tail, use pop
            return self.pop()
        prev_node: Node | None = self.get(index-1) # get the previous node, you can still access node at given index using temp.next
        if prev_node == None:
            return None
        # (1) -> (2) -> (3)
        curr_node = prev_node.next # get node at given index using the prev node pointer
        prev_node.next = curr_node.next
        curr_node.next = None # remove pointer
        # (1) -> (3)
        self.length -= 1
        return curr_node
    
    def reverse(self):
        if self.length <= 1:
            return False
        # swapping head and tail nodes
        curr_node = self.head # pass head node to temp
        self.head = self.tail
        self.tail = curr_node
        prev_node: Node | None = None # track the previous node
        while curr_node != None: # loop starting from head node
            # switching pointers
            next_node = curr_node.next # store the next node
            curr_node.next = prev_node # set next node as previous node
            # moving nodes
            prev_node = curr_node # replace the previous node with the current node
            curr_node = next_node # replace current node with the next node
        return True
            
            
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.print_list()
print(ll.remove(5))