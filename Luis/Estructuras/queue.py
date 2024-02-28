class Queue:
    def __init__(self):
        self.list=[]

    def __str__(self):
        return '\n'.join(map(str, self.list))
    
    def is_empty(self):
        return len(self.list)==0
    
    def enqueue(self, e):
        self.list.append(e)

    def dequeue(self):
        if self.is_empty():
            return print("No tiene elementos para devolver")
        else:
            self.list.pop(0)

    def top(self):
        if self.is_empty():
            return print("No tiene elementos para devolver")
        else:
            self.list[0]

    def len(self):
        return len(self.list)
    
queue=Queue()
queue.enqueue(3)
queue.enqueue(6)
queue.enqueue(10)
print(queue)