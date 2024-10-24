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