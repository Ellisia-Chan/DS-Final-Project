# 🟧 in progress
# ✅ working
# ⚠️ Untested
# 🐞Debugging

class Queue:
    # ⚠️ Untested
    def __init__(self):
        self.queue = []
    
    # ⚠️ Untested
    def enqueue(self, element):
        self.queue.append(element)
    
    # ⚠️ Untested
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    # ⚠️ Untested
    def front(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    # ⚠️ Untested
    def isEmpty(self):
        return len(self.queue) == 0
    
    # ⚠️ Untested
    def size(self):
        return len(self.queue)
    
    def show_queue(self):
        print(self.queue)