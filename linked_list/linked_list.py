class node:
  def __init__(self, data= None):
    self.data = data
    self.head = None

class linked_list:
  def __init__(self):
    self.head = node()


  def insert(self, desired_location):
    new_node = node(desired_location)
    new_node.next = self.head
    self.head = new_node
    # while cur.head != None:
    #   cur = cur.head
    # cur.head = new_node


  def includes(self, data):
    if not self.head:
      return False
    cur = self.head
    while cur:
      if cur.data == data:
        return True
      cur = cur.head
    return False
  

  def length(self):
    cur = self.head
    total = 0
    while cur.head != None:
      total += 1
      cur = cur.head
    return total


  def to_list(self):
    elems = " "
    cur_node = self.head
    while cur_node.head != None:
      cur_node = cur_node.head
      elems += " " + str(cur_node.data)

    print(elems)
   

my_list = linked_list()
my_list.to_list()

my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.to_list()