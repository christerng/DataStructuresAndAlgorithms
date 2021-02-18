class LinkedQueue:

    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __repr__(self):
        out = ""
        node = self._head
        while node is not None:
            out += node._element
            node = node._next
        return out

    def __init__(self,):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self._size == 0:
            raise Exception("Queue is empty")
        return self._head._element

    def dequeue(self):
        if self._size == 0:
            raise Exception("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self._size == 0:
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self._size == 0:
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size == 0:
            raise Exception("Queue is empty")
        self.enqueue(self.dequeue())