# 7. Write a program that checks whether a string of parentheses is balanced
# or not using stack. &gt;
# Expected Output:
# Input an expression in parentheses: {[])
# The expression is not balanced.
# -----------------------------------------
# Input an expression in parentheses: ((()))
# The expression is balanced.
# -----------------------------------------
# Input an expression in parentheses: ())
# The expression is not balanced.
# -----------------------------------------
# Input an text of parentheses: ([]){}[[(){}]{}]
# The expression is balanced.
# -----------------------------------------
# Input an expression in parentheses: [(]))
# The expression is not balanced.

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

    def is_balanced(self, string):
        for i in range(len(string)):
            if string[i] == "(" or string[i] == "[" or string[i] == "{":
                self.push(string[i])
            elif string[i] == ")" or string[i] == "]" or string[i] == "}":
                if self.is_empty():
                    return False
                elif not self.is_matching(self.pop(), string[i]):
                    return False
        if self.is_empty():
            return True
        else:
            return False

    def is_matching(self, popped, char):
        if popped == "(" and char == ")":
            return True
        elif popped == "[" and char == "]":
            return True
        elif popped == "{" and char == "}":
            return True
        else:
            return False
        
# Create a stack instance
stack = Stack()

# Accept a string from the user
string = input("Input an expression in parentheses: ")

# Check whether the string of parentheses is balanced or not using stack
if stack.is_balanced(string):
    print("The expression is balanced.")
else:
    print("The expression is not balanced.")

# Description: This program checks whether a string of parentheses is balanced
# or not using stack.
