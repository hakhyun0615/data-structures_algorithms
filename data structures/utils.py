class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    # add very end
    def enqueue(self, item):
        self.items.append(item)
    
    # delete very front and return
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)
        
    def size(self):
        return len(self.items)

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
    
    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next
    
    def set_item(self, new_item):
        self.item = new_item
    
    def set_next(self, new_next):
        self.next = new_next

class BTNode:
    def __init__(self, item, left_child = None, right_child = None):
        self.key = item
        self.left = left_child
        self.right = right_child

    def get_key(self): 
        return self.key
    
    def get_left(self): 
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_key(self, new_item):
        self.key = new_item
    
    def set_left(self, new_left_child):
        self.left = new_left_child
    
    def set_right(self, new_right_child):
        self.right = new_right_child