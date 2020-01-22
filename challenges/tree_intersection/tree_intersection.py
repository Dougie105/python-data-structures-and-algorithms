from .tree import *

def tree_intersection(tree1, tree2):
    lst = []

    def walk(node):
        if node.left:
            walk(node.left)
        compare(node, tree2.root)
        if node.right:
            walk(node.right)

    def compare(val1, val2):
        if val2.left:
            compare(val1, val2.left)
        if val1.value == val2.value:
            lst.append(val1.value)
            return
        if val2.right:
            compare(val1, val2.right)
    walk(tree1.root)

    if len(lst) > 0:
        return lst
    else:
        raise ValueError('No matching Values')