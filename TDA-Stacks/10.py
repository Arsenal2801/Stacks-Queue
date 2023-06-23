# 10. Write a program that reverses a stack using only stack operations push
# and pop. &gt;
# Expected Output:
# Original Stack: 10 20 30 40 50
# Reversed Stack: 50 40 30 20 10

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, data):
        self.top += 1
        self.stack.insert(self.top, data)
        print("Push data: {}".format(data))

    def pop(self):
        if self.top >= 0:
            popped = self.stack[self.top]
            self.stack.pop(self.top)
            self.top -= 1
            return popped
        else:
            print("Stack Underflow!")

    def display(self):
        if self.top >= 0:
            print("Elements in Stack are: ", end="")
            for i in range(self.top + 1):
                print(self.stack[i], end=" ")
            print()
        else:
            print("Stack is empty!")

    def reverse(self):
        if self.top >= 0:
            temp = self.stack[self.top]
            self.stack.pop(self.top)
            self.top -= 1
            self.reverse()
            self.insert_at_bottom(temp)
        else:
            return

    def insert_at_bottom(self, data):
        if self.top == -1:
            self.push(data)
        else:
            temp = self.stack[self.top]
            self.stack.pop(self.top)
            self.top -= 1
            self.insert_at_bottom(data)
            self.push(temp)


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    print("Original Stack: ", end="")
    stack.display()

    stack.reverse()

    print("Reversed Stack: ", end="")
    stack.display()

# Description: This program reverses a stack using only stack operations push
# and pop.

