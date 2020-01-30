from graph import Graph, Vertex

def depth_first(graph, value):
    visited_lst = []
    visited_lst.append(value)

    def recursive(node):
        neighbors = Graph.get_neighbors(node, value)
        for neighbor in neighbors:
            if neighbor[0] not in visited_lst:
                visited_lst.append(neighbor[0])
                recursive(neighbor[0])
        return

    recursive(value)
    return visited_lst
