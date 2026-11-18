class Queue:

    def __init__(self):
        self.queue = []

    # 1. Enqueue
    def enqueue(self, item):
        self.queue.append(item)
        print(item, "inserted into queue")

    # 2. Dequeue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Deleted:", self.queue.pop(0))

    # 3. Display
    def display(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue:", self.queue)

    # 4. Reverse Queue using Stack
    def reverse_queue(self):
        stack = []

        while self.queue:
            stack.append(self.queue.pop(0))

        while stack:
            self.queue.append(stack.pop())

        print("Reversed Queue:", self.queue)

    # 5. Merge two Queues
    def merge_queue(self, q2):
        merged = self.queue + q2.queue
        print("Merged Queue:", merged)

    # 6. Check Identical Queues
    def identical(self, q2):
        if self.queue == q2.queue:
            print("Queues are Identical")
        else:
            print("Queues are Not Identical")


# Main Program

q1 = Queue()
q2 = Queue()

# First Queue
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

# Second Queue
q2.enqueue(40)
q2.enqueue(50)

print("\nFirst Queue:")
q1.display()

print("\nDequeue:")
q1.dequeue()
q1.display()

print("\nReverse Queue:")
q1.reverse_queue()

print("\nMerge Queues:")
q1.merge_queue(q2)

print("\nCheck Identical:")
q1.identical(q2)