class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start = None):
        self.start = start
    
    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, data):
        new_node = Node(prev = None, item = data, next = self.start)
        if not self.is_empty():
            self.start.prev = new_node
        self.start = new_node

    def insert_at_end(self, data):
        if self.is_empty():
            self.start = Node(prev = None, item = data, next = None)
            return
        
        last = self.start
        while last.next:
            last = last.next
        
        new_node = Node(prev = last, item = data, next = None)
        last.next = new_node 
        

    def search(self, data):
        current = self.start
        while current:
            if current.item == data:
                return True
            current = current.next
        return False
    
    def insert_after(self, afterItem, data ):
        if self.is_empty():
            return
        
        current = self.start
        while current:
            if current.item == afterItem:
                break
            current = current.next
        
        if current is None:
            print(f"Item {afterItem} not found in the list.")
            return
        
        new_node = Node(prev = current, item = data, next = current.next)
        if current.next:
            current.next.prev = new_node
        current.next = new_node


    def print_list(self):
        current = self.start
        while current:
            print(current.item, end ='-> ')
            current = current.next
        
    def delete_first(self):
        if self.is_empty():
            print("List is empty.")
            return
        
        self.start = self.start.next
        if self.start:
            self.start.prev = None
    
    def delete_last(self):
        if self.is_empty():
            print("List is empty.")
            return
        
        last = self.start
        while last.next:
            last = last.next
        
        if last.prev:
            last.prev.next = None
        else:
            self.start = None
        last.prev = None 

    def delete_item(self, data):
        if self.is_empty():
            print("List is empty.")
            return
        
        current = self.start
        while current:
            if current.item == data:
                break
            current = current.next
        
        if current is None:
            print(f"Item {data} not found in the list.")
            return
        
        if current.prev:
            current.prev.next = current.next
        else:
            self.start = current.next
        
        if current.next:
            current.next.prev = current.prev
        last = current
        current = None
        del last 


# Testing the implementation

dll = DLL()
dll.insert_at_start(10)
dll.insert_at_start(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

print("Original list:")

dll.print_list()

dll.insert_after(20, 25)

print("\nList after inserting 25 after 20:")

dll.print_list()

print("\nSearch for 25:", dll.search(25))

dll.delete_first()

print("\nList after deleting the first node:")

dll.print_list()

dll.delete_last()

print("\nList after deleting the last node:")

dll.print_list()

dll.delete_item(30) 

print("\nList after deleting 30:")

dll.print_list()
     