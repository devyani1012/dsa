class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class doublylinkedlist:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert(self, data):
        new_node = Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    # Insert at end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    # Display
    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end="   ")
            temp = temp.next

        print("None")


DLL = doublylinkedlist()

DLL.insert(10)
DLL.insert(20)
DLL.insert(30)

print("Insertion at beginning:")
DLL.traverse()

DLL.append(40)
DLL.append(50)

print("Insertion at end:")
DLL.traverse()