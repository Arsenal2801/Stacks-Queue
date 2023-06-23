# 5. Write a program to count the number of elements in a queue. &gt;
# Expected Output:
# Initialize a queue!
# Check the queue is empty or not? Yes
# Number of elements in queue: 0
# Insert some elements into the queue:
# Queue elements are: 1 2 3
# Number of elements in queue: 3
# Delete two elements from the said queue:
# Queue elements are: 3
# Number of elements in queue: 1
# Insert another element into the queue:
# Queue elements are: 3 4
# Number of elements in the queue: 2

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

    def count(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            print("Number of elements in queue: {}".format(self.rear + 1))

if __name__ == "__main__":
    print("Initialize a queue!")
    queue = Queue(5)
    print("Check the queue is empty or not? {}".format(queue.is_empty()))
    print("Insert some elements into the queue:")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()
    queue.count()
    print("Delete two elements from the said queue:")
    queue.dequeue()
    queue.dequeue()
    queue.display()
    queue.count()
    print("Insert another element into the queue:")
    queue.enqueue(4)
    queue.display()
    queue.count()

# Description: Program to count the number of elements in a queue.
