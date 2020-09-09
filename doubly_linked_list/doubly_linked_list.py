"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    def delete(self):
        if self.prev:
            self.prev.next = self.next        
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        pass
        new_node = ListNode(value, None, None)
        self.length += 1

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
            self.max = value
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
        if self.head:
            value = self.head.value
            print("remove from tail", value, "length", self.length)
            self.delete(self.head)
            return value
        else:
            return
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
        new_node = ListNode(value)
        self.length += 1
        print("add to tail", value, "length", self.length)

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            self.max = value
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
        value = self.tail.value
        self.delete(self.tail)
        return value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

        if not self.head:
            print("Cannot delete from an empty list")
            return

        self.length -= 1

        if self.head == self.tail:
            self.head = None
            self.tail = None

        if node == self.head:
            self.head = node.next
            self.head.prev = None

        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None

        node.delete()


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass
        if self.head == self.tail:
            return self.head.value

        max = 0
        curr_node = self.head

        while True:

            if curr_node.value > max:
                max = curr_node.value

            if curr_node.next == None:
                break
            else:
                curr_node = curr_node.next

        return max