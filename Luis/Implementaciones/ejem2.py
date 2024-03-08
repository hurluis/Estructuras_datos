class priorityqueue:
  def __init__(self):
    self.queuepriority1 = []
    self.queuepriority2 = []
    self.queuepriority3 = []

  def __str__(self):
    return ' '.join(map(str,self.queuepriority1))

  def is_empty(self):
    return len(self.queuepriority1) == 0 and len(self.queuepriority2) == 0 and len(self.queuepriority3) == 0

  def add(self, e):
    if e[0] == 1:
      self.queuepriority1.append(e)
    elif e[0] == 2:
      self.queuepriority2.append(e)
    elif e[0] == 3:
      self.queuepriority3.append(e)
    else:
      return "Error - No existe la prioridad"

  def remove_min(self):
    if self.is_empty():
      return 'no existen elementos en la pila para retornar'
    else:
       if len(self.queuepriority1) > 0:
        return self.queuepriority1.pop(0)
       elif len(self.queuepriority2) > 0:
        return self.queuepriority2.pop(0)
       elif len(self.queuepriority3) > 0:
        return self.queuepriority3.pop(0)


  def min(self):
     if self.is_empty():
      return 'no existen elementos en la pila para retornar'
     else:
       if len(self.queuepriority1) > 0:
        return self.queuepriority1[0]
       elif len(self.queuepriority2) > 0:
        return self.queuepriority2[0]
       elif len(self.queuepriority3) > 0:
        return self.queuepriority3[0]


  def len(self):
    return len(self.queuepriority1) + len(self.queuepriority2) + len(self.queuepriority3)

  def delete(self):
    self.queuepriority1 = None
    self.queuepriority2 = None
    self.queuepriority3 = None


custompriority = priorityqueue()
custompriority.add((2,'John'))
custompriority.add((3,'Jorge'))
custompriority.add((1,'Mario'))
print(custompriority)

custompriority.min()