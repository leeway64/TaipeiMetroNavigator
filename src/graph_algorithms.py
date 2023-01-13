from collections import deque
from typing import List, Dict

from pyinline import inline


# The @inline decorator turns find_shortest_path into an inline function
@inline
def find_shortest_path(graph: Dict[str, List[str]], src: str, dest: str):  # Type hinting
    """
    Find the shortest path and distance between the source and destination stations.

    :param graph: An undirected graph in dictionary form. Each key represents a node in the graph,
    and each key's value represents that node's neighbors.
    :type graph: Dict[str, List[str]]
    :param src: The starting station/node
    :type src: str
    :param dest: The destination station/node
    :type dest: str
    :return: A dictionary containing the shortest path between src and dest and the number of nodes
    between them.
    :rtype: Dict
    """
    visited = set(src)
    shortest_path = [[src]]
    # Use BFS
    # We need to embed both the current node and the current distance into each queue element.
    current_node = deque([[src, 0]])
    while current_node:
        current, distance = current_node.pop()
        current_path = shortest_path.pop(0)

        if current == dest:
            return {"shortest_path": current_path, "distance": distance}

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                # I need to explicitly create another list, because Python automatically assigns by
                # reference. That means that writing previous_path = current_shortest_path means
                # that previous_path still points to the current_shortest_path list.
                previous_path = list(current_path)

                previous_path.append(neighbor)

                shortest_path.append(previous_path)
                current_node.appendleft([neighbor, distance + 1])

    return {"shortest_path": None, "distance": None}
