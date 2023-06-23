# 9. Write a program to find the maximum element in a queue. &gt;
# Expected Output:
# Queue elements are: 1 2 3 4 5
# 
# Maximum value in the queue is: 5
# Remove 2 elements from the said queue:
# Queue elements are: 3 4 5
# Maximum value in the queue is: 5
# Insert 3 more elements:
# Queue elements are: 3 4 5 600 427 519
# Maximum value in the queue is: 600

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
print("Maximum value in the queue is: {}".format(queue.max()))
print("Remove 2 elements from the said queue:")
queue.dequeue()
queue.dequeue()
queue.display()
print("Maximum value in the queue is: {}".format(queue.max()))
print("Insert 3 more elements:")
queue.enqueue(600)
queue.enqueue(427)
queue.enqueue(519)
queue.display()
print("Maximum value in the queue is: {}".format(queue.max()))

# Description:
# In this program, we have a class Queue with methods enqueue, dequeue, display, is_empty, sum, max, min, average, search, reverse, sort, size, and clear.
# The enqueue method inserts an element into the queue.
# The dequeue method removes an element from the queue.
# The display method displays the elements of the queue.
# The is_empty method checks if the queue is empty.
# The sum method returns the sum of the elements of the queue.
# The max method returns the maximum element of the queue.
# The min method returns the minimum element of the queue.
# The average method returns the average of the elements of the queue.
# The search method returns the index of the element if it is found in the queue, otherwise it returns -1.
# The reverse method displays the elements of the queue in reverse order.
# The sort method sorts the elements of the queue in ascending order.
# The size method returns the size of the queue.
# The clear method clears the queue.
# In the main function, we create a queue object and insert elements into it.
# Then we display the elements of the queue and find the maximum element of the queue.
# Then we remove two elements from the queue and display the elements of the queue.
# Then we find the maximum element of the queue.
# Then we insert three more elements into the queue and display the elements of the queue.
# Then we find the maximum element of the queue.

        