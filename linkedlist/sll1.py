class node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Insertion at the beginning
def insert_begin(head):
    new_node = node(5)
    new_node.next = head
    head = new_node
    return head


# Insertion at the end
def insert_end(head):
    new_node = node(60)
    current = head

    while current.next is not None:
        current = current.next

    current.next = new_node
    return head


# Insertion at a specific position
def specific_position(head, pos):
    new_node = node(25)
    current = head

    for i in range(pos - 1):
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head

# delete node at begning
def deletation_node(head):
    head=head.next
    return head

# delation at end 
def delation_at_end(head):
    current=head
    while current.next.next is not None:
        current=current.next

    current.next=None
    return head    

# deletion at specific pos
def delete_position(head, pos):
    current = head

    for i in range(pos - 1):
        current = current.next

    current.next = current.next.next

    return head


# Display linked list
def display(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Creating nodes manually
n1 = node(10)
n2 = node(20)
n3 = node(30)
n4 = node(40)
n5 = node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = n1

# Calling insertion functions
head = insert_begin(head)
head = insert_end(head)
head = specific_position(head, 2)
head=deletation_node(head)
head=delation_at_end(head)
head=delete_position(head,3)
display(head)