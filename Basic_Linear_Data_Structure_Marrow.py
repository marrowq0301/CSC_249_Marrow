'''ChatGPT prompt:  Write a simple program that illustrates a basic linear 
data structure in action.  Please use iteration when writing this program.'''

# A simple queue implementation using a list
class Queue:
    def __init__(self):
        self.items = []  # Initialize an empty list to represent the queue

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)  # Remove the first item
        else:
            return "Queue is empty!"

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def display(self):
        """Display the items in the queue."""
        print("Queue:", self.items)


# Main program to demonstrate the Queue
queue = Queue()

# Enqueue some items
for i in range(1, 6):  # Add numbers 1 to 5 to the queue
    queue.enqueue(i)
    print(f"Enqueued: {i}")
    queue.display()

# Dequeue all items
while not queue.is_empty():
    removed_item = queue.dequeue()
    print(f"Dequeued: {removed_item}")
    queue.display()

'''ChatGPT Explanation of program:

1. Class Definition:

The Queue class uses a list to store items.
The enqueue method adds an item to the end of the list.
The dequeue method removes an item from the front of the list.
The is_empty method checks if the queue is empty.
The display method shows the current state of the queue.


2. Iteration:

A for loop is used to add items to the queue (enqueue).
A while loop is used to remove items until the queue is empty (dequeue).


3.  Output: This program simulates items entering and leaving the queue, showing 
the contents at each step.'''