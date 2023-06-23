# 10. Write a program to find the minimum element in a queue.
# Expected Output:
# Queue elements are: 1 2 3 4 5
# Minimum value in the queue is: 1
# Remove 2 elements from the said queue:
# Queue elements are: 3 4 5
# Minimum value in the queue is: 3
# Insert 3 more elements:
# Queue elements are: 3 4 5 600 -427 519
# Minimum value in the queue is: -427


class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.rear == self.size - 1:
            print("Queue Overflow!")
        else:
            if self.front == -1:
                self.front += 1
            self.rear += 1
            self.queue.insert(self.rear, data)
            print("Enqueue data: {}".format(data))

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow!")
        else:
            popped = self.queue[self.front]
            self.queue.pop(self.front)
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.rear -= 1
            return popped

    def display(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            print("Queue elements are: ", end="")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

    def is_empty(self):
        if self.front == -1:
            return True
        else:
            return False

    def sum(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            sum = 0
            for i in range(self.front, self.rear + 1):
                sum += self.queue[i]
            return sum

    def max(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            max = self.queue[self.front]
            for i in range(self.front, self.rear + 1):
                if self.queue[i] > max:
                    max = self.queue[i]
            return max
        
    def min(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            min = self.queue[self.front]
            for i in range(self.front, self.rear + 1):
                if self.queue[i] < min:
                    min = self.queue[i]
            return min

    def average(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            sum = 0
            for i in range(self.front, self.rear + 1):
                sum += self.queue[i]
            return sum / (self.rear + 1)
        
    def search(self, data):
        if self.front == -1:
            print("Queue is empty!")
        else:
            for i in range(self.front, self.rear + 1):
                if self.queue[i] == data:
                    return i
            return -1
        
    def reverse(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[self.rear - i], end=" ")
            print()

    def sort(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            for i in range(self.front, self.rear + 1):
                for j in range(self.front, self.rear + 1):
                    if self.queue[i] < self.queue[j]:
                        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
            self.display()

    def size(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            return self.rear + 1
        
    def clear(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            self.queue.clear()
            self.front = -1
            self.rear = -1

queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.display()
print("Minimum value in the queue is: {}".format(queue.min()))
print("Remove 2 elements from the said queue:")
queue.dequeue()
queue.dequeue()
queue.display()
print("Minimum value in the queue is: {}".format(queue.min()))
print("Insert 3 more elements:")
queue.enqueue(600)
queue.enqueue(-427)
queue.enqueue(519)
queue.display()
print("Minimum value in the queue is: {}".format(queue.min()))

# Description:
# The program above finds the minimum element in a queue.
# The program first creates a queue with a size of 5.
# Then, the program enqueues 5 elements into the queue.
# The program then displays the queue and finds the minimum value in the queue.
# The program then dequeues 2 elements from the queue and displays the queue.
# The program then finds the minimum value in the queue.
# The program then enqueues 3 elements into the queue and displays the queue.
# The program then finds the minimum value in the queue.
# The program then displays the queue and finds the minimum value in the queue.