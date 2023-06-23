# 2. Write a program to implement a stack using a singly linked list.
# Expected Output:
# Push data 1
# Push data 2
# Push data 3
# Push data 4
# Pop data: 4
# Pop data: 3
# Pop data: 2
# Pop data: 1
# Check a stack is empty or not?
# Stack is empty!

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    # Constructor to initialize the root of linked list
    def __init__(self):
        self.root = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node
        print("Push data: {}".format(data))

    def pop(self):
        if self.root is None:
            return None
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def is_empty(self):
        return True if self.root is None else False

    def display(self):
        temp = self.root
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Create a stack instance
stack = Stack()

# Push elements into the stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

# Display the elements in the stack
stack.display()

# Pop elements from the stack
print("Pop data: {}".format(stack.pop()))

# Display the elements in the stack
stack.display()

# Description: This program implements a stack data structure using a singly linked list.
# Stack Class
# The Stack class represents the stack data structure. It contains the following methods:

# __init__(): This constructor method initializes a new instance of the Stack class.
# It creates an empty root node to store the stack elements.

# push(item): The push() method accepts an item as a parameter and adds it to the top of the stack.

# pop(): The pop() method removes and returns the topmost item from the stack.

# is_empty(): The is_empty() method checks if the stack is empty. It returns True if the root node is None, indicating an empty stack, and False otherwise.

# display(): The display() method prints the elements in the stack. It traverses the stack and prints the data of each node.