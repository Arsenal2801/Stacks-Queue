# 1. Write a program to implement a stack using an array with push and pop
# operations.
# Expected Output:
# Elements in the stack are: 3 5 4 3 2 1

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Elements in the stack are:", end=" ")
        for item in self.stack:
            print(item, end=" ")
        print()


# Create a stack instance
stack = Stack()

# Push elements into the stack
stack.push(3)
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)

# Display the elements in the stack
stack.display()


# This program implements a stack data structure using an array. 
# It provides functionalities to perform the push and pop operations on the stack.

# Stack Class
# The Stack class represents the stack data structure. It contains the following methods:

# __init__(): This constructor method initializes a new instance of the Stack class. 
# It creates an empty array called stack to store the stack elements.

# push(item): The push() method accepts an item as a parameter and adds it to the top of the stack. 
# It appends the item to the stack array.

# pop(): The pop() method removes and returns the topmost item from the stack. 
# It uses the pop() function of the stack array to remove the last item and return it. If the stack is empty, it returns None.

# is_empty(): The is_empty() method checks if the stack is empty. 
# It returns True if the length of the stack array is 0, indicating an empty stack, and False otherwise.

# display(): The display() method prints all the elements in the stack. 
# It iterates over the stack array and prints each item separated by a space. The output is formatted as "Elements in the stack are: <items>".