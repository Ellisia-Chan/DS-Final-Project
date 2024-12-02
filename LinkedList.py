# 🟧 in progress
# ✅ working
# ⚠️ Untested
# 🐞Debugging

# Create a Node class to create a node
class Node:
    # ✅ working
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class Linked_List:
    # ✅ working
    def __init__(self):
        self.head = None

    # ✅ working
    # Insert a node at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    # ✅ working
    # Update the data of a node at a given index
    def update_node(self, val, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            current_node.data = val
        else:
            print("Index out of range")

    # ✅ working
    # Return the size of the linked list
    def size(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    # 🐞Debugging
    # Print the linked list
    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    # ✅ working
    def get_linked_list(self) -> list:
        Linked_List = []
        current_node = self.head
        while current_node:
            Linked_List.append(current_node.data)
            current_node = current_node.next
        return Linked_List
    
    # ✅ working
    def get_node(self, index: int) -> list:
        current_node = self.head
        position = 0
        index -= 1
        
        while current_node is not None:
            if position == index:
                return current_node.data
            position += 1
            current_node = current_node.next
        return None