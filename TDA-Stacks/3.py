# 3. Write a program to check a stack is full or not using an array with push
# and pop operations.
# Expected Output:
# Stack size: 3
# Original Stack: 1 2 3
# Push another value and check if the stack is full or not!
# Stack is full!
# Stack size: 3
# Original Stack: 10 20
# Check the said stack is full or not!
# Stack is not full!

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

    def is_full(self):
        return True if self.root is None else False
    
    def size(self):
        temp = self.root
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    

# Create a stack instance
stack = Stack()

# Push elements into the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Diplays the size of the stack
print("Stack size:", stack.size())

# Display the elements in the stack
stack.display()

# Push another element into the stack
stack.push(4)

# Diplays the size of the stack
print("Stack size:", stack.size())

# Display the elements in the stack
stack.display()

# Pop elements from the stack
print("Pop data:", stack.pop())

# Pop elements from the stack
print("Pop data:", stack.pop())

# Pop elements from the stack
print("Pop data:", stack.pop())

# Pop elements from the stack
print("Pop data:", stack.pop())

# Diplays the size of the stack
print("Stack size:", stack.size())

# Display the elements in the stack
stack.display()

# Check a stack is empty or not?
if stack.is_empty():
    print("Stack is empty!")
else:
    print("Stack is not empty!")
  

#  Description: This program implements a stack using a singly linked list.
#  The program also checks if the stack is full or not.
#  Date: 1/28/2021
    