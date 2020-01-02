class Queue:
    '''Create a queue calss'''
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        '''Add to your queue'''
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node

    def dequeue(self):
        '''Remove from queue'''
        current = self.front
        if current != None:
            self.front = current.next
            return current
        else:
            print("Queue is empty.")

    def peek(self):
        '''Check value of whats next in the queue'''
        if self.front == None:
            return None
        current = self.front
        return self.front.value

    def isEmpty(self):
        '''Returns if the queue is empty or not'''
        return self.front == None


class Node:
    '''Set up a node class'''
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.next = None
        self.rear = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self, node=None, arr=[]):
        node = node or self.root

        arr.append(node.value)

        if node.left:
            self.pre_order(node.left, arr)
        if node.right:
            self.pre_order(node.right, arr)
        return arr

    def in_order(self, node=None, arr=[]):
        node = node or self.root
        if node.left:
            self.in_order(node.left, arr)

        arr.append(node.value)

        if node.right:
            self.in_order(node.right, arr)
        return arr

    def post_order(self, node=None, arr=[]):
        node = node or self.root
        if node.left:
            self.post_order(node.left, arr)
        if node.right:
            self.post_order(node.right, arr)

        arr.append(node.value)

        return arr

def breadth_first(tree):
    """Write a breadth first traversal method which takes a Binary Tree as its unique input. Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered."""

    if tree.root is None:
        return None
    queue = Queue()
    lst = []
    queue.enqueue(tree.root)
    while queue.front:
        node = queue.front.value
        lst.append(node.value)
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)
        queue.dequeue()
    return lst


class BinarySearchTree(BinaryTree):
    def add(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return value
        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = node
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    return
                current = current.right

