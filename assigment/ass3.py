class node:
    def __init__(self,pid,name,pr):
        self.pid=pid
        self.name=name
        self.priority=pr
        self.next=None
class PriorityQueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,new_node):

        if self.front==None:
            self.front=new_node
            return

        if self.front.priority>=new_node.priority:
            new_node.next=self.front
            self.front=new_node
            return

        else:
            temp=self.front

            while temp:
                if new_node.priority<=temp.priority:
                    break
                else:
                    prev=temp
                    temp=temp.next

            prev.next=new_node
            new_node.next=temp
    def dequeue(self):

        if self.front:
            temp=self.front
            print("Executed Process:",temp.pid,temp.name)
            self.front=self.front.next

        else:
            print("No process available")
    def display_next(self):

        if self.front:
            print("Next Process:")
            print("Process ID:",self.front.pid)
            print("Process Name:",self.front.name)
            print("Priority:",self.front.priority)

        else:
            print("No process available")
    def display_all(self):

        if self.front==None:
            print("No pending processes")
            return

        temp=self.front

        print(" Processes:")

        while temp:
            print(temp.pid,temp.name,temp.priority)
            temp=temp.next
    def count(self):

        temp=self.front
        c=0

        while temp:
            c=c+1
            temp=temp.next

        print("Total  Processes:",c)
pq=PriorityQueue()
pq.enqueue(node(101,"System Process",1))
pq.enqueue(node(102,"Interactive Process",2))
pq.enqueue(node(103,"Background Process",3))
pq.enqueue(node(104,"Low Priority Process",4))
pq.display_all()

print("\n highest priority dequeue")
pq.dequeue()

print("\n display next process")
pq.display_next()

print("\n display all")
pq.display_all()

print("\n total count")
pq.count()