class PriorityQueue:
    def __init__(self):
        self.list=[]

    def __str__(self):
        return '\n'.join(map(str, self.list))
    
    def is_empty(self):
        return len(self.list)==0
    
    def add(self, e):
        self.list.append(e)

    def remove(self):
        if self.is_empty():
            return print("No tiene elementos para devolver")
        else:
            maxpriority=self.list[0]
            for item in self.list[1: ]:
                if item[0]<maxpriority[0]:
                    item=maxpriority

            self.list.remove(maxpriority)
            return maxpriority
        
    def min(self):
        if self.is_empty():
            return print("No tiene elementos para devolver")
        else:
            self.list[0]

    def len(self):
        return len(self.list)
    
    def delete(self):
        self.list=None

queue=PriorityQueue()
queue.add(4,"Luis")
queue.add(7,"Alex")
queue.add(5,"John")
print(queue)