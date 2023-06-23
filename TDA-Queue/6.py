# 6. Write a program to reverse the elements of a queue. &gt;
# Expected Output:
# Queue elements are:
# 
# 1 2 3 4 5
# Reverse Queue, elements are:
# 5 4 3 2 1
# Add two elements to the said queue:
# Queue elements are:
# 5 4 3 2 1 100 200
# Reverse Queue, elements are:
# 200 100 1 2 3 4 5

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

    def reverse(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            print("Queue elements are: ", end="")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
            print("Reverse Queue, elements are: ", end="")
            for i in range(self.rear, self.front - 1, -1):
                print(self.queue[i], end=" ")
            print()

    def count(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            print("Number of elements in queue: {}".format(self.rear - self.front + 1))


if __name__ == "__main__":
    print("Initialize a queue!")
    q = Queue(5)
    print("Check the queue is empty or not? {}".format(q.is_empty()))
    print("Insert some elements into the queue:")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    q.count()
    print("Delete two elements from the said queue:")
    q.dequeue()
    q.dequeue()
    q.display()
    q.count()
    print("Insert another element into the queue:")
    q.enqueue(4)
    q.display()
    q.count()
    print("Reverse the elements of the queue:")
    q.reverse()
    print("Add two elements to the said queue:")
    q.enqueue(100)
    q.enqueue(200)
    q.display()
    q.count()
    print("Reverse the elements of the queue:")
    q.reverse()

# Description:
# The reverse() method reverses the elements of the queue.
# The count() method returns the number of elements in the queue.
#