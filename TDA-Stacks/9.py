# 9. Write a program to implement two stacks using a single array.
# Expected Output:
# 3 popped from stack 1
# 2 popped from stack 1
# 1 popped from stack 1
# 30 popped from stack 2
# 20 popped from stack 2
# 10 popped from stack 2

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
            for i in range(self.top2, self.size):
                print(self.stack[i], end=" ")
            print()
        else:
            print("Stack-2 is empty!")

if __name__ == "__main__":
    size = int(input("Enter the size of the stack: "))
    stack = Stack(size)
    while True:
        print("1. Push data to Stack-1")
        print("2. Push data to Stack-2")
        print("3. Pop data from Stack-1")
        print("4. Pop data from Stack-2")
        print("5. Display Stack-1")
        print("6. Display Stack-2")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter the data to be pushed to Stack-1: "))
            stack.push1(data)
        elif choice == 2:
            data = int(input("Enter the data to be pushed to Stack-2: "))
            stack.push2(data)
        elif choice == 3:
            popped = stack.pop1()
            if popped:
                print("{} popped from Stack-1".format(popped))
        elif choice == 4:
            popped = stack.pop2()
            if popped:
                print("{} popped from Stack-2".format(popped))
        elif choice == 5:
            stack.display1()
        elif choice == 6:
            stack.display2()
        elif choice == 7:
            break
        else:
            print("Invalid choice!")
        print()

# Description: This program implements two stacks using a single array.
# Push and pop operations are performed on both the stacks.
# Time Complexity: O(1)
# Space Complexity: O(n)

