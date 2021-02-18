class PositionalList:

    class _Node:
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    class _Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return self._make_position(newest)

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """{is_empty, first, last, prev, next, add_after, add_first}"""
        if self.is_empty():
            return self.add_first(e)
        return self.add_after(self.last(), e)
        
    def add_before(self, p, e):
        """{is_empty, first, last, prev, next, add_after, add_first}"""
        try:
            return self.add_after(self.before(p), e)
        except: 
            return self.add_first(e)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

    def _delete_node(self, node):
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def _validate(self, p):
        if not isinstance(p, self._Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return
        return self._Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor
            cursor = self.after(cursor)

    def __reversed__(self):
        cursor = self.last()
        while cursor is not None:
            yield cursor
            cursor = self.before(cursor)

    def move_to_front(self, p):
        if p == self.first():
            return

        p._node._prev._next = p._node._next
        p._node._next._prev = p._node._prev

        p._node._prev = self._header
        p._node._next = self._header._next

        self._header._next._prev = p._node
        self._header._next = p._node


if __name__ == "__main__":
    p = PositionalList()
    a = p.add_last("a")
    b = p.add_last("b")
    c = p.add_last("c")
    d = p.add_last("d")
    e = p.add_last("e")
    f = p.add_last("f")

    for position in (a, b, c, d, e, f, a, c, f, b, d, e):
        p.move_to_front(position)

    for position in p:
        print(position.element(), end=" ")