
class Queue:
    def __init__(self, max_size):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def peek(self):
        if self.get_size() > 0:
            return self.head.get_value()
        else:
            print("Looks like this queue is empty!")

    def get_size(self):
        return self.size
    def has_space(self):
        if self.max_size == None:
            return True
        else: 
            return self.max_size > self.get_size()
    def is_empty(self):
            return self.get_size() == 0
