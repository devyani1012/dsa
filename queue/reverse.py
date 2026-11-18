
# Reverse Queue Using Stack
# Stack and Queue using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack using Linked List
class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        temp = self.top
        self.top = self.top.next
        return temp.data

    def is_empty(self):
        return self.top is None

    def print(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Queue using Linked List
class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return temp.data

    def is_empty(self):
        return self.front is None

    def print(self):
        current = self.front

        while current:
            print(current.data, end=" ")
            current = current.next

        print()


# Reverse Queue using Stack
def reverse_queue(queue1):

    stack1 = Stack()

    # Move elements from Queue to Stack
    while not queue1.is_empty():
        stack1.push(queue1.dequeue())

    # Move elements from Stack back to Queue
    while not stack1.is_empty():
        queue1.enqueue(stack1.pop())


# Main Program
que = Queue()

que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.print()

reverse_queue(que)
que.print()
