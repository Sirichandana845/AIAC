from collections import deque
from typing import Dict, List, Set, Any
class Graph:
    def __init__(self, directed: bool = False):
        # adjacency list: vertex -> list of neighbor vertices
        self.adj: Dict[Any, List[Any]] = {}
        self.directed = directed

    def add_vertex(self, v: Any) -> None:
        # ensure vertex exists in adjacency list
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u: Any, v: Any) -> None:
        # add vertices if missing
        self.add_vertex(u)
        self.add_vertex(v)
        # add edge u -> v
        self.adj[u].append(v)
        # if undirected, also add v -> u
        if not self.directed:
            self.adj[v].append(u)

    def bfs(self, start: Any) -> List[Any]:
        """
        Breadth-First Search (BFS)
        - Uses a queue to explore neighbors level by level.
        - Marks nodes as visited as soon as they are enqueued to avoid duplicates in the queue.
        Returns the list of visited nodes in BFS order.
        """
        if start not in self.adj:
            return []

        visited: Set[Any] = set()   # set to track visited vertices
        order: List[Any] = []       # traversal order
        q = deque()

        # start traversal by enqueueing start and marking visited
        q.append(start)
        visited.add(start)

        while q:
            current = q.popleft()  # FIFO: process the oldest enqueued vertex
            order.append(current)

            # iterate neighbors and enqueue any not yet visited
            for neighbor in self.adj[current]:
                if neighbor not in visited:
                    visited.add(neighbor)  # mark when enqueuing to avoid duplicates
                    q.append(neighbor)

        return order

    def dfs_recursive(self, start: Any) -> List[Any]:
        """
        Depth-First Search (DFS) - recursive implementation.
        - Explores as deep as possible along each branch before backtracking.
        - Natural and simple to express via recursion.
        Returns the list of visited nodes in DFS order.
        """
        order: List[Any] = []
        visited: Set[Any] = set()

        def _dfs(v: Any):
            visited.add(v)      # mark node on entry
            order.append(v)     # record visitation
            # recurse on neighbors that are not yet visited
            for neighbor in self.adj.get(v, []):
                if neighbor not in visited:
                    _dfs(neighbor)

        if start in self.adj:
            _dfs(start)
        return order

    def dfs_iterative(self, start: Any) -> List[Any]:
        """
        Depth-First Search (DFS) - iterative implementation using a stack.
        - Uses an explicit stack instead of system recursion.
        - To mimic recursive order, neighbors are pushed in reversed order.
        Returns the list of visited nodes in DFS order.
        """
        if start not in self.adj:
            return []

        visited: Set[Any] = set()
        order: List[Any] = []
        stack: List[Any] = [start]

        while stack:
            current = stack.pop()  # LIFO: take the most recently pushed vertex
            if current in visited:
                continue
            visited.add(current)   # mark when popped (first time seen)
            order.append(current)

            # push neighbors onto the stack. Reversing helps produce the same order
            # as a typical recursive DFS that visits neighbors in the listed order.
            neighbors = self.adj[current]
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

        return order


# Demonstration and short comparison
if __name__ == "__main__":
    # build a sample undirected graph:
    # A - B - D
    # |   |
    # C - E
    g = Graph(directed=False)
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "E")]
    for u, v in edges:
        g.add_edge(u, v)

    print("Adjacency list:", g.adj)
    print("BFS starting at A:", g.bfs("A"))
    print("DFS recursive starting at A:", g.dfs_recursive("A"))
    print("DFS iterative starting at A:", g.dfs_iterative("A"))

    # Comparison (explanatory comment):
    # - Recursive DFS is concise and maps directly to the conceptual algorithm,
    #   but may hit Python's recursion depth limit on very deep graphs.
    # - Iterative DFS (with an explicit stack) avoids recursion limits and can be
    #   more efficient in languages/situations where function call overhead matters.