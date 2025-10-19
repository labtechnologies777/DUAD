## Binary Tree. 

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Binary_Tree():
    def __init__(self,root=None):
        self.root = root

    def create_tree(self, root,left,right,left_left, right_right):
        self.root = root
        self.root.left = left
        self.root.right = right
        self.root.left.left = left_left
        self.root.left.right = right_right

    def print_structure(self):
        print(f"Root:", {self.root.data})
        print(f"Left child of root:", {self.root.left.data})
        print(f"Right child of root:", {self.root.right.data})
        print(f"Left child of left node:", {self.root.left.left.data})
        print(f"Right child of left node:", {self.root.left.right.data})


node_1 = Node("A")
node_2 = Node("B")
node_3 = Node("C")
node_4 = Node("D")
node_5 = Node("E")
binary_tree = Binary_Tree()
binary_tree.create_tree(node_1,node_2,node_3, node_4, node_5)
binary_tree.print_structure()