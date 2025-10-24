from typing import Any, List, Optional
class Node:
    def __init__(self, value: Any):
        self.value: Any = value
        self.next: Optional["Node"] = None  # pointer to the next node


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None  # start with an empty list

    def insert_at_end(self, value: Any) -> None:
        """
        Insert a new node with `value` at the end of the list.
        Pointer updates:
        - If list is empty, set head to the new node (head now points to the new node).
        - Otherwise, walk to the last node and set last.next to the new node
          (the previous last node's `next` pointer is updated to point to the new node).
        """
        new_node = Node(value)

        if self.head is None:
            # Empty list: update head pointer to reference the new node.
            self.head = new_node
            return

        # Non-empty list: traverse until current is the last node (current.next is None)
        current = self.head
        while current.next is not None:
            current = current.next

        # current is the former last node; update its next pointer to the new node
        current.next = new_node

    def delete_value(self, value: Any) -> bool:
        """
        Delete the first node with the given value.
        Returns True if a node was deleted, False otherwise.

        Pointer updates:
        - If the node to delete is the head:
          update head to head.next (head now points to the second node or None).
        - If the node is in the middle or end:
          update prev.next to current.next to bypass `current` (prev.next now points to node after current).
        """
        current = self.head
        prev: Optional[Node] = None

        # Traverse to find the node to delete
        while current is not None:
            if current.value == value:
                if prev is None:
                    # Node to delete is the head: move head pointer forward
                    # This drops the reference to the old head, effectively deleting it.
                    self.head = current.next
                else:
                    # Bypass current by linking prev.next to current.next
                    # This removes current from the chain while preserving the rest of the list.
                    prev.next = current.next
                return True  # deletion successful
            prev = current
            current = current.next

        return False  # value not found

    def traverse(self) -> List[Any]:
        """
        Return a list of node values in order by following next pointers from head.
        This does not modify any pointers.
        """
        values: List[Any] = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next  # move to the next node by following the next pointer
        return values


if __name__ == "__main__":
    # Simple demonstration and quick tests.
    ll = LinkedList()

    # Insert into empty list
    ll.insert_at_end(10)       # head -> [10]
    ll.insert_at_end(20)       # head -> [10] -> [20]
    ll.insert_at_end(30)       # head -> [10] -> [20] -> [30]
    print("After inserts:", ll.traverse())  # expected [10, 20, 30]

    # Delete middle value
    deleted = ll.delete_value(20)  # head -> [10] -> [30]
    print("Deleted 20?", deleted, "List now:", ll.traverse())  # expected True, [10, 30]

    # Delete head
    deleted = ll.delete_value(10)  # head -> [30]
    print("Deleted 10?", deleted, "List now:", ll.traverse())  # expected True, [30]

    # Delete tail / only element
    deleted = ll.delete_value(30)  # head -> None
    print("Deleted 30?", deleted, "List now:", ll.traverse())  # expected True, []

    # Delete from empty list
    deleted = ll.delete_value(40)
    print("Deleted 40 from empty list?", deleted, "List now:", ll.traverse())  # expected False, []

    # Insert after deletions
    ll.insert_at_end(50)
    print("Final list:", ll.traverse())  # expected [50]

    # Suggested test cases (to validate more thoroughly):
    # 1. Insert multiple values and traverse to confirm order.
    # 2. Delete a value not present in the list (should return False, list unchanged).
    # 3. Delete the head when multiple nodes exist.
    # 4. Delete the tail when multiple nodes exist.
    # 5. Delete the only element in a single-element list (head becomes None).
    # 6. Insert into an initially empty list.
    # 7. Delete when list is empty (no error, return False).
    # 8. Repeatedly insert and delete in alternating order to check pointer integrity.