# ---------------------------------------------------------------------------------- #
## STACK // LIFO // PUSH (insert to the top of the stack), POP (remove top most of the stack)

# class Node:
#   def __init__(self, data,next=None):
#     self.main = data
#     self.next = next

#   def __repr__(self):
#       return f"{self.main}"

# class Stack:
#     def __init__(self,top=None):
#         self.top = top

#     def push(self, value):
#         new_node = value
#         new_node.next = self.top  # New node points to the current top
#         self.top = new_node      # New node becomes the new top
#         # print(f"TOP: {self.top}")
#         # print(f"NEXT:{new_node.next}")
        
#     def pop(self):
#         popped_data = self.top
#         self.top = self.top.next  # Move top to the next node
#         # print(f"POP: {popped_data}")
#         return popped_data
    

#     def print_structure(self):
#         current_node = self.top
#         while current_node is not None:
#             print(current_node)
#             current_node = current_node.next        


    
# node_1 = Node("A")
# node_2 = Node("B")
# node_3 = Node("C")
# node_4 = Node("D")
# stack = Stack()
# stack.push(node_1)
# stack.push(node_2)
# stack.push(node_3)
# stack.push(node_4)
# print("---- PUSH-----")
# stack.print_structure()
# stack.pop()
# stack.pop()
# print("---- POP-----")
# stack.print_structure()


# ---------------------------------------------------------------------------------- #
## Double Ended Queue // push_left, push_right (para agregar nodos al inicio y al final) // pop_left y pop_right (para quitar nodos al inicio y al final).


# class Node:
#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next

#     def __repr__(self):
#         return f"{self.data}"

# class Deque:
#     def __init__(self, front=None,rear=None):
#         self.front = front
#         self.rear = rear

#     def append_front(self, value):
#         new_node = value
#         if self.front is None:
#             self.front = self.rear = new_node
#         else:
#             new_node.next = self.front
#             self.front.prev = new_node
#             self.front = new_node

#     def append_rear(self, value):
#         new_node = value
#         if self.rear is None:
#             self.front = self.rear = new_node
#         else:
#             new_node.prev = self.rear
#             self.rear.next = new_node
#             self.rear = new_node

#     def pop_front(self):
#         if self.front is None:
#             print("Deque is empty! Cannot pop from front.")
#             return
#         else:
#             popped_data = self.front.data
#             self.front = self.front.next
#             if self.front is not None:
#                 self.front.prev = None
#             else:
#                 self.rear = None
#             return popped_data

#     def pop_rear(self):
#         if self.rear is None:
#             print("Deque is empty! Cannot pop from rear.")
#             return
#         else:
#             popped_data = self.rear.data
#             self.rear = self.rear.prev
#             if self.rear is not None:
#                 self.rear.next = None
#             else:
#                 self.front = None
#             return popped_data

#     def print_structure(self):
#         if self.front is None:
#             print("Deque is empty.")
#             return
#         else:
#             current_node = self.front
#             while current_node:
#                 print(current_node.data)
#                 current_node = current_node.next


# node_1 = Node("A")
# node_2 = Node("B")
# node_3 = Node("C")
# node_4 = Node("D")
# node_5 = Node("E")
# deque = Deque()
# print("---- APPEND REAR ----")
# deque.append_rear(node_1)
# deque.append_rear(node_2)
# deque.print_structure()
# print("---- APPEND FRONT ----")
# deque.append_front(node_3)
# deque.print_structure()
# print("---- POP FRONT ----")
# deque.pop_front()
# deque.print_structure()
# print("---- POP REAR ----")
# deque.pop_rear()
# deque.print_structure()


# ---------------------------------------------------------------------------------- #
## Binary Tree. 

# class Node:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right

# class Binary_Tree():
#     def __init__(self,root=None):
#         self.root = root

#     def create_tree(self, root,left,right,left_left, right_right):
#         self.root = root
#         self.root.left = left
#         self.root.right = right
#         self.root.left.left = left_left
#         self.root.left.right = right_right

#     def print_structure(self):
#         print(f"Root:", {self.root.data})
#         print(f"Left child of root:", {self.root.left.data})
#         print(f"Right child of root:", {self.root.right.data})
#         print(f"Left child of left node:", {self.root.left.left.data})
#         print(f"Right child of left node:", {self.root.left.right.data})


# node_1 = Node("A")
# node_2 = Node("B")
# node_3 = Node("C")
# node_4 = Node("D")
# node_5 = Node("E")
# binary_tree = Binary_Tree()
# binary_tree.create_tree(node_1,node_2,node_3, node_4, node_5)
# binary_tree.print_structure()



