# 4. Write a program that accepts a string and reverse it using a stack.
# Expected Output:
# Input a string: w3resource
# Reversed string using a stack is: ecruoser3w

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

    def reverse_string(self, string):
        for i in range(len(string)):
            self.push(string[i])
        reverse = ""
        for i in range(len(string)):
            reverse += self.pop()
        return reverse

# Create a stack instance
stack = Stack()

# Accept a string from the user
string = input("Input a string: ")

# Reverse the string using a stack
reverse = stack.reverse_string(string)

# Display the reversed string
print("Reversed string using a stack is: {}".format(reverse))

# Description: This program accepts a string and reverse it using a stack.