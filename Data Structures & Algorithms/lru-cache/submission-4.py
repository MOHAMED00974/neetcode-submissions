from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.items= OrderedDict()
        self.count= capacity

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        else:
            self.items.move_to_end(key)
            return self.items[key]

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items.move_to_end(key)    
            self.count+= 1    
        
        self.items[key]= value
        
        if self.count:
            self.count-= 1
            return 
        
        self.items.popitem(last=False)