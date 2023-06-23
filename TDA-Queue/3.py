# 3. Write a program to implement a queue using a linked list. Programs
# should contain functions for inserting elements into the queue, displaying
# queue elements, and checking whether the queue is empty or not. &gt;
# Expected Output:
# Initialize a queue!
# Check the queue is empty or not? Yes
# Insert some elements into the queue:
# 1 2 3
# Insert another element into the queue:
# 
# 1 2 3 4
# Check the queue is empty or not? No

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        # self.queue = []
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.front == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print("Enqueue data: {}".format(data))

    def dequeue(self):
        if self.front == None:
            print("Queue Underflow!")
        else:
            popped = self.front.data
            self.front = self.front.next
            return popped

    def display(self):
        if self.front == None:
            print("Queue is empty!")
        else:
            print("Queue elements are: ", end="")
            temp = self.front
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False
        
if __name__ == "__main__":
    print("Initialize a queue!")
    queue = Queue()
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
    print("Dequeue data: {}".format(queue.dequeue()))
    queue.display()
    print("Dequeue data: {}".format(queue.dequeue()))
    queue.display()
    print("Dequeue data: {}".format(queue.dequeue()))
    queue.display()
    print("Dequeue data: {}".format(queue.dequeue()))
    queue.display()
    print("Check the queue is empty or not? {}".format(queue.is_empty()))


# Description: This program implements a queue using a linked list. Programs
# should contain functions for inserting elements into the queue, displaying
# queue elements, and checking whether the queue is empty or not.
