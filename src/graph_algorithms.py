from collections import deque
from typing import List, Dict

from pyinline import inline


# The @inline decorator turns find_shortest_path into an inline function
@inline
def find_shortest_path(graph: Dict[str, List[str]], src: str, dest: str):  # Type-hinting
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
                # print(f"previous path: {previous_path}")

                previous_path.append(neighbor)
                # print(f"previous path after append: {previous_path}")

                shortest_path.append(previous_path)
                current_node.appendleft([neighbor, distance + 1])

    return {"shortest_path": None, "distance": None}
