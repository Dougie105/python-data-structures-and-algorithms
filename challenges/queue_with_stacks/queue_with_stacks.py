class Node:
    """ Class for the Node instances"""

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """Class Stack wich implements Stack data structure with its common methods"""

    def __init__(self):
        """Initiate Stack"""

        self.top = None

    def is_empty(self):
        """Is the Stack is empty"""
        if self.top == None:
            return True
        return False

    def push(self, value):
        """Method takes any value as an argument and adds a new node with that value to the top of the stack """

        new_node = Node(value)
        new_node.next, self.top = self.top, new_node

    def pop(self):
        """Method that removes the node from the top of the stack, and returns the node’s value."""

        if not self.is_empty():
            temp, self.top = self.top, self.top.next
            temp.next = None
            return temp.value
        else:
            return None

    def peek(self):
        """Method that returns the value of the node located on top of the stack, without removing it from the stack."""

        if not self.is_empty():
            return self.top.value
        else:
            return None


class PseudoQueue:
    def __init__(self, stack1):
        """Initiate PseudoQueue class with one empty and one given stack"""
        self.stack1 = stack1
        self.stack2 = Stack()

    def enqueue(self, value):
        """Method to inserts value into the PseudoQueue, using a first-in, first-out approach."""
        self.stack1.push(value)

    def dequeue(self):
        """"Method to extract a value from the PseudoQueue, using a first-in, first-out approach. Returns value of extracted node """

        if self.stack1.top == None:
            raise Exception("PseudoQueue is empty")
        while self.stack1.top != None:
            poped_file = self.stack1.pop()

            self.stack2.push(poped_file)

        pop_val = self.stack2.pop()

        while self.stack2.top != None:
            self.stack1.push(self.stack2.pop())
        return pop_val
        
