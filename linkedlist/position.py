class node:
    def __init__(self, values):
        self.data = values
        self.next = None

class solution:
    def __init__(self):
        self.head = None

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node

        else:
            p = 1
            temp = self.head

            while p < pos - 1 and temp is not None:
                temp = temp.next
                p += 1

            if temp is None:
                print("Invalid position")
                return

            new_node.next = temp.next
            temp.next = new_node

    def middle_node(self):
            slow=self.head
            fast=self.head    
    
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
    
            if slow:
                print("middle node:",slow.data)    
            else:
                print("list is empty")          

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None") 

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")




list1 = solution()

list1.insert(node(10), 1)
list1.insert(node(20), 2)
list1.insert(node(40), 2)

print("After inserting at position 2:")
list1.print()

list1.insert(node(54), 1)

print("After inserting at position 1:")
list1.print()


solution.middle()