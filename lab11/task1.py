from collections import deque
from typing import Any, Iterable
class Stack:
    """A simple LIFO stack using a Python list as the underlying container.

    Using list.append() and list.pop() on the end gives amortized O(1)
    push/pop behavior.

    Attributes:
        _items (list): Internal list storing stack elements.
    """

    def __init__(self, iterable: Iterable[Any] | None = None) -> None:
        """Initialize the stack optionally with items from an iterable.

        Args:
            iterable: Optional iterable of initial items; the last element
                of the iterable will be the top of the stack.
        """
        # Use a list because append/pop at the end are efficient.
        self._items: list[Any] = list(iterable) if iterable is not None else []

    def push(self, item: Any) -> None:
        """Push an item onto the top of the stack.

        Args:
            item: The value to push onto the stack.
        """
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the top item from the stack.

        Returns:
            The item that was on top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        """Return the top item without removing it.

        Returns:
            The item on top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        # Accessing the last element is O(1).
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check whether the stack is empty.

        Returns:
            True if the stack has no items, False otherwise.
        """
        return len(self._items) == 0

    def __len__(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)

    def __repr__(self) -> str:
        """Return a concise representation showing top on the right."""
        return f"Stack({self._items!r})"


class DequeStack:
    """Alternative stack implementation using collections.deque.

    deque can be slightly more memory-friendly and has guaranteed O(1)
    append/pop operations on both ends. For stack semantics we use the right
    end (index -1) similarly to the list-based implementation.
    """

    def __init__(self, iterable: Iterable[Any] | None = None) -> None:
        """Initialize deque-backed stack."""
        self._d = deque(iterable) if iterable is not None else deque()

    def push(self, item: Any) -> None:
        """Push item onto stack (right end of deque)."""
        self._d.append(item)

    def pop(self) -> Any:
        """Pop item from stack (right end)."""
        if not self._d:
            raise IndexError("pop from empty stack")
        return self._d.pop()

    def peek(self) -> Any:
        """Peek at the top item without removing it."""
        if not self._d:
            raise IndexError("peek from empty stack")
        return self._d[-1]

    def is_empty(self) -> bool:
        """Return True if stack is empty."""
        return not self._d

    def __len__(self) -> int:
        return len(self._d)

    def __repr__(self) -> str:
        return f"DequeStack({list(self._d)!r})"


# Sample tests for Stack operations
if __name__ == "__main__":
    # Basic usage demonstration with mixed-type sample data
    sample_data = [1, "two", 3.0]

    s = Stack()
    print("Initial empty:", s.is_empty())  # Expect True

    for item in sample_data:
        s.push(item)
        print(f"Pushed {item!r}, peek ->", s.peek())

    # Peek should show the last pushed element
    assert s.peek() == sample_data[-1]

    # Pop all items and print them (LIFO order)
    popped = []
    while not s.is_empty():
        popped_item = s.pop()
        popped.append(popped_item)
        print("Popped:", popped_item)

    # Popped should be reverse of sample_data
    assert popped == list(reversed(sample_data))
    print("Empty after pops:", s.is_empty())  # Expect True

    # Demonstrate error handling for empty stack operations
    try:
        s.pop()
    except IndexError as e:
        print("Correctly caught error on pop from empty stack:", e)

    try:
        s.peek()
    except IndexError as e:
        print("Correctly caught error on peek from empty stack:", e)

    # Demonstrate DequeStack as an alternative
    ds = DequeStack(sample_data)
    print("DequeStack initialized:", ds)
    ds.push("new-top")
    print("DequeStack peek:", ds.peek())
    print("DequeStack popped:", ds.pop())
    print("DequeStack final:", ds)


# Suggested optimizations and alternative notes:
#
# - collections.deque (provided above as DequeStack) can be used when you want
#   guaranteed O(1) operations at both ends. For a pure stack either list or
#   deque is fine; list is slightly more idiomatic and compact for stacks.
#
# - If you need thread-safe stacks, consider using queue.LifoQueue which
#   includes locking, at the cost of some overhead.
#
# - For extremely large datasets where occasional reallocation is a concern,
#   deque may be preferable since it avoids large contiguous memory blocks.
#
# - If memory snapshots or persistent (immutable) stacks are required,
#   consider using a linked list approach or a persistent data structure library.
#
# Feel free to ask for any of these alternative implementations or for
# benchmarks comparing list vs deque for your specific workload.