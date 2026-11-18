
# Node class
class Node:
    def __init__(self, data):
        self.data = data  # store data
        self.next = None  # store reference to next node
# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # initially empty list
    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:   # if list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:  # traverse to the end
            last = last.next
        last.next = new_node
    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    # Function to insert after a given position
    def insert_after(self, prev_data, new_data):
        temp = self.head
        while temp:
            if temp.data == prev_data:
                break
            temp = temp.next
        if temp is None:
            print(f"Node with data {prev_data} not found.")
            return
        new_node = Node(new_data)
        new_node.next = temp.next
        temp.next = new_node      
# Print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll. print_list()
l = LinkedList()
ll.prepend(100)
ll = LinkedList()
ll.insert_after(20, 25) 
           