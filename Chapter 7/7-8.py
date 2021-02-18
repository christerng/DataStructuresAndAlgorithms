class DoublyLinkedList:

    class _Node:
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)  # Sentinel header
        self._trailer = self._Node(None, None, None)  # Sentinel trailer
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        node._prev._next, node._next._prev = node._next, node._prev
        self._size -= 1
        element = node._element
        node._prev = node._prev = node._element = None
        return element

    def find_middle_node(self):
        if self._size == 0:
            return
        left = self._header._next
        right = self._trailer._prev
        while left is not right and left._next is not right:
            left = left._next
            right = right._prev
        return left
    

"""
Time complexity: O(n)
"""