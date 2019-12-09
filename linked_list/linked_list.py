class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = Node()

    def insert(self, desired_location):
        new_node = Node(desired_location)
        new_node.next = self.head
        self.head = new_node
        return desired_location

    def includes(self, data):
        if not self.head:
            return False
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def to_list(self):
        value = " "
        cur = self.head
        while cur.next != None:
            value += " " + str(cur.data)
            cur = cur.next
        print(value)
        return value
