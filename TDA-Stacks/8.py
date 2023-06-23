# 8. Write a program to find the next greater element for each element in an
# array using a stack. Return -1 if there is no next-larger element
# Expected Output:
# Elements in the array are: 1 2 3 4 5 6
# The next larger elements are:
# 1 --> 2
# 2 --> 3
# 3 --> 4
# 
# 4 --> 5
# 5 --> 6
# 6 --> -1
# Elements in the array are: 6 5 4 3 2 1 0
# The next larger elements are:
# 0 --> -1
# 1 --> -1
# 2 --> -1
# 3 --> -1
# 4 --> -1
# 5 --> -1
# 6 --> -1
# Elements in the array are: 3 7 5 9 3 2 4 1 4
# The next larger elements are:
# 3 --> 7
# 5 --> 9
# 7 --> 9
# 2 --> 4
# 3 --> 4
# 1 --> 4
# 4 --> -1
# 9 --> -1
# --------------------------------


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
    
    def next_larger(self, arr):
        for i in range(len(arr)):
            next = -1
            for j in range(i+1, len(arr)):
                if arr[i] < arr[j]:
                    next = arr[j]
                    break
            print("{} --> {}".format(arr[i], next))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



if __name__ == "__main__":
    s = Stack()
    arr = [1, 2, 3, 4, 5, 6]
    print("Elements in the array are: ", end="")
    for i in arr:
        print(i, end=" ")
    print()
    print("The next larger elements are: ")
    s.next_larger(arr)
    print("Elements in the array are: ", end="")
    arr = [6, 5, 4, 3, 2, 1, 0]
    for i in arr:
        print(i, end=" ")
    print()
    print("The next larger elements are: ")
    s.next_larger(arr)
    print("Elements in the array are: ", end="")
    arr = [3, 7, 5, 9, 3, 2, 4, 1, 4]
    for i in arr:
        print(i, end=" ")
    print()
    print("The next larger elements are: ")
    s.next_larger(arr)

# --------------------------------

# Description: This program implements a stack using a linked list
#
# Time Complexity: O(1) for push, pop, is_empty, is_full, size
#                  O(n^2) for sort
#                  O(n^2) for next_larger

# --------------------------------