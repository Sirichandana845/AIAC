from typing import Optional, List
class Node:
    """
    Node of a Binary Search Tree.

    Attributes:
        key: The value stored in the node.
        left: Left child Node or None.
        right: Right child Node or None.
    """
    def __init__(self, key: int):
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.key})"


class BST:
    """
    Simple Binary Search Tree (BST) implementation supporting insertion,
    search, and inorder traversal.
    """
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, key: int) -> None:
        """
        Insert key into the BST. Duplicate keys are ignored.

        Args:
            key: Integer value to insert.
        """
        if self.root is None:
            self.root = Node(key)
            return

        parent = None
        current = self.root
        while current:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                # Duplicate; do nothing.
                return

        if key < parent.key:
            parent.left = Node(key)
        else:
            parent.right = Node(key)

    def search(self, key: int) -> Optional[Node]:
        """
        Search for a key in the BST.

        Args:
            key: Integer to search for.

        Returns:
            The Node containing key if found, otherwise None.
        """
        current = self.root
        while current:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_traversal(self) -> List[int]:
        """
        Perform an inorder traversal of the BST.

        Returns:
            A list of keys in ascending order.
        """
        result: List[int] = []

        def _inorder(node: Optional[Node]) -> None:
            if node is None:
                return
            _inorder(node.left)
            result.append(node.key)
            _inorder(node.right)

        _inorder(self.root)
        return result


if __name__ == "__main__":
    # Build BST from a list of integers
    values = [7, 3, 9, 1, 5, 8, 10, 4, 6, 2]
    bst = BST()
    for v in values:
        bst.insert(v)

    # Inorder traversal should produce a sorted list
    print("Inorder traversal:", bst.inorder_traversal())

    # Test search() for present and absent elements
    tests = [5, 11, 1, 0, 10]
    for t in tests:
        node = bst.search(t)
        print(f"Search {t}: {'Found' if node else 'Not found'}")