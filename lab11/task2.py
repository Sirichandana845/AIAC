from collections import deque
from time import perf_counter
class ListQueue:
    """Queue implemented with a Python list (enqueue: O(1), dequeue: O(n))."""

    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        # Removing from front causes O(n) shifts
        return self._data.pop(0)

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


class DequeQueue:
    """Queue implemented with collections.deque (enqueue and dequeue: O(1))."""

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


def benchmark(queue_cls, n):
    q = queue_cls()
    t0 = perf_counter()
    for i in range(n):
        q.enqueue(i)
    t_enqueue = perf_counter() - t0

    t0 = perf_counter()
    while not q.is_empty():
        q.dequeue()
    t_dequeue = perf_counter() - t0

    return t_enqueue, t_dequeue


if __name__ == "__main__":
    # Quick functional demo
    lq = ListQueue()
    dq = DequeQueue()

    for ch in ["a", "b", "c"]:
        lq.enqueue(ch)
        dq.enqueue(ch)

    print("ListQueue dequeue sequence:", [lq.dequeue(), lq.dequeue(), lq.dequeue()])
    print("DequeQueue dequeue sequence:", [dq.dequeue(), dq.dequeue(), dq.dequeue()])

    # Micro-benchmark to illustrate performance difference
    N = 20000
    le, ld = benchmark(ListQueue, N)
    de, dd = benchmark(DequeQueue, N)

    print(f"\nBenchmark for N={N} operations each:")
    print(f"ListQueue  - enqueue: {le:.4f}s, dequeue: {ld:.4f}s")
    print(f"DequeQueue - enqueue: {de:.4f}s, dequeue: {dd:.4f}s")

    # AI-generated performance comparison & recommendation (concise)
    ai_review = (
        "Performance review:\n"
        "- List-backed queue: enqueue is amortized O(1), but dequeue using pop(0) is O(n) "
        "because elements are shifted. This leads to poor dequeue performance as N grows.\n"
        "- Deque-backed queue: both enqueue (append) and dequeue (popleft) are O(1) "
        "amortized, implemented as a doubly-linked block deque under the hood.\n"
        "Recommendation: use collections.deque for queues in Python for efficient FIFO operations."
    )

    print("\nAI Review and Recommendation:")
    print(ai_review)