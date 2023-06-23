# 6. Write a program to sort a given stack using another stack.
# Expected Output:
# Original stack: 1 5 5 2 3 8
# Sorted stack: 1 2 3 5 5 8


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
    
    def sort(self):
        temp = self.root
        while temp:
            temp2 = temp.next
            while temp2:
                if temp.data > temp2.data:
                    temp.data, temp2.data = temp2.data, temp.data
                temp2 = temp2.next
            temp = temp.next
        return self.root
    
# Create a stack instance
stack = Stack()
stack.push(1)
stack.push(5)
stack.push(5)
stack.push(2)
stack.push(3)
stack.push(8)

stack.display()
stack.sort()
stack.display()

# Description: This program implements a stack using a singly linked list.