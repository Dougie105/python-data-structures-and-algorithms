class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    # Insert function

    def insert(self, value):
        node = Node(value, self.head)
        self.head = node

    # Includes Function

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    # String Method

    def __str__(self):
        as_string = "LinkedList : "
        current = self.head
        while current:
            as_string = f"[{current.value}] ->"
            current = current.next
        return as_string

    def append(self, val):
        current = self.head
        while current:
            if current.next == None:
                current.next = Node(val)
                return self.__str__()
            else:
                current = current.next
                self.head = Node(val)
                return self.__str__()

    def insert_before(self, value, new_val):
        if self.includes(value):
            new_node = Node(new_val)
            current = self.head
            while current.next:
                if current.next.value == value:
                    new_node = current.next
                    current.next = new_node.next
                    return self.__str__()
                else:
                    current = current.next
                    return self.__str__()

    def insert_after(self, existing, val):
        if self.includes(existing):
            current = self.head
            while current:
                if current.val == existing:
                    new_node = current.next
                    new_node.next = current.next
                    return self.__str__()
                else:
                    current = current.next
                    return self.__str__()


########################## DEMO TESTS ###############################


if __name__ == "__main__":
    ll = linked_list()
    ll.insert("apples")
    assert ll.head.value == "apples"
    ll.insert("bananas")

    assert ll.head.value == "bananas"
    assert ll.head.next.value == "apples"
    assert ll.head.next.next == None

    assert ll.includes("bananas") == True
    assert ll.includes("apples") == True
    assert ll.includes("candy") == False

    ll = linked_list()
    assert ll.includes("bananas") == False

    print("Success")
