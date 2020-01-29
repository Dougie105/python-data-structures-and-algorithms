from graph import *

def get_edge(graph, lst):
    if not lst:
        return False
    if len(lst) == 1:
        return(True, 0)
    cost = 0
    current_node = None
    index = 1
    while index < len(lst):
        next_node = None
        if current_node == None:
            current_node = lst[0]
        neighbors = current_node.get_neighbors()
        target = lst[index]
        for neighbor in neighbors:
            if neighbor[0].data == target:
                cost += neighbor[1]
                next_node = neighbor[0]
        if next_node == None:
            return False
        else:
            current_node = next_node
            index += 1
    return(True, cost)
