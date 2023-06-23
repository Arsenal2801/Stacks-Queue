# 5. Write a program to implement two stacks in a single array and performs
# push and pop operations for both stacks.
# Expected Output:
# Elements in Stack-1 are: 50 40 30 10
# Elements in Stack-2 are: 70 60 50 40 20


class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top1 = -1
        self.top2 = self.size

    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.stack.insert(self.top1, data)
            print("Push data: {}".format(data))
        else:
            print("Stack Overflow!")

    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.stack.insert(self.top2, data)
            print("Push data: {}".format(data))
        else:
            print("Stack Overflow!")

    def pop1(self):
        if self.top1 >= 0:
            popped = self.stack[self.top1]
            self.stack.pop(self.top1)
            self.top1 -= 1
            return popped
        else:
            print("Stack Underflow!")

    def pop2(self):
        if self.top2 < self.size:
            popped = self.stack[self.top2]
            self.stack.pop(self.top2)
            self.top2 += 1
            return popped
        else:
            print("Stack Underflow!")

    def display1(self):
        if self.top1 >= 0:
            print("Elements in Stack-1 are: ", end="")
            for i in range(self.top1 + 1):
                print(self.stack[i], end=" ")
            print()
        else:
            print("Stack-1 is empty!")

    def display2(self):
        if self.top2 < self.size:
            print("Elements in Stack-2 are: ", end="")
            for i in range(self.size - 1, self.top2 - 1, -1):
                print(self.stack[i], end=" ")
            print()
        else:
            print("Stack-2 is empty!")

    def is_empty1(self):
        return True if self.top1 == -1 else False
    
    def is_empty2(self):
        return True if self.top2 == self.size else False
    
    def is_full(self):
        return True if self.top1 == self.top2 - 1 else False
    
    def size1(self):
        return self.top1 + 1
    
    def size2(self):
        return self.size - self.top2
    
    def peek1(self):
        return self.stack[self.top1]
    
    def peek2(self):
        return self.stack[self.top2]


# Create a stack instance
stack = Stack(10)
stack.push1(10)
stack.push1(30)
stack.push1(40)
stack.push1(50)

stack.push2(20)
stack.push2(40)
stack.push2(50)
stack.push2(60)
stack.push2(70)

stack.display1()
stack.display2()

print("Pop data from Stack-1: {}".format(stack.pop1()))
print("Pop data from Stack-2: {}".format(stack.pop2()))

stack.display1()
stack.display2()

print("Peek data from Stack-1: {}".format(stack.peek1()))
print("Peek data from Stack-2: {}".format(stack.peek2()))

print("Stack-1 size: {}".format(stack.size1()))
print("Stack-2 size: {}".format(stack.size2()))

print("Stack-1 is empty: {}".format(stack.is_empty1()))
print("Stack-2 is empty: {}".format(stack.is_empty2()))

print("Stack is full: {}".format(stack.is_full()))

# Description: This program implements two stacks in a single array and performs
# push and pop operations for both stacks.
