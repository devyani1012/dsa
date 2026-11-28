class node:
    def __init__ (self,data):
        self.prev=None
        self.data=data
        self.next=None

class dll:

    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=node(data)


        if self.head is not None:
            new_node.next=self.head
            new_node.prev=new_node
        self.head=new_node    

    def display(self):
        temp=self.head

        while temp:
            print(temp.data ,end="  ")
            temp=temp.next

        print("none")    

dl=dll()
dl.insert(10)  
dl.insert(20)      
dl.display()

