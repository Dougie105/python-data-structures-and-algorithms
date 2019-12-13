class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert function

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        return value

    # Includes Function

    def includes(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    # String Function

    def __str__(self):
        as_string = ""
        curr = self.head
        while curr:
            as_string += f"{curr.value} "
            curr = curr.next
        return as_string

    # Append Function

    def append(self, value):
        if not self.head:
            self.insert(value)
            return
        else:
            current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    # Insert Before Function

    def insert_before(self, existing_value, value):

        current = self.head
        if current.value == existing_value:
            new_node = Node(value)
            new_node.next = current
            self.head = new_node
            return True

        while current.next:
            if current.next.value == existing_value:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next

    def insert_after(self, existing_value, value):
        current = self.head
        while current:
            if current.value == existing_value:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return True

            current = current.next

    # Kth From End Function

    """
    The while loop will only run until the range of i gets to be the specified length and then run the while loop, therefore moving both pointers at the same time until future hits the end of the linked list and returns the value of curr (being a specified kth distance away).
    """

    def kth_from_end(self, k):
        value_list = []
        if self.head:
            current = self.head
            while current.next:
                value_list.append(current.value)
                current = current.next

            value_list.append(current.value)

        if 0 <= k < len(value_list):
            return value_list[-(k + 1)]
        else:
            return "K is out of range"

#
