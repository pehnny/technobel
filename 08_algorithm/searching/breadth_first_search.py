from collections import deque
from collections.abc import Callable
from dataclasses import dataclass
from typing import Optional

"""Breadth first search is a pertinent algorithm to
find the shortest path between two nodes of a network.
"""

network = {}
network["you"] = ["alice", "bob", "claire"]
network["bob"] = ["anuj", "peggy"]
network["alice"] = ["peggy"]
network["claire"] = ["thom", "jonny"]
network["anuj"] = []
network["peggy"] = []
network["thom"] = []
network["jonny"] = []

def is_person_seller(name: str) -> bool:
    return name[-1] == "m"

def breadth_first_search(
        network: dict[str, list[str]], 
        key: str, 
        condition: Callable[[str], bool]
    ) -> bool:
    """Search for a connexion between the entry point of a network
    and a specific elemnt determined by the `condition`.

    Complexity is `O(V+E)` where `V` is the number of Vertices,
    the number of different values of the network,
    and `E` is the number of Edges, the total number of connexion between
    each elements.

    Exemple
    -------
    ``breadth_first_search({...}, "...", lambda key: key == target)``
    """
    queue = deque(network[key])
    checked = set()
    
    while queue:
        first = queue.popleft()
        if first not in checked:
            if condition(first):
                return True
            queue.extend(network[first])
            checked.add(first)
    return False

@dataclass
class Node[T]:
    value: T
    children: Optional[list[Node[T]]]

def breadth_search[T](
        node: Node[T], 
        target: T, 
    ) -> bool:
    """Search for a connexion between the entry point of a tree
    and a specific elemnt determined by the `condition`.
    A tree is a special kind of network where every node has
    only one parent (except the root node). This data structure
    avoids infinite loops naturally.

    Complexity is `O(V+E)` where `V` is the number of Vertices,
    the number of different values of the network,
    and `E` is the number of Edges, the total number of connexion between
    each elements.

    Exemple
    -------
    ``breadth_first_search({...}, "...", lambda key: key == target)``
    """
    queue = deque([node])
    while queue:
        current = queue.popleft()
        if current.value == target:
            return True
        if current.children:
            queue.extend(current.children)
    return False

