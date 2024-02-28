class Stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        return (map(str, reversed(self.list)))
    
    def is_empty(self):
        return len(self.list)==0
    
    def push(self, e):
        self.list.append(e)

    def pop(self):
        if self.is_empty():
            return print("No tiene elementos para devolver")
        else:
            self.list.pop()

    def top(self):
        if self.is_empty():
            return print("No tiene elementos para devolver")
        else:
            self.list[-1]

    def len(self):
        return len(self.list)
    
stack=Stack()
stack.push(3)
stack.push(6)
stack.push(10)
print(stack)