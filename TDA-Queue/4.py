# 4. Write a program to implement a queue using an array. Create a function
# that removes an element from the queue. &gt;
# Expected Output:
# Initialize a queue!
# Check the queue is empty or not? Yes
# Insert some elements into the queue:
# 1 2 3
# Insert another element into the queue:
# 1 2 3 4
# Check the queue is empty or not? No

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

if __name__ == "__main__":
    print("Initialize a queue!")
    queue = Queue(5)
    print("Check the queue is empty or not? {}".format(queue.is_empty()))
    print("Insert some elements into the queue:")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()
    print("Insert another element into the queue:")
    queue.enqueue(4)
    queue.display()
    print("Check the queue is empty or not? {}".format(queue.is_empty()))

# Description:
# The program implements a queue using an array. The program creates a class
# named Queue. The class has a constructor that takes the size of the queue as
# an argument. The class has the following methods:
# enqueue() - inserts an element into the queue.
# dequeue() - removes an element from the queue.
# display() - displays the elements of the queue.
# is_empty() - checks whether the queue is empty or not.
# The program creates an object of the Queue class and calls the methods on the
# object.

