# 8. Write a program to compute the average value of the elements in a
# queue. &gt;
# Expected Output:
# Queue elements are: 1 2 3 4 5
# Average of the elements in the queue is: 3.000000
# Remove 2 elements from the said queue:
# Queue elements are: 3 4 5
# Average of the elements in the queue is: 4.000000
# Insert 3 more elements:
# Queue elements are: 3 4 5 300 427 519
# Average of the elements in the queue is: 209.666672

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
            print("Sum of the elements in the queue is: {}".format(sum))

    def average(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            sum = 0
            for i in range(self.front, self.rear + 1):
                sum += self.queue[i]
            print("Average of the elements in the queue is: {}".format(sum / (self.rear + 1)))

if __name__ == "__main__":
    queue = Queue(5)
    queue.display()
    queue.sum()
    queue.average()
    print("Enqueue 5 elements:")
    for i in range(5):
        queue.enqueue(i + 1)
    queue.display()
    queue.sum()
    queue.average()
    print("Dequeue 2 elements:")
    for i in range(2):
        queue.dequeue()
    queue.display()
    queue.sum()
    queue.average()
    print("Enqueue 3 elements:")
    for i in range(3):
        queue.enqueue(i + 300)
    queue.display()
    queue.sum()
    queue.average()

# Description: Program to compute the average value of the elements in a queue.