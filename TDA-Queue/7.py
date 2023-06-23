# 7. Write a program to calculate the sum of the elements in a queue.
# Expected Output:
# Queue elements are: 1 2 3 4 5
# Sum of the elements in the queue is: 15
# Remove 2 elements from the said queue:
# Queue elements are: 3 4 5
# Sum of the elements in the queue is: 12
# Insert 3 more elements:
# Queue elements are: 3 4 5 300 400 500
# Sum of the elements in the queue is: 1212

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

    def insert(self, data):
        if self.rear == self.size - 1:
            print("Queue Overflow!")
        else:
            self.rear += 1
            self.queue.insert(self.rear, data)
            print("Enqueue data: {}".format(data))

    def remove(self):
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
        
    def insert_three(self, data1, data2, data3):
        if self.rear == self.size - 1:
            print("Queue Overflow!")
        else:
            self.rear += 1
            self.queue.insert(self.rear, data1)
            self.rear += 1
            self.queue.insert(self.rear, data2)
            self.rear += 1
            self.queue.insert(self.rear, data3)
            print("Enqueue data: {}, {}, {}".format(data1, data2, data3))

queue = Queue(5)
queue.display()
queue.sum()
queue.dequeue()
queue.dequeue()
queue.display()
queue.sum()
queue.insert(300)
queue.insert(400)
queue.insert(500)
queue.display()
queue.sum()
queue.insert_three(600, 700, 800)
queue.display()
queue.sum()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.display()
queue.sum()

# Description:
# In this program, we are creating a class Queue with the required methods.
# The methods are:
# 1. enqueue(data): To insert data into the queue.
# 2. dequeue(): To remove data from the queue.
# 3. display(): To display the elements of the queue.
# 4. is_empty(): To check if the queue is empty.
# 5. sum(): To calculate the sum of the elements in the queue.
# 6. insert(data): To insert data into the queue.
# 7. remove(): To remove data from the queue.
# 8. insert_three(data1, data2, data3): To insert three data into the queue.
# We are creating an object queue of the class Queue and passing the size of the queue as an argument.
# We are displaying the elements of the queue and calculating the sum of the elements in the queue.
# We are removing two elements from the queue and displaying the elements of the queue and calculating the sum of the elements in the queue.
# We are inserting three elements into the queue and displaying the elements of the queue and calculating the sum of the elements in the queue.
# We are removing all the elements from the queue and displaying the elements of the queue and calculating the sum of the elements in the queue.

