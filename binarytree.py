class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
def preOrder(root):
    if root:
        print(str(root.info)+" ", end="") #pr
        preOrder(root.left)
        preOrder(root.right)
tree = BinarySearchTree()


arr = [1,2,5,3,4,6]

for i in range(len(arr)):
    tree.create(arr[i])

preOrder(tree.root)
