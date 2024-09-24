class Node:
    def __init__(self, value):
        self.value: any = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self, value):
        new_node: Node = Node(value)
        self.head: Node = new_node # set initial node as head
        self.tail: Node = new_node # set initial node as tail
        self.length: int = 1 # track length of linkedlist
        
    def print_list(self):
        temp = self.head # get fist element in linked list
        print('PRINTING NODES...')
        while temp is not None: # loop through until there is no next node
            print(temp.value)
            temp = temp.next # set the next node to temp per iteration
        
    def append(self, value):
        new_node = Node(value) # create new node
        if self.length == 0: # Handle empty linked list. If empty, set new node as initial node in list
            self.head = new_node # set initial node as head
            self.tail = new_node # set initial node as tail
            return True # just returns something
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
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
            
        temp: Node = self.head # get fist element in linked list
        prev_node: Node | None = None
        while temp is not None: # loop through until tail is reached
            if temp.next == None: # if True, then next node is the tail
                self.tail = prev_node # set previous node as tail node
                self.tail.next = None # set next node to None
                self.length -= 1
                if self.length == 0: # reset head and tail nodes if no nodes remain
                    self.head = None
                    self.tail = None
                return temp # return popped node
            prev_node = temp
            temp = temp.next # set the next node to temp per iteration
                
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node # set initial node as head
            self.tail = new_node # set initial node as tail
            return True # just returns something
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
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        temp = self.head # place current head node to temp
        self.head = temp.next # replace current head with temp next node
        self.length -= 1 # decrement length of ll
        if self.length == 0: # reset head and tail nodes if no nodes remain
            self.head = None
            self.tail = None
        return temp
    
    def get_value(self, index):
        if self.length == 0:
            return None
        
        temp = self.head
        if index < 0 or index > self.length-1: # handle index out of bounds
            return None
        
        for _ in range(index):
            temp = temp.next # set the next node to temp per iteration
        return temp # return node at index
    
    def set_value()
                
        
ll = LinkedList(1)
ll.append(2)
ll.append(3)
# ll.print_list()
print(ll.get_value(3))
        
    
    