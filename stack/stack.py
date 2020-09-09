"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop()

#-------------------------single_linked_lists-----------------------------

import sys

sys.path.append("../single_linked_list")
from single_linked_lists import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length

    def push(self, value):
        return self.storage.add_to_tail(value)
#make sure we are adding and removing from the same side (head or tail)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.remove_from_tail()



#------------------------------------------------Linked List--------
import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList



class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.add_to_head(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.remove_from_head()