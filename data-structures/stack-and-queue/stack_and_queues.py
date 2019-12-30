class Node:
    '''Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.'''
    def __init__(self,value=None):
        self.value = value
        self.next = None

class Stack:
    '''Create a Stack class that has a top property. It creates an empty Stack when instantiated. This object should be aware of a default empty value assigned to top when the stack is created.'''
    def __init__(self):
        self.top = None

    def push(self, item):
        '''Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.'''
        node = Node(item)
        node.next = self.top
        self.top = node

    def pop(self):
        '''Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.'''
        current = self.top
        if current:
            self.top = current.next
        else:
            print('Stack is empty.')

    def peek(self):
        '''Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.'''
        if self.top == None:
            return None
        else:
            current = self.top
            return current.value

    def isEmpty(self):
        '''Define a method called isEmpty that does not take an argument, and returns a boolean indicating whether or not the stack is empty.'''
        return self.top == None


class Queue:
    '''Create a Queue class that has a front property. It creates an empty Queue when instantiated. This object should be aware of a default empty value assigned to front when the queue is created.'''
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        '''Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.'''
        node = Node(val)
        if self.rear:
            self.rear.next == node
        else:
            self.front = node
        self.rear = node

    def dequeue(self):
        '''Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.'''
        current = self.front
        if current != None:
            self.front = current.next
        else:
            print("Queue is empty.")


    def peek(self):
        '''Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.'''
        if self.front == None:
            return None
        current = self.front
        return self.front.value

    def isEmpty(self):
        '''Define a method called isEmpty that does not take an argument, and returns a boolean indicating whether or not the queue is empty.'''
        return self.front == None