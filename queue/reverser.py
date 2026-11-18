#reverse queue using stack
#stack using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    
    def print(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

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
        self.front = temp.next
        if self.front==None:
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

def reverse_queue(queue1):
    stack1 = Stack()
    while not queue1.is_empty():
        stack1.push(Node(queue1.dequeue()))
    stack1.print()    

que=Queue()
que.enqueue(Node(1))    
que.enqueue(Node(2))
que.enqueue(Node(3))
que.enqueue(Node(4))
que.print()
reverse_queue(que)