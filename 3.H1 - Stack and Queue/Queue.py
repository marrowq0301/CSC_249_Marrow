from Node import Node
from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.list = LinkedList()
        
    def enqueue(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)
        
        # Insert as list tail (end of queue)
        self.list.append(new_node)
    
    def dequeue(self):
        # Copy data from list's head node (queue's front node)
        dequeued_item = self.list.head.data
        
        # Remove list head
        self.list.remove_after(None)
        
        # Return the dequeued item
        return dequeued_item
