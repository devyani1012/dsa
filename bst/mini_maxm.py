class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class scorces:
    def __init__(self):
        self.root=None

    def insert(self,new_node):
        if self.root is None:
            self.root=new_node
            print(new_node.data,end="  ")
            return
        temp=self.root
        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left=new_node
                    print(new_node.data,end=" ")

                    return
                else:

                    temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    print(new_node.data,end="  ")

                    return
                else:
                    temp=temp.right

    def minmax(self):
        temp=self.root
        while temp.left:
            temp=temp.left
        print("\n min",temp.data)    
        temp=self.root
        if temp.right:
            temp=temp.right
        print("\n max",temp.data)                    

bst=scorces()
#scores = [60, 40, 80, 25, 50, 70, 90, 30, 45, 65, 85, 95]
bst.insert(Node(60))
bst.insert(Node(25))
bst.insert(Node(50))
bst.insert(Node(70))
bst.insert(Node(30))
bst.insert(Node(60))

bst.minmax()



