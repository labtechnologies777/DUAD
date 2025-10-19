# ---------------------------------------------------------------------------------- #
## STACK // LIFO // PUSH (insert to the top of the stack), POP (remove top most of the stack)

class Node:
  def __init__(self, data,next=None):
    self.main = data
    self.next = next

  def __repr__(self):
      return f"{self.main}"

class Stack:
    def __init__(self,top=None):
        self.top = top

    def push(self, value):
        new_node = value
        new_node.next = self.top  
        self.top = new_node
        
    def pop(self):
        popped_data = self.top
        self.top = self.top.next
        return popped_data
    

    def print_structure(self):
        current_node = self.top
        while current_node is not None:
            print(current_node)
            current_node = current_node.next        


    
node_1 = Node("A")
node_2 = Node("B")
node_3 = Node("C")
node_4 = Node("D")
stack = Stack()
stack.push(node_1)
stack.push(node_2)
stack.push(node_3)
stack.push(node_4)
print("---- PUSH-----")
stack.print_structure()
stack.pop()
stack.pop()
print("---- POP-----")
stack.print_structure()
