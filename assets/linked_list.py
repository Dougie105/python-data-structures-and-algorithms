class Node:
    '''
    __init__ is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
    '''
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None


    def insert(self, value):
        '''  
        Insert function checks to see if the list is empty. If the list is empty the value is made the head and inserted. If it is not the head, it makes the current head the next node and makes itself the head.
        '''
        node = Node(value)
        node.next = self.head
        self.head = node
        return value


    def includes(self, value):
        '''
        Includes Function runs through the linked-list and checks if the value is inside the list. If so it will throw True and False if there is no match.
        '''
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False


    def __str__(self):
        '''
        String Function changes all the values to strings and makes them a part of the same stringed linked list.
        '''
        as_string = ""
        curr = self.head
        while curr:
            as_string += f"{curr.value} "
            curr = curr.next
        return as_string


    def append(self, value):
        '''
        Append Function will hop from node to node to see if the next node has a next. Once the node is found that has no next the value is then set to be that existing nodes next therefore leaving the new values next to be nothing.
        '''
        if not self.head:
            self.insert(value)
            return
        else:
            current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)


    def insert_before(self, existing_value, value):
        '''
        Insert Before Function will iterate through the linked list and check for the existing value. Once that existing value is matched with the new value then the existing value then points to that value and tells the node that was origionally pointing to that node to point to him instead.
        '''
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
        """
        The while loop will run until the existing_value equils the value wanted. The new value will then point to the existing values next as its next and then have the existing node will point to the new next node.
        """
        current = self.head
        while current:
            if current.value == existing_value:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return True

            current = current.next

    # Kth From End Function


    def kth_from_end(self, k):
        """
        The while loop will only run until the range of i gets to be the specified length and then run the while loop, therefore moving both pointers at the same time until future hits the end of the linked list and returns the value of curr (being a specified kth distance away).
        """
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
