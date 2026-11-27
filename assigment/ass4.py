class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # 1. Insert node
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    # 2. Display scores in ascending order
    def inorder(self, rt):
        if rt is None:
            return

        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    # 3. Find minimum and maximum scores
    def findminmax(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root

        while temp.left:
            temp = temp.left

        print("\nLowest Score:", temp.data)

        temp = self.root

        while temp.right:
            temp = temp.right

        print("Highest Score:", temp.data)

    # 4. Count students scoring above 50
    def count_above_50(self, rt):
        if rt is None:
            return 0

        count = 0

        if rt.data > 50:
            count = 1

        return (count +
                self.count_above_50(rt.left) +
                self.count_above_50(rt.right))

    # 5. Search particular score
    def search(self, key):
        temp = self.root

        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        return False

    # 6. Find average of all scores
    def total(self, rt):
        if rt is None:
            return 0

        return (rt.data +
                self.total(rt.left) +
                self.total(rt.right))

    def count_nodes(self, rt):
        if rt is None:
            return 0

        return (1 +
                self.count_nodes(rt.left) +
                self.count_nodes(rt.right))


# Driver Code

b1 = BST()

scores = [45, 78, 32, 89, 56, 92,
          67, 34, 85, 73, 61, 98]

# Insert scores into BST
for val in scores:
    b1.insert(Node(val))

# Display ascending order
print("Scores in Ascending Order:")
b1.inorder(b1.root)

# Find lowest and highest
b1.findminmax()

# Count students above 50
print("\nStudents scoring above 50:",
      b1.count_above_50(b1.root))

# Search particular score
key = 85

if b1.search(key):
    print("Score", key, "Found")
else:
    print("Score", key, "Not Found")

# Calculate average
total = b1.total(b1.root)
count = b1.count_nodes(b1.root)

average = total / count

print("Total Marks:", total)
print("Average Score:", round(average, 2))