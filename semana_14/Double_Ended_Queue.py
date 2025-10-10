## Double Ended Queue // push_left, push_right (para agregar nodos al inicio y al final) // pop_left y pop_right (para quitar nodos al inicio y al final).


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"{self.data}"

class Deque:
    def __init__(self, front=None,rear=None):
        self.front = front
        self.rear = rear

    def append_front(self, value):
        new_node = value
        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def append_rear(self, value):
        new_node = value
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def pop_front(self):
        if self.front is None:
            print("Deque is empty! Cannot pop from front.")
            return
        else:
            popped_data = self.front.data
            self.front = self.front.next
            if self.front is not None:
                self.front.prev = None
            else:
                self.rear = None
            return popped_data

    def pop_rear(self):
        if self.rear is None:
            print("Deque is empty! Cannot pop from rear.")
            return
        else:
            popped_data = self.rear.data
            self.rear = self.rear.prev
            if self.rear is not None:
                self.rear.next = None
            else:
                self.front = None
            return popped_data

    def print_structure(self):
        if self.front is None:
            print("Deque is empty.")
            return
        else:
            current_node = self.front
            while current_node:
                print(current_node.data)
                current_node = current_node.next


node_1 = Node("A")
node_2 = Node("B")
node_3 = Node("C")
node_4 = Node("D")
node_5 = Node("E")
deque = Deque()
print("---- APPEND REAR ----")
deque.append_rear(node_1)
deque.append_rear(node_2)
deque.print_structure()
print("---- APPEND FRONT ----")
deque.append_front(node_3)
deque.print_structure()
print("---- POP FRONT ----")
deque.pop_front()
deque.print_structure()
print("---- POP REAR ----")
deque.pop_rear()
deque.print_structure()